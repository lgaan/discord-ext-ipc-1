from discord.ext import commands, ipc


class IpcRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ipc.Server.listener()
    async def get_member_count(self, guild_id):
        guild = self.bot.get_guild(
            guild_id
        )  # get the guild object using parsed guild_id

        return guild.member_count  # return the member count to the client


def setup(bot):
    bot.ipc.add_cog(IpcRoutes(bot))  # Add the cog using the bot.ipc.add_cog method.
