from disnake.ext import commands
import disnake


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Ban user")
    async def ban(self, inter, user: disnake.User, *, reason=None):
        await inter.guild.ban(user, reason=reason)
        await inter.response.send_message(f"Забанен {user.mention}", ephemeral=True)


    @commands.slash_command(description="Unban user")
    async def unban(self, inter, user: disnake.User):
        await inter.guild.unban(user)
        await inter.response.send_message(f"Разбанен {user.mention}", ephemeral=True)


def setup(bot):
    bot.add_cog(Ban(bot))
