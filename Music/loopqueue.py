from SQL import loops


async def loopqueue(ctx):
    serverid = ctx.guild.id
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if song == 0 and queue == 0:
                await loops.update("queue", 1, serverid)
                await ctx.send('Queue has been looped.')
            elif song == 1 and queue == 0:
                await loops.update("queue", 1, serverid)
                await loops.update("song", 0, serverid)
                await ctx.send('Queue has been looped and the song has been unlooped.')
            else:
                await loops.update("queue", 0, serverid)
                await ctx.send('Queue has been unlooped.')
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
        else:
            await ctx.send(str(ctx.author.name) + " is not in the same channel.")
    else:
        await ctx.send('Bot is not connected to a voice channel')
