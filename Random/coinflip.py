import random


async def coinflip(ctx):
    waarde = random.randint(1, 101)
    if 1 <= waarde < 50:
        await ctx.channel.send('Heads')
    elif 50 <= waarde < 101:
        await ctx.channel.send('Tails')
    else:
        await ctx.channel.send('Side' + "\n" + "Daaamn you're one flipping lucky bastard! (See my pun there, hehe bots rule)")



