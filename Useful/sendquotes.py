import discord

from SQL import quotes


async def sendquotes(ctx, user, type):
    quotelist = await quotes.read()
    string = ''
    members = ctx.guild.members
    iterator = 0
    membername = ""
    if user:
        userid = 0
        if type == 'normal':
            userid = user.split('<')[1]
            userid = userid.replace('<', '')
            userid = userid.replace('@!', '')
            userid = userid.replace('>', '')
        elif type == 'slash':
            userid = user.id
        for member in members:
            if member.id == int(userid):
                membername = member.display_name
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in quotelist):
            while iterator < len(quotelist):
                if len(string) >= 2000:
                    string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"], '')
                    embed = discord.Embed(title=membername + 'quotes', color=discord.Color.green(), description=string)
                    if type == 'normal':
                        await ctx.send(embed=embed)
                    elif type == 'slash':
                        await ctx.respond(embed=embed)
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
                embed = discord.Embed(title=membername + ' quotes', color=discord.Color.green(), description=string)
                if type == 'normal':
                    await ctx.send(embed=embed)
                elif type == 'slash':
                    await ctx.respond(embed=embed)
        else:
            await ctx.send(membername + " Doesn't have any quotes yet.")
    else:
        while iterator < len(quotelist):
            if len(string) >= 4096:
                for member in members:
                    if member.id == quotelist[iterator - 1]["userid"]:
                        membername = member.display_name
                string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"] + " - " + membername, '')
                embed = discord.Embed(title='All quotes', color=discord.Color.green(), description=string)
                if type == 'normal':
                    await ctx.send(embed=embed)
                elif type == 'slash':
                    await ctx.respond(embed=embed)
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
        if len(string) >= 4096:
            for member in members:
                if member.id == quotelist[iterator - 1]["userid"]:
                    membername = member.display_name
            string = string.replace(str(iterator) + ') ' + quotelist[iterator - 1]["quote"] + " - " + membername, '')
        embed = discord.Embed(title='All quotes', color=discord.Color.green(), description=string)
        if type == 'normal':
            await ctx.send(embed=embed)
        elif type == 'slash':
            await ctx.respond(embed=embed)
