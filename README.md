# 24 points Discord bot
## 24 points rules
Given 4 numbers ranging from 1 to 12, try to find a solution that evaluates to 24 which uses each number exactly once, and any basic operations `+-*/`.
<br>
All questions generated by the bot are solvable.
## Commands
- `/start`: Starts a new game if there isn't one already ongoing. A new question is generated automatically after the current question is solved. The first user to solve a question gets 1 point.
- `/stop`: Stops the currently ongoing game.
- `/list`: Shows a list of possible solutions for the current question.
- `/ranking`: Shows the ranking of each user who participated in the game.
- To answer a question, simply type your answer as a mathematical expression into the channel e.g. `9*2+(12-6)`. Only valid expressions containing `(0-9, +-*/, ())` will be accepted.
