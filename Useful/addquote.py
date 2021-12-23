from SQL import quotes


async def addquote(ctx, quotestring):
    await ctx.message.delete()
    quote = quotestring.split('<')[0]
    user = quotestring.split('<')[1]
    userid = user.replace('<', '')
    userid = userid.replace('@!', '')
    userid = userid.replace('>', '')
    serverid = ctx.guild.id
    await quotes.write(quote, int(userid), serverid)
