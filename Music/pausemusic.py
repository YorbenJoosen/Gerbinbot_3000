from SQL import pause


async def pausemusic(ctx):
    serverid = ctx.guild.id
    pausevariable = await pause.read(serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if pausevariable == 1:
                await ctx.send("The music has already been paused.")
            else:
                ctx.voice_client.pause()
                await pause.update(1, serverid)
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
        else:
            await ctx.send(str(ctx.author.name) + " is not in the same channel.")
    else:
        await ctx.send('Bot is not connected to a voice channel')