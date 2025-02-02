🛜 Status_bot 🛜

A lightweight .py Discord bot configuration that tracks YouTube live status, updates a pinned message, and cleans up old notifications for a clutter-free server. 🚀

Features

✅ Auto-updates status – Edits a pinned message to show live/offline status.✅ Sends live notifications – Alerts the server when a stream starts.✅ Deletes old notifications – Keeps the chat clean by removing outdated messages.✅ Lightweight & efficient – Runs smoothly with minimal resource usage.

Installation

1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/status_bot.git
cd status_bot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up the .env File

Create a .env file in the project directory and add:

DISCORD_TOKEN=your_discord_bot_token
YOUTUBE_API_KEY=your_youtube_api_key
YOUTUBE_CHANNEL_ID=your_youtube_channel_id
DISCORD_CHANNEL_ID=your_discord_channel_id
MESSAGE_ID=your_discord_message_id  # ID of the pinned message to edit

4️⃣ Run the Bot

python status_bot.py

_________________

Deploying to Heroku

1️⃣ Login & Create App

heroku login
heroku create your-app-name

2️⃣ Set Config Variables

heroku config:set DISCORD_TOKEN=your_discord_bot_token
heroku config:set YOUTUBE_API_KEY=your_youtube_api_key
heroku config:set YOUTUBE_CHANNEL_ID=your_youtube_channel_id
heroku config:set DISCORD_CHANNEL_ID=your_discord_channel_id
heroku config:set MESSAGE_ID=your_discord_message_id

3️⃣ Deploy to Heroku

git add .
git commit -m "Initial"
git push heroku main
heroku ps:scale worker=1

How It Works

1️⃣ Bot checks YouTube every (60) seconds for live status.2️⃣ Edits the pinned message to show "🔴 LIVE NOW" or "⚫ Currently Offline".3️⃣ Sends a one-time notification when a stream starts.4️⃣ Deletes old notifications to prevent clutter.5️⃣ Resets when offline, ensuring the next stream gets a fresh announcement.


Feel free to fork this repo, submit issues, or open a pull request if you have improvements! 🚀

License

MIT License. Free to use and modify. 

```
██╗   ██╗███╗   ██╗██╗   ██╗███╗   ██╗ ██████╗ 
╚██╗ ██╔╝████╗  ██║╚██╗ ██╔╝████╗  ██║██╔════╝ 
 ╚████╔╝ ██╔██╗ ██║ ╚████╔╝ ██╔██╗ ██║██║  ███╗
  ╚██╔╝  ██║╚██╗██║  ╚██╔╝  ██║╚██╗██║██║   ██║
   ██║   ██║ ╚████║   ██║   ██║ ╚████║╚██████╔╝
   ╚═╝   ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝
                                               
                                                                                                               
Developer: ynyng - ynyng LLC - ynyng@ynyng.org
