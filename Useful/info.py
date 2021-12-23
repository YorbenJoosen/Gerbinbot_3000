import discord
import config_file

async def info(ctx):
    await ctx.message.delete()
    await ctx.channel.send(file=discord.File(config_file.rickroll_path), delete_after=5)
