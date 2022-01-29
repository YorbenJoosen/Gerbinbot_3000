import discord
import audioread
import asyncio
import config_file
from Music import playvideo
from SQL import musicqueue, loops, pause, skipped, disconnected, turnonoff


async def disconnect(ctx, type):
    serverid = ctx.guild.id
    voice_state = ctx.author.voice
    doeidruif = await turnonoff.read(serverid, 'doeidruif')
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            await skipped.update(0, serverid)
            ctx.voice_client.stop()
            await musicqueue.empty(serverid)
            await loops.update("queue", 0, serverid)
            await loops.update("song", 0, serverid)
            await pause.update(0, serverid)
            await disconnected.update(1, serverid)
            playvideo.sleeptask.cancel()
            if doeidruif == 1:
                ctx.voice_client.play(discord.FFmpegPCMAudio(source=config_file.doei_druif_path))
                with audioread.audio_open(config_file.doei_druif_path) as f:
                    await asyncio.sleep(f.duration)
            await ctx.voice_client.disconnect()
            if type == 'slash':
                await ctx.respond('Bopt has been disconnected', ephemeral=True)
            await disconnected.update(0, serverid)
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
