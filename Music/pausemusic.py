from SQL import pause


async def pausemusic(ctx, type):
    serverid = ctx.guild.id
    pausevariable = await pause.read(serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if pausevariable == 1:
                if type == 'normal':
                    await ctx.reply("The music has already been paused.")
                elif type == 'slash':
                    await ctx.respond("The music has already been paused.")
            else:
                ctx.voice_client.pause()
                if type == 'slash':
                    await ctx.respond('Music has been paused.', ephemeral=True)
                await pause.update(1, serverid)
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