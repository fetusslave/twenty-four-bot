import os
import asyncio
from dotenv import load_dotenv
import discord
from discord import app_commands
import solver

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

print(os.getenv("GUILD_ID", None))
print(os.getenv("DISCORD_TOKEN", ""))

guild = discord.Object(id=os.getenv("GUILD_ID", None))

current_question = solver.Question()

game = solver.Game()

@client.event
async def on_ready():
    await tree.sync(guild=guild)
    print("ready")


@tree.command(name="uwu", description="say uwu", guild=guild)
async def uwu(interaction):
    await interaction.response.send_message("uwu")


@tree.command(name="hello", description="say hello", guild=guild)
async def hello(interaction):
    await interaction.response.send_message("hello")


@tree.command(name="start", description="start new game", guild=guild)
async def start(interaction):
    global game
    if game.is_ongoing():
        await interaction.response.send_message("there is an ongoing game")
    else:
        game = solver.Game()
        game.start()
        await interaction.response.send_message("start")
        await question(interaction)


async def question(interaction):
    global game
    await interaction.channel.send(game.question.__str__())
    solved = False
    while not solved and game.is_ongoing():
        solution = await client.wait_for("message")
        if solution.author.bot:
            continue
        if game.check_solution(solution.content, solution.author):
            print(solution)
            await interaction.channel.send(solution.author)
            solved = True
            game.new_question()
            await question(interaction)


@tree.command(name="stop", description="stop the current game", guild=guild)
async def stop(interaction):
    global game
    if not game.is_ongoing():
        await interaction.response.send_message("there is no ongoing game")
        return
    else:
        game.stop()
        players = game.get_ranking()
        await interaction.response.send_message("game ended\n"+get_ranking_string(players))


@tree.command(name="list", description="list all solutions", guild=guild)
async def list(interaction):
    global game
    if not game.is_ongoing():
        await interaction.response.send_message("there is no ongoing game")
        return
    solutions = game.question.solve()
    message = ""
    for i in solutions:
        message += i.replace("*", "x").__str__()+"\n"
    if message == "":
        await interaction.response.send_message("no solutions")
    else:
        await interaction.response.send_message(message[:2000])


@tree.command(name="ranking", description="view rankings", guild=guild)
async def ranking(interaction):
    global game
    if not game.is_ongoing():
        await interaction.response.send_message("there is no ongoing game")
        return
    players = game.get_ranking()
    await interaction.response.send_message(get_ranking_string(players))


def get_ranking_string(players):
    message = ""
    for i in range(len(players)):
        message += f"{i + 1}. {players[i][0]}\t{players[i][1]}\n"
    return message


asyncio.run(client.run(os.getenv("DISCORD_TOKEN", "")))

