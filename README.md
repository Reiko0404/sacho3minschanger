# sacho3minschanger
A bot that changes its nickname for pranks every 3 minutes.
Discord Nickname Changer Bot

This bot automatically changes the nickname of a specified Discord user at a set interval. The list of nicknames to cycle through is loaded from a JSON file.

Features

Periodically changes the nickname of a specified Discord user.

Manages the list of nicknames to use from a nicks.json file.

Allows customization of the nickname change interval.

How to Use

Install Required Libraries:

pip install discord
content_copy
Use code with caution.
Bash

Configure Bot Token and Settings:

Replace YOUR_DISCORD_BOT_TOKEN with your bot's token.

Replace GUILD_ID with the ID of the server where the bot will change nicknames.

Replace TARGET_USER_ID with the ID of the user whose nickname will be changed.

Set INTERVAL to the desired nickname change interval in seconds.

Create Nickname List File:

Create a file named nicks.json and populate it with a JSON array of nicknames. Example:

["Nickname1", "Nickname2", "Nickname3"]
content_copy
Use code with caution.
Json

Run the Bot:

python your_bot_file.py
content_copy
Use code with caution.
Bash
Permissions

The bot requires the "Manage Nicknames" permission in the server to change nicknames.

The bot's role must be higher than the role of the user whose nickname is being changed.

The bot cannot change the nickname of the server owner.

Notes

Ensure that the nicks.json file is in the same directory as the Python code.

Respect Discord API rate limits when setting the nickname change interval.

Check the logs for any errors that may occur during operation.

Example nicks.json file:
[
  "Awesome User",
  "Cool Dude",
  "The Legend",
  "Pro Gamer"
]
content_copy
Use code with caution.
Json

This bot provides a simple way to automate nickname changes for a Discord user, adding a bit of fun or dynamism to their presence on your server.
