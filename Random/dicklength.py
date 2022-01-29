import random


async def dicklength(ctx, type, user, bot):
    length = random.randrange(1, 50)
    if user:
        if type == 'normal':
            userid = user.split('<')[1]
            userid = userid.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
            user = bot.get_user(int(userid))
            await ctx.reply(user.display_name + ' dick: 8' + '=' * length + 'D')
        elif type == 'slash':
            await ctx.respond(user.display_name + ' dick: 8' + '=' * length + 'D')
    else:
        if type == 'normal':
            await ctx.reply('8' + '=' * length + 'D')
        elif type == 'slash':
            await ctx.respond('8' + '=' * length + 'D')
