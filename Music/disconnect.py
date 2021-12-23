import discord
import audioread
import asyncio
import config_file
from Music import playvideo
from SQL import musicqueue, loops, pause, skipped, disconnected


async def disconnect(ctx):
    serverid = ctx.guild.id
    voice_state = ctx.author.voice
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
            ctx.voice_client.play(discord.FFmpegPCMAudio(source=config_file.doei_druif_path))
            with audioread.audio_open(config_file.doei_druif_path) as f:
                await asyncio.sleep(f.duration)
            await ctx.voice_client.disconnect()
            await disconnected.update(0, serverid)
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
        else:
            await ctx.send(str(ctx.author.name) + " is not in the same channel.")
    else:
        await ctx.send('Bot is not connected to a voice channel')
