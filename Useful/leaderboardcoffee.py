import discord
from SQL import coffee


async def leaderboardcoffee(ctx, user, bot, type):
    coffeelist = await coffee.read()
    string = ''
    coffeelist = sorted(coffeelist, key=lambda i: i['score'], reverse=True)
    iterator = 0
    length = 10
    membername = ""
    members = ctx.guild.members
    serverid = ctx.guild.id
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
                membername = member.name
                break
        if any(d['userid'] == int(userid) and d['serverid'] == serverid for d in coffeelist):
            while iterator < len(coffeelist):
                if coffeelist[iterator]['userid'] == int(userid) and coffeelist[iterator]['serverid'] == serverid:
                    if type == 'normal':
                        await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(coffeelist[iterator]['score']))
                    elif type == 'slash':
                        await ctx.respond(str(iterator + 1) + ") " + membername + ': ' + str(coffeelist[iterator]['score']))
                    iterator = len(coffeelist)
                elif coffeelist[iterator]['serverid'] != serverid:
                    del coffeelist[iterator]
                else:
                    iterator += 1
        else:
            if type == 'normal':
                await ctx.send(membername + " isn't on the coffee leaderboard yet.")
            elif type == 'slash':
                await ctx.respond(membername + " isn't on the coffee leaderboard yet.")
    else:
        while iterator < len(coffeelist):
            if coffeelist[iterator]["serverid"] == serverid:
                iterator += 1
            else:
                del coffeelist[iterator]
        if len(coffeelist) < 10:
            length = len(coffeelist)
        for i in range(0, length):
            for member in members:
                if member.id == coffeelist[i]["userid"]:
                    membername = member.display_name
            string += str(i + 1) + ") " + membername + ": " + str(coffeelist[i]["score"]) + "\n"
        embed = discord.Embed(title='Coffee leaderboard', color=discord.Color.green(), description=string)
        if type == 'normal':
            await ctx.send(embed=embed)
        elif type == 'slash':
            await ctx.respond(embed=embed)
