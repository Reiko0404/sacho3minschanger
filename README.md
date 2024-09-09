## Discord Nickname Changer Bot
## THIS MAKE FOR FRANK FRIEND NICKNAME xD 

This bot automatically changes the nickname of a specified Discord user at a set interval. The list of nicknames to cycle through is loaded from a JSON file.

### Features

* Periodically changes the nickname of a specified Discord user.
* Manages the list of nicknames to use from a `nicks.json` file.
* Allows customization of the nickname change interval.

### How to Use

1. **Install Required Libraries:**
```bash
pip install discord
```

2. **Configure Bot Token and Settings:**
   - Replace `YOUR_DISCORD_BOT_TOKEN` with your bot's token.
   - Replace `GUILD_ID` with the ID of the server where the bot will change nicknames.
   - Replace `TARGET_USER_ID` with the ID of the user whose nickname will be changed.
   - Set `INTERVAL` to the desired nickname change interval in seconds.

3. **Create Nickname List File:**
   - Create a file named `nicks.json` and populate it with a JSON array of nicknames. Example:
   ```json
   ["Nickname1", "Nickname2", "Nickname3"]
   ```

4. **Run the Bot:**
   ```bash
   python your_bot_file.py
   ```

### Permissions

* The bot requires the "Manage Nicknames" permission in the server to change nicknames.
* The bot's role must be higher than the role of the user whose nickname is being changed.
* The bot cannot change the nickname of the server owner.

### Notes

* Ensure that the `nicks.json` file is in the same directory as the Python code.
* Respect Discord API rate limits when setting the nickname change interval. 
* Check the logs for any errors that may occur during operation.

### Example `nicks.json` file:

```json
[
  "Awesome User",
  "Cool Dude",
  "The Legend",
  "Pro Gamer"
]
```

This bot provides a simple way to automate nickname changes for a Discord user, adding a bit of fun or dynamism to their presence on your server.
