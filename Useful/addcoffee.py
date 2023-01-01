from SQL import coffee


async def addcoffee(ctx, coffeestring, amount, user, type):
    coffeelist = await coffee.read()
    serverid = ctx.guild.id
    if type == 'normal':
        await ctx.message.delete()
        amount = koffiestring.split('<')[0]
        if amount == '':
            await ctx.send("You forgot to mention the amount")
        else:
            amount = int(amount)
            user = coffeestring.split('<')[1]
            userid = user.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
            i = 0
            while i < len(coffeelist):
                if int(userid) == coffeelist[i]["userid"] and int(serverid) == coffeelist[i]["serverid"]:
                    amount += coffeelist[i]["score"]
                    await coffee.update(int(userid), amount, serverid)
                    i = len(coffeelist)
                elif i == len(coffeelist) - 1:
                    await coffee.write(int(userid), amount, serverid)
                    i += 1
                else:
                    i += 1
    elif type == 'slash':
        userid = user.id
        i = 0
        if len(coffeelist == 0):
            await coffee.write(int(userid), amount, serverid)
        while i < len(coffeelist):
            if int(userid) == coffeelist[i]["userid"] and int(serverid) == coffeelist[i]["serverid"]:
                amount += coffeelist[i]["score"]
                await coffee.update(int(userid), amount, serverid)
                i = len(coffeelist)
            elif i == len(coffeelist) - 1:
                await coffee.write(int(userid), amount, serverid)
                i += 1
            else:
                i += 1
        await ctx.respond('Added the amount.')
