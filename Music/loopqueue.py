from SQL import loops


async def loopqueue(ctx, type):
    serverid = ctx.guild.id
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if song == 0 and queue == 0:
                await loops.update("queue", 1, serverid)
                if type == 'normal':
                    await ctx.reply('Queue has been looped.')
                elif type == 'slash':
                    await ctx.respond('Queue has been looped.')
            elif song == 1 and queue == 0:
                await loops.update("queue", 1, serverid)
                await loops.update("song", 0, serverid)
                if type == 'normal':
                    await ctx.reply('Queue has been looped and the song has been unlooped.')
                elif type == 'slash':
                    await ctx.respond('Queue has been looped and the song has been unlooped.')
            else:
                await loops.update("queue", 0, serverid)
                if type == 'normal':
                    await ctx.reply('Queue has been unlooped.')
                elif type == 'slash':
                    await ctx.respond('Queue has been unlooped.')
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
