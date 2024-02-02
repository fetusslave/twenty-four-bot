import discord
from discord.ext import commands
from discord import app_commands
from twenty_four_points import solver
from twenty_four_points.helpers import get_ranking_string


class GameCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.games = {}

    @app_commands.command(name="start", description="start new game")
    async def start(self, interaction):
        if self.games.get(interaction.guild_id):
            await interaction.response.send_message("there is an ongoing game")
        else:
            game = solver.Game()
            game.start()
            self.games.update({interaction.guild_id: game})
            await interaction.response.send_message("start")
            await self.question(interaction)

    async def question(self, interaction):
        game = self.games[interaction.guild_id]
        # send the question
        await interaction.channel.send(game.question.__str__())
        solved = False
        # keep checking until question has been solved
        while not solved and game.is_ongoing():
            solution = await self.client.wait_for("message")
            if solution.author.bot:
                continue
            if game.check_solution(solution.content, solution.author):
                await interaction.channel.send(solution.author)
                solved = True
                game.new_question()
                await self.question(interaction)

    @app_commands.command(name="stop", description="stop the current game")
    async def stop(self, interaction):
        guild_id = interaction.guild_id
        game = self.games.get(guild_id)
        if game:
            game.stop()
            players = game.get_ranking()
            await interaction.response.send_message("game ended\n" + get_ranking_string(players))
            del self.games[guild_id]
        else:
            await interaction.response.send_message("there is no ongoing game")

    @app_commands.command(name="list", description="list all solutions")
    async def list(self, interaction):
        game = self.games.get(interaction.guild_id)
        if not game:
            await interaction.response.send_message("there is no ongoing game")
            return
        solutions = game.question.solve()
        message = ""
        for i in solutions:
            message += i.replace("*", "x").__str__() + "\n"
        if message == "":
            await interaction.response.send_message("no solutions")
        else:
            await interaction.response.send_message(message[:2000])

    @app_commands.command(name="ranking", description="view rankings")
    async def ranking(self, interaction):
        game = self.games.get(interaction.guild_id)
        if not game:
            await interaction.response.send_message("there is no ongoing game")
            return
        players = game.get_ranking()
        await interaction.response.send_message(get_ranking_string(players))


async def setup(client: commands.Bot) -> None:
    await client.add_cog(GameCog(client))
