import discord
from SQL import text


async def leaderboardtext(ctx, user):
    textlist = await text.read()
    string = ''
    textlist = sorted(textlist, key=lambda i: i['score'], reverse=True)
    iterator = 0
    membername = ""
    members = ctx.guild.members
    length = 10
    if user:
        userid = user.split('<')[1]
        userid = userid.replace('<', '')
        userid = userid.replace('@!', '')
        userid = userid.replace('>', '')
        for member in members:
            if member.id == int(userid):
                membername = member.display_name
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in textlist):
            while iterator < len(textlist):
                if textlist[iterator]['userid'] == int(userid) and textlist[iterator]['serverid'] == ctx.guild.id:
                    await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(textlist[iterator]['score']))
                    iterator = len(textlist)
                else:
                    iterator += 1
        else:
            await ctx.send(membername + " isn't on the text leaderboard yet.")
    else:
        while iterator < len(textlist):
            if textlist[iterator]["serverid"] == ctx.guild.id:
                iterator += 1
            else:
                del textlist[iterator]
        if len(textlist) < 10:
            length = len(textlist)
        for i in range(0, length):
            for member in members:
                if member.id == textlist[i]["userid"]:
                    membername = member.display_name
            string += str(i+1) + ") " + membername + ": " + str(textlist[i]["score"]) + "\n"
        embed = discord.Embed(title='Text leaderboard', color=discord.Color.green(), description=string)
        await ctx.send(embed=embed)
