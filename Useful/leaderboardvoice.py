import discord
from SQL import voice


async def leaderboardvoice(ctx, user):
    voicelist = await voice.read()
    string = ''
    voicelist = sorted(voicelist, key=lambda i: i['score'], reverse=True)
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
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in voicelist):
            while iterator < len(voicelist):
                if voicelist[iterator]['userid'] == int(userid) and voicelist[iterator]['serverid'] == ctx.guild.id:
                    await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(voicelist[iterator]['score']))
                    iterator = len(voicelist)
                else:
                    iterator += 1
        else:
            await ctx.send(membername + " isn't on the voice leaderboard yet.")
    else:
        while iterator < len(voicelist):
            if voicelist[iterator]["serverid"] == ctx.guild.id:
                iterator += 1
            else:
                del voicelist[iterator]
        if len(voicelist) < 10:
            length = len(voicelist)
        for i in range(0, length):
            for member in members:
                if member.id == voicelist[i]["userid"]:
                    membername = member.display_name
            string += str(i+1) + ") " + membername + ": " + str(voicelist[i]["score"]) + "\n"
        embed = discord.Embed(title='Voice leaderboard', color=discord.Color.green(), description=string)
        await ctx.send(embed=embed)
