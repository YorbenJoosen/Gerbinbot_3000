from SQL import quotes


async def sendquotes(ctx, user):
    quotelist = await quotes.read()
    string = ''
    members = ctx.guild.members
    iterator = 0
    membername = ""
    if user:
        userid = user.split('<')[1]
        userid = userid.replace('<', '')
        userid = userid.replace('@!', '')
        userid = userid.replace('>', '')
        for member in members:
            if member.id == int(userid):
                membername = member.display_name
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in quotelist):
            await ctx.send("These are the quotes for " + membername + ':')
            while iterator < len(quotelist):
                if len(string) >= 2000:
                    string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"], '')
                    await ctx.send(string)
                    string = ''
                    iterator -= 1
                elif quotelist[iterator]['serverid'] == ctx.guild.id and quotelist[iterator]['userid'] == int(userid):
                    string += str(iterator + 1) + ') ' + quotelist[iterator]["quote"] + '\n'
                    iterator += 1
                else:
                    del quotelist[iterator]
            if string:
                if len(string) >= 2000:
                    string = string.replace(str(iterator - 2) + ') ' + quotelist[iterator - 1]["quote"], '')
                await ctx.send(string)
        else:
            await ctx.send(membername + " Doesn't have any quotes yet.")
    else:
        while iterator < len(quotelist):
            if len(string) >= 2000:
                for member in members:
                    if member.id == quotelist[iterator - 1]["userid"]:
                        membername = member.display_name
                string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"] + " - " + membername, '')
                await ctx.send(string)
                string = ''
                iterator -= 1
            elif quotelist[iterator]['serverid'] == ctx.guild.id:
                for member in members:
                    if member.id == quotelist[iterator]["userid"]:
                        membername = member.display_name
                string += str(iterator + 1) + ') ' + quotelist[iterator]["quote"] + " - " + membername + '\n'
                iterator += 1
            else:
                del quotelist[iterator]
        if len(string) >= 2000:
            for member in members:
                if member.id == quotelist[iterator - 1]["userid"]:
                    membername = member.display_name
            string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"] + " - " + membername, '')
        await ctx.send(string)
