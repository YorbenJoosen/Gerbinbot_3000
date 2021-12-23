import random


async def gayrate(ctx):
    rating = random.randrange(0, 100)
    await ctx.channel.send('You are ' + str(rating) + '% gay.')
