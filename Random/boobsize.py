import random


async def boobsize(ctx):
    number = random.choice([60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
    letter = random.choice(["AA", "A", "B", "C", "D", "E", "F", "G", "H"])
    boobsize = str(number) + letter
    await ctx.channel.send(boobsize)
