import random


async def simprate(ctx, type, user, bot):
    rating = random.randrange(0, 100)
    if user:
        if type == 'normal':
            userid = user.split('<')[1]
            userid = userid.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
            user = bot.get_user(int(userid))
            await ctx.reply(user.display_name + ' is ' + str(rating) + '% simp.')
        elif type == 'slash':
            await ctx.respond(user.display_name + ' is ' + str(rating) + '% simp.')
    else:
        if type == 'normal':
            await ctx.reply('You are ' + str(rating) + '% simp.')
        elif type == 'slash':
            await ctx.respond('You are ' + str(rating) + '% simp.')
