import random


async def coinflip(ctx, type):
    waarde = random.randint(1, 101)
    if 1 <= waarde < 50:
        if type == 'normal':
            await ctx.reply('Heads')
        elif type == 'slash':
            await ctx.respond('Heads')
    elif 50 <= waarde < 101:
        if type == 'normal':
            await ctx.reply('Tails')
        elif type == 'slash':
            await ctx.respond('Tails')
    else:
        if type == 'normal':
            await ctx.reply('Side' + "\n" + "Daaamn you're one flipping lucky bastard! (See my pun there, hehe bots rule)")
        elif type == 'slash':
            await ctx.respond('Side' + "\n" + "Daaamn you're one flipping lucky bastard! (See my pun there, hehe bots rule)")



