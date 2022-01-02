import discord
from SQL import camera


async def leaderboardcamera(ctx, user):
    cameralist = await camera.read()
    string = ''
    cameralist = sorted(cameralist, key=lambda i: i['score'], reverse=True)
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
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in cameralist):
            while iterator < len(cameralist):
                if cameralist[iterator]['userid'] == int(userid) and cameralist[iterator]['serverid'] == ctx.guild.id:
                    await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(cameralist[iterator]['score']))
                    iterator = len(cameralist)
                elif cameralist[iterator]['serverid'] != ctx.guild.id:
                    del cameralist[iterator]
                else:
                    iterator += 1
        else:
            await ctx.send(membername + " isn't on the camera leaderboard yet.")
    else:
        while iterator < len(cameralist):
            if cameralist[iterator]["serverid"] == ctx.guild.id:
                iterator += 1
            else:
                del cameralist[iterator]
        if len(cameralist) < 10:
            length = len(cameralist)
        for i in range(0, length):
            for member in members:
                if member.id == cameralist[i]["userid"]:
                    membername = member.display_name
            string += str(i+1) + ") " + membername + ": " + str(cameralist[i]["score"]) + "\n"
        embed = discord.Embed(title='Camera leaderboard', color=discord.Color.green(), description=string)
        await ctx.send(embed=embed)
