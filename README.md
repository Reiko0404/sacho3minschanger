## Discord Nickname Changer Bot (Prank Edition)

This bot is designed to playfully prank a friend on Discord by automatically changing their nickname at set intervals. The list of nicknames to cycle through is loaded from a JSON file, allowing for creative and potentially embarrassing possibilities. 

### Features

* **Automated Pranks:** Periodically changes the nickname of a targeted Discord user, keeping them on their toes.
* **Customizable Nickname List:**  Manages the list of nicknames to use from a `nicks.json` file, allowing for personalized and hilarious options.
* **Adjustable Prank Frequency:**  Allows customization of the nickname change interval, controlling the intensity of the prank.

### How to Use (For Mischief Makers)

1. **Install Required Libraries:**
   ```bash
   pip install discord
   ```

2. **Configure Bot Token and Target:**
   - Replace `YOUR_DISCORD_BOT_TOKEN` with your bot's token.
   - Replace `GUILD_ID` with the ID of the server where the prank will take place.
   - Replace `TARGET_USER_ID` with the ID of your unsuspecting friend (the target of the prank).
   - Set `INTERVAL` to the desired nickname change interval in seconds (shorter intervals = more chaos).

3. **Craft the Perfect Nickname List:**
   - Create a file named `nicks.json` and populate it with a JSON array of funny, embarrassing, or inside-joke nicknames. Example:
     ```json
     ["Goofy Gus", "Chicken Nugget", "Lord of the Lag", "The One Who Always Gets Pranked"]
     ```

4. **Unleash the Bot (and the Laughter):**
   ```bash
   python your_bot_file.py
   ```

### Permissions (For Pranking Success)

* The bot requires the "Manage Nicknames" permission in the server to change nicknames.
* The bot's role must be higher than the role of the user being pranked.
* The bot cannot change the nickname of the server owner (even if they're a good sport).

### Disclaimer (For Responsible Pranksters)

* Ensure that the `nicks.json` file is in the same directory as the Python code.
* Respect Discord API rate limits when setting the nickname change interval (too fast might get your bot in trouble). 
* Check the logs for any errors that may occur during operation.
* **Most importantly:** Use this bot responsibly and only prank friends who will find it funny.  Avoid anything offensive or hurtful. Good pranks are about laughter, not negativity. 

### Example `nicks.json` file (For Inspiration):

```json
[
  "Sir Stumbles-a-Lot",
  "Queen of the Typo",
  "The Master of Dad Jokes",
  "The Face That Launched a Thousand Memes" 
]
```

This bot provides a lighthearted way to add some fun and playful chaos to your Discord server. Use it wisely, and may the pranks be ever in your favor! 
