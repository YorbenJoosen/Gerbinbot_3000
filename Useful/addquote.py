from SQL import quotes


async def addquote(ctx, quotestring, quote, user, type):
    if type == 'normal':
        await ctx.message.delete()
        quote = quotestring.split('<')[0]
        user = quotestring.split('<')[1]
        userid = user.replace('<', '')
        userid = userid.replace('@!', '')
        userid = userid.replace('>', '')
        serverid = ctx.guild.id
        await quotes.write(quote, int(userid), serverid)
    elif type == 'slash':
        serverid = ctx.guild.id
        await quotes.write(quote, int(user.id), serverid)
        await ctx.respond('Quote has been added.')
