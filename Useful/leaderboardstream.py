import discord
from SQL import stream


async def leaderboardstream(ctx, user):
    streamlist = await stream.read()
    string = ''
    streamlist = sorted(streamlist, key=lambda i: i['score'], reverse=True)
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
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in streamlist):
            while iterator < len(streamlist):
                if streamlist[iterator]['userid'] == int(userid) and streamlist[iterator]['serverid'] == ctx.guild.id:
                    await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(streamlist[iterator]['score']))
                    iterator = len(streamlist)
                elif streamlist[iterator]['serverid'] != ctx.guild.id:
                    del streamlist[iterator]
                else:
                    iterator += 1
        else:
            await ctx.send(membername + " isn't on the streaming leaderboard yet.")
    else:
        while iterator < len(streamlist):
            if streamlist[iterator]["serverid"] == ctx.guild.id:
                iterator += 1
            else:
                del streamlist[iterator]
        if len(streamlist) < 10:
            length = len(streamlist)
        for i in range(0, length):
            for member in members:
                if member.id == streamlist[i]["userid"]:
                    membername = member.display_name
            string += str(i+1) + ") " + membername + ": " + str(streamlist[i]["score"]) + "\n"
        embed = discord.Embed(title='Streaming leaderboard', color=discord.Color.green(), description=string)
        await ctx.send(embed=embed)
