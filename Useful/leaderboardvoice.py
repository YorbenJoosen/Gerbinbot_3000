import discord
from SQL import voice


async def leaderboardvoice(ctx, user, type):
    voicelist = await voice.read()
    string = ''
    voicelist = sorted(voicelist, key=lambda i: i['score'], reverse=True)
    iterator = 0
    membername = ""
    members = ctx.guild.members
    length = 10
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
        if any(d['userid'] == int(userid) and d['serverid'] == ctx.guild.id for d in voicelist):
            while iterator < len(voicelist):
                if voicelist[iterator]['userid'] == int(userid) and voicelist[iterator]['serverid'] == ctx.guild.id:
                    if type == 'normal':
                        await ctx.send(str(iterator + 1) + ") " + membername + ': ' + str(voicelist[iterator]['score']))
                    elif type == 'slash':
                        await ctx.respond(str(iterator + 1) + ") " + membername + ': ' + str(voicelist[iterator]['score']))
                    iterator = len(voicelist)
                elif voicelist[iterator]['serverid'] != ctx.guild.id:
                    del voicelist[iterator]
                else:
                    iterator += 1
        else:
            if type == 'normal':
                await ctx.send(membername + " isn't on the voice leaderboard yet.")
            elif type == 'slash':
                await ctx.respond(membername + " isn't on the voice leaderboard yet.")
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
        if type == 'normal':
            await ctx.send(embed=embed)
        elif type == 'slash':
            await ctx.respond(embed=embed)
