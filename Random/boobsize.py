import random


async def boobsize(ctx, type, user, bot):
    number = random.choice([60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
    letter = random.choice(["AA", "A", "B", "C", "D", "E", "F", "G", "H"])
    boobsize = str(number) + letter
    if user:
        if type == 'normal':
            userid = user.split('<')[1]
            userid = userid.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
            user = bot.get_user(int(userid))
            await ctx.reply(user.display_name + ' boobsize: ' + boobsize)
        elif type == 'slash':
            await ctx.respond(user.display_name + ' boobsize: ' + boobsize)
    else:
        if type == 'normal':
            await ctx.reply(boobsize)
        elif type == 'slash':
            await ctx.respond(boobsize)