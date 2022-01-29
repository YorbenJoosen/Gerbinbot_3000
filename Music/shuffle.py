import random

from SQL import musicqueue, loops, skipped
from Music import playvideo


async def shuffle(ctx, type):
    serverid = ctx.guild.id
    voice_state = ctx.author.voice
    replacement = []
    musiclist = await musicqueue.read(serverid)
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    length = len(musiclist)
    if len(musiclist) > 1:
        number = random.randrange(0, (len(musiclist) - 1))
    else:
        number = 0
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if queue == 1:
                if type == 'normal':
                    await ctx.reply("You can't shuffle when the queue is looped.")
                elif type == 'slash':
                    await ctx.respond("You can't shuffle when the queue is looped.")
            elif song == 1:
                if type == 'normal':
                    await ctx.reply("You can't shuffle when a song is looped.")
                elif type == 'slash':
                    await ctx.respond("You can't shuffle when a song is looped.")
            else:
                ctx.voice_client.stop()
                for i in range(length):
                    replacement.append({"url": musiclist[number]["url"], "title": musiclist[number]["title"], "duration": musiclist[number]["duration"], "time": musiclist[number]["time"]})
                    del musiclist[number]
                    if length > 1:
                        length -= 1
                        number = random.randrange(0, length)
                    else:
                        number = 0
                await musicqueue.empty(serverid)
                for i in range(len(replacement)):
                    await musicqueue.write(replacement[i]["url"], replacement[i]["title"], replacement[i]["duration"], serverid)
                if type == 'normal':
                    await ctx.reply('Queue has been shuffled.')
                elif type == 'slash':
                    await ctx.respond('Queue has been shuffled.')
                await skipped.update(1, serverid)
                await playvideo.playvideo(ctx)
        elif voice_state is None:
            if type == 'normal':
                await ctx.reply(str(ctx.author.name) + " is not in a channel.")
            elif type == 'slash':
                await ctx.respond(str(ctx.author.name) + " is not in a channel.")
        else:
            if type == 'normal':
                await ctx.reply(str(ctx.author.name) + " is not in the same channel.")
            elif type == 'slash':
                await ctx.respond(str(ctx.author.name) + " is not in the same channel.")
    else:
        if type == 'normal':
            await ctx.reply('Bot is not connected to a voice channel')
        elif type == 'slash':
            await ctx.respond('Bot is not connected to a voice channel')