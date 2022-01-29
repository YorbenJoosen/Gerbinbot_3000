from SQL import musicqueue


async def queue(ctx, type):
    musiclist = await musicqueue.read(ctx.guild.id)
    string = ""
    iterator = 0
    if len(musiclist) == 0:
        if type == 'normal':
            await ctx.reply("There are no songs queued currently.")
        elif type == 'slash':
            await ctx.respond("There are no songs queued currently.")
    else:
        while iterator < len(musiclist):
            if len(string) >= 2000:
                string = string.replace(str(iterator) + ") " + musiclist[iterator - 1]["title"] + " " + musiclist[iterator - 1]["duration"], "")
                break
            else:
                string += str(iterator + 1) + ") " + musiclist[iterator]["title"] + " " + musiclist[iterator]["duration"] + "\n"
                iterator += 1
        if type == 'normal':
            await ctx.reply(string)
        elif type == 'slash':
            await ctx.respond(string)
