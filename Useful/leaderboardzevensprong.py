import discord
from SQL import zevensprong


async def leaderboardzevensprong(ctx, user, bot):
    zevenspronglist = await zevensprong.read()
    string = ''
    zevenspronglist = sorted(zevenspronglist, key=lambda i: i['score'], reverse=True)
    iterator = 0
    length = 10
    membername = ""
    members = bot.get_all_members()
    if user:
        userid = user.split('<')[1]
        userid = userid.replace('<', '')
        userid = userid.replace('@!', '')
        userid = userid.replace('>', '')
        for member in members:
            if member.id == int(userid):
                membername = member.name
                break
        if any(d['userid'] == int(userid)for d in zevenspronglist):
            while iterator < len(zevenspronglist):
                if zevenspronglist[iterator]['userid'] == int(userid):
                    await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(zevenspronglist[iterator]['score']))
                    iterator = len(zevenspronglist)
                else:
                    iterator += 1
        else:
            await ctx.send(membername + " isn't on the zevensprong leaderboard yet.")
    else:
        string += 7*":beer:" + "\n"
        if len(zevenspronglist) < 10:
            length = len(zevenspronglist)
        for i in range(0, length):
            for member in members:
                if member.id == zevenspronglist[i]["userid"]:
                    membername = member.name
                    break
            string += str(i+1) + ") " + membername + ": " + str(zevenspronglist[i]["score"]) + "\n"
        embed = discord.Embed(title='Zevensprong leaderboard', color=discord.Color.green(), description=string)
        await ctx.send(embed=embed)
