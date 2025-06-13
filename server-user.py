from disnake.ext import commands


class ServerUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Info about server")
    async def server(self, inter):
        await inter.response.send_message(f"Название сервера: {inter.guild.name}\nВсего участников: {inter.guild.member_count}")


    @commands.slash_command(description="Info about user")
    async def user(self, inter):
        await inter.response.send_message(f"Ваш тег: {inter.author}\nВаш ID: {inter.author.id}")


def setup(bot):
    bot.add_cog(ServerUser(bot))