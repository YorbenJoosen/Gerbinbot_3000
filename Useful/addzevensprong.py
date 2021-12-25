from SQL import zevensprong


async def addzevensprong(ctx, zevensprongstring):
    await ctx.message.delete()
    zevenspronglist = await zevensprong.read()
    amount = zevensprongstring.split('<')[0]
    if amount == '':
        await ctx.send("You forgot to mention the amount")
    else:
        amount = int(amount)
        user = zevensprongstring.split('<')[1]
        userid = user.replace('<', '')
        userid = userid.replace('@!', '')
        userid = userid.replace('>', '')
        i = 0
        while i < len(zevenspronglist):
            if int(userid) == zevenspronglist[i]["userid"]:
                amount += zevenspronglist[i]["score"]
                await zevensprong.update(int(userid), amount)
                i = len(zevenspronglist)
            elif i == len(zevenspronglist) - 1:
                await zevensprong.write(int(userid), amount)
                i += 1
            else:
                i += 1
