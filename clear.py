from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Clear messages")
    async def clear(self, inter, amount: int):
        await inter.response.send_message(f"Удаленно {amount} сообщений.")
        await inter.channel.purge(limit=amount + 1)


def setup(bot):
    bot.add_cog(Clear(bot))
