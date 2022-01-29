import random


async def vaginawidth(ctx, type, user, bot):
    width = random.randrange(0, 50, 2)
    message = "{(" + " " * int((width / 2)) + "." + " " * int((width / 2)) + ")}"
    if user:
        if type == 'normal':
            userid = user.split('<')[1]
            userid = userid.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
            user = bot.get_user(int(userid))
            await ctx.reply(user.display_name + ' vagina: ' + message)
        elif type == 'slash':
            await ctx.respond(user.display_name + ' vagina: ' + message)
    else:
        if type == 'normal':
            await ctx.reply(message)
        elif type == 'slash':
            await ctx.respond(message)
    if width > 40:
        if type == 'normal':
            await ctx.reply("Jeeeezus how many dicks have you had?")
        if type == 'slash':
            await ctx.respond("Jeeeezus how many dicks have you had?")
