# 24 points Discord bot
Built using [discord.py](https://github.com/Rapptz/discord.py) library.
## 24 points rules
Given 4 numbers ranging from 1 to 12, try to find a solution that evaluates to 24 which uses each number exactly once, and any basic operations `+-*/`.
<br>
All questions generated by the bot are solvable.
## Commands
- `/start`: Starts a new game if there isn't one already ongoing. A new question is generated automatically after the current question is solved. The first user to solve a question gets 1 point.
- `/stop`: Stops the currently ongoing game.
- `/list`: Shows a list of possible solutions for the current question.
- `/ranking`: Shows the ranking of each user who participated in the game.
- To answer a question, simply type your answer as a mathematical expression into the channel e.g. `9*2+(12-6)`. Only valid expressions containing `0-9, +-*/, ()` will be accepted.
## Running locally
- Create a new Discord application at the Discord [Developer portal](https://discord.com/developers/).
- Invite the bot to your Discord server.
- Clone the repository
  ```
  git clone https://github.com/fetusslave/twenty_four_bot.git
  ```
- Install dependencies
  ```
  pip3 install -r requirements.txt
  ```
- Create a `.env` file in the project root directory with your Discord bot token and server ID
  ```
  GUILD_ID=your_server_id
  DISCORD_TOKEN=your_bots_discord_token
  ```
- Run the bot
  ```
  python3 main.py
  ```
