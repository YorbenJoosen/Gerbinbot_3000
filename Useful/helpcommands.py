import discord
import config_file


async def helpcommands(ctx):
    embed = discord.Embed(title='Available commands', color=discord.Color.green())
    embed.set_author(name='Ouzen#0299', url='https://github.com/XThexLonexWolfX', icon_url=config_file.help_picture)
    embed.add_field(name='Music commands', value=config_file.help_music, inline=False)
    embed.add_field(name='Useful commands', value=config_file.help_useful, inline=False)
    embed.add_field(name='Random commands', value=config_file.help_random, inline=False)
    embed.add_field(name='Admin commands', value=config_file.help_admin, inline=False)
    embed.set_footer(text='This bot was made by Ouzen#2099 also known as XThexLonexWolfX or Yorben Joosen')
    await ctx.send(embed=embed)
