import disnake
from disnake.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Info about server")
    async def information(self, inter):
        embed = disnake.Embed(title="Information", description="About", color=0xfface1)
        embed.add_field(name="Server Name", value=inter.guild.name, inline=False)
        embed.add_field(name="Count Members", value=inter.guild.member_count, inline=False)
        embed.add_field(name="User Tag", value=inter.author, inline=False)
        embed.add_field(name="User ID", value=inter.author.id, inline=False)
        embed.set_footer(text="by: skyxgods")
        embed.set_author(name="skyxgods")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url=self.bot.user.avatar.url)
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Embed(bot))
