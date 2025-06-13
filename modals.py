import disnake
from disnake.ext import commands
from disnake import TextInputStyle, ModalInteraction, ApplicationCommandInteraction


class MyModal(disnake.ui.Modal):
    def __init__(self):
        self.fields = {
            "название": "Name",
            "описание": "Description"
        }

        components = [
            disnake.ui.TextInput(
                label=self.fields["название"],
                placeholder="Foo Tag",
                custom_id="название",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label=self.fields["описание"],
                placeholder="Lorem ipsum dolor sit amet",
                custom_id="описание",
                style=TextInputStyle.paragraph,
            ),
        ]

        super().__init__(
            title="Report",
            custom_id="create_tag",
            components=components,
        )

    async def callback(self, inter: ModalInteraction):
        embed = disnake.Embed(title="Report", color=disnake.Color.red())
        for key, value in inter.text_values.items():
            label = self.fields.get(key, key).capitalize()
            embed.add_field(name=label, value=value[:1024], inline=False)

        await inter.response.send_message(embed=embed)


class TagModalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="report", description="Create a report")
    async def tags(self, inter: ApplicationCommandInteraction):
        await inter.response.send_modal(modal=MyModal())


def setup(bot):
    bot.add_cog(TagModalCog(bot))
