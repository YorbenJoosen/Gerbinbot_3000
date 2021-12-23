from SQL import musicqueue


async def clearqueue(ctx):
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            await musicqueue.empty(ctx.guild.id)
            await ctx.send("Queue has been cleared")
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
        else:
            await ctx.send(str(ctx.author.name) + " is not in the same channel.")
    else:
        await ctx.send('Bot is not connected to a voice channel')
