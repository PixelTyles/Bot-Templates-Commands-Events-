import discord
from discord.ext import commands
from discord.commands import slash_command

class greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command
    async def greet(self, ctx, member: discord.Member):
        greet = discord.Embed(
            title="greeting",
            description="Member {ctx.author.} welcomed {member.mention}."
        )

def setup(bot):
    bot.add_cog(greet(bot))