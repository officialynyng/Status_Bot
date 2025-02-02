import discord
import requests
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))  # Fixed message to edit

# YouTube API URL for checking live status
YOUTUBE_API_URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={YOUTUBE_CHANNEL_ID}&eventType=live&type=video&key={YOUTUBE_API_KEY}"

# Discord bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

was_live = False  # Tracks whether the last check detected a live stream
last_notification_id = None  # Stores last live notification message ID

async def check_youtube_stream():
    """Check if the YouTube channel is live and update the Discord message."""
    global was_live, last_notification_id
    await client.wait_until_ready()
    channel = client.get_channel(DISCORD_CHANNEL_ID)

    try:
        message = await channel.fetch_message(MESSAGE_ID)  # Fetch existing status message
    except discord.NotFound:
        print("Error: Message ID not found. Ensure the bot has permission to access the channel.")
        return

    while not client.is_closed():
        try:
            response = requests.get(YOUTUBE_API_URL).json()
            live_streams = response.get("items", [])

            if live_streams:
                stream = live_streams[0]
                video_id = stream["id"]["videoId"]
                title = stream["snippet"]["title"]
                thumbnail = stream["snippet"]["thumbnails"]["high"]["url"]
                stream_url = f"https://www.youtube.com/watch?v={video_id}"

                embed = discord.Embed(
                    title=f"🔴 LIVE NOW: {title}",
                    url=stream_url,
                    description="Click the link above to watch the stream!",
                    color=discord.Color.red()
                )
                embed.set_image(url=thumbnail)

                await message.edit(content="", embed=embed)

                # Notify once per stream and delete the last notification
                if not was_live:
                    if last_notification_id:
                        try:
                            last_message = await channel.fetch_message(last_notification_id)
                            await last_message.delete()
                        except discord.NotFound:
                            pass  # If the message was already deleted

                    notification = await channel.send(f"🚀 **{title}** is now live! Watch here: {stream_url}")
                    last_notification_id = notification.id  # Store new notification ID
                    was_live = True  # Prevent duplicate notifications

            else:
                # Delete the last live notification when going offline
                if was_live and last_notification_id:
                    try:
                        last_message = await channel.fetch_message(last_notification_id)
                        await last_message.delete()
                        last_notification_id = None  # Reset after deleting
                    except discord.NotFound:
                        pass  # If the message was already deleted

                embed = discord.Embed(
                    title="⚫ Currently Offline",
                    description="Stay tuned for the next live stream!",
                    color=discord.Color.dark_gray()
                )
                await message.edit(content="", embed=embed)
                was_live = False  # Reset flag for next stream

        except Exception as e:
            print(f"Error checking YouTube stream: {e}")

        await asyncio.sleep(60)  # Check every minute

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    client.loop.create_task(check_youtube_stream())

client.run(DISCORD_TOKEN)

