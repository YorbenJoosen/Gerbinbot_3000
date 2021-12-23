import random


async def vaginawidth(ctx):
    width = random.randrange(0, 50, 2)
    message = "{(" + " " * int((width / 2)) + "." + " " * int((width / 2)) + ")}"
    await ctx.channel.send(message)
    if width > 40:
        await ctx.channel.send("Jeeeezus how many dicks have you had?")
