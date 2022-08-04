import asyncio

import discord
connections = {}
sleeptask = 0


async def sleepasyncio(length, vc):
    await asyncio.sleep(length)
    vc.stop_recording()


async def finished_callback(sink, channel: discord.TextChannel, *args):
    recorded_users = [f"<@{user_id}>" for user_id, audio in sink.audio_data.items()]
    await sink.vc.disconnect()
    files = [
        discord.File(audio.file, f"{user_id}.{sink.encoding}")
        for user_id, audio in sink.audio_data.items()
    ]
    await channel.send(
        f"Finished! Recorded audio for {', '.join(recorded_users)}.", files=files
    )


async def record(ctx, option, type):
    voice = ctx.author.voice
    global sleeptask
    if voice:
        if option == "start":
            if ctx.voice_client is None:
                vc = await voice.channel.connect()
                connections.update({ctx.guild.id: vc})
                vc.start_recording(discord.sinks.MP3Sink(), finished_callback, ctx.channel)
                sleeptask = asyncio.create_task(sleepasyncio(300, vc))
                try:
                    await sleeptask
                except asyncio.CancelledError:
                    pass
                if type == 'slash':
                    await ctx.respond("Bot is recording.", ephemeral=True)
                else:
                    await ctx.reply("Bot started recording")
            elif ctx.author.voice.channel == ctx.voice_client.channel:
                if type == 'normal':
                    await ctx.reply('Bot is already playing something else.')
                elif type == 'slash':
                    await ctx.respond('Bot is already playing something else.')
            else:
                if type == 'normal':
                    await ctx.reply('Bot is already in another channel.')
                elif type == 'slash':
                    await ctx.respond('Bot is already in another channel.')
        elif option == "stop":
            if ctx.guild.id in connections:
                vc = connections[ctx.guild.id]
                sleeptask.cancel()
                vc.stop_recording()
                del connections[ctx.guild.id]
                if type == "slash":
                    await ctx.respond("Bot stopped recording", ephemeral=True)
                else:
                    await ctx.reply("Bot stopped recording")
            else:
                if type == "slash":
                    await ctx.respond("Not recording in this server", ephemeral=True)
                else:
                    await ctx.reply("Not recording in this server")
    else:
        if type == 'normal':
            await ctx.reply(str(ctx.author.name) + " is not in a channel.")
        elif type == 'slash':
            await ctx.respond(str(ctx.author.name) + " is not in a channel.")
