# Usage 
### 1. Create a new Telegram bot with BotFather.
first you need to create your personal telegram bot token.

1. Start a new conversation with the [BotFather](https://telegram.me/botfather).

2. Send `/newbot` to create a new Telegram bot.

3. When asked, enter a name for the bot.

4. Give the Telegram bot a unique username. Note that the bot name must end with the word "bot" (case-insensitive).

5. Copy and save the Telegram bot's access token for later steps.


### 1. Clone the repositories.
```bash
$ git clone https://github.com/RecycleAI/RecycleIT-C.git
```

### 2. change bot.py token.
Now put your personal token in this line of bot.py code.
```bash
  ACCESS_TOKEN = "**********************"  # your bot token
```

### 3. Run bot.py.

```bash
$ cd ./RecycleIT-C/src/tools/Telegram_bot
$ python bot.py
```
