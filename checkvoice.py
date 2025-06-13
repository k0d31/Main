import disnake
from disnake.ext import commands

class CheckVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="voice", description="Check in voice")
    async def checkvoice(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        voice = member.voice
        if voice is not None:
            await inter.response.send_message(f"{member.mention} в голосовом канале {voice.channel.mention}", ephemeral=True, delete_after=5)
        else:
            await inter.response.send_message(f"{member.mention} не в голосовом канале!", ephemeral=True, delete_after=5)


def setup(bot):
    bot.add_cog(CheckVoice(bot))
