import random


async def dicklength(ctx):
    length = random.randrange(1, 50)
    await ctx.channel.send('8' + '=' * length + 'D')
