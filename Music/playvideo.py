import asyncio
import audioread
import discord
import youtube_dl
import yt_dlp

import config_file
from SQL import musicqueue, loops, skipped, disconnected, turnonoff

ytdl_format_options = {
    'format': 'bestaudio/best',  # Get best audio
    'noplaylist': True,  # Download single video instead of a playlist if in doubt.
    'no_check_certificate': True,  # Do not verify SSL certificates
    'ignoreerrors': True,  # Ignore errors
    'quiet': True,  # No output/print
    'no_warnings': True,  # Ignore warnings
    'default_search': 'auto',  # Prepend this string if an input url is not valid, auto for elaborate guessing
    'cookiefile': config_file.cookie_path,  # cookiefile to be able to play age restricted videos
    'cachedir': 'store_false',  # Disabled cache to prevent HTTP 403 errors
    "include_ads": False
}
ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 15'  # Auto reconnect, otherwise songs randomly stop
}
sleeptask = 0


async def sleepasyncio(video_length, ctx):
    serverid = ctx.guild.id
    musiclist = await musicqueue.read(serverid)
    await asyncio.sleep(video_length)
    if await disconnected.read(serverid) == 0:
        ctx.voice_client.stop()
        if await loops.read("queue", serverid) == 1:
            await musicqueue.write(musiclist[0]["url"], musiclist[0]["title"], musiclist[0]["duration"], serverid)
            await musicqueue.delete(serverid)
            musiclist = await musicqueue.read(serverid)
            await musicqueue.sqlsort(musiclist, serverid)
        elif await loops.read("song", serverid) == 0 and await loops.read("queue", serverid) == 0:
            await musicqueue.delete(serverid)
            del musiclist[0]


async def playvideo(ctx):
    global sleeptask
    serverid = ctx.guild.id
    musiclist = await musicqueue.read(serverid)
    doeidruif = await turnonoff.read(serverid, 'doeidruif')
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
    while len(musiclist) > 0:
        skippedornot = await skipped.read(serverid)
        if skippedornot == 1 or await disconnected.read(serverid) == 1:
            sleeptask.cancel()
            await skipped.update(0, serverid)
            await disconnected.update(0, serverid)
        hour = musiclist[0]['duration'].split(':')[0]
        minutes = musiclist[0]['duration'].split(':')[1]
        seconds = musiclist[0]['duration'].split(':')[2]
        video_length = int(hour) * 3600 + int(minutes) * 60 + int(seconds)
        if skippedornot == 0:
            with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
                data = ydl.extract_info(musiclist[0]['url'], download=False)
            filename = data["url"]
            ctx.voice_client.play(discord.FFmpegPCMAudio(filename, **ffmpeg_options))
        else:
            ctx.voice_client.resume()
            await skipped.update(0, serverid)
        sleeptask = asyncio.create_task(sleepasyncio(video_length, ctx))
        try:
            await sleeptask
        except asyncio.CancelledError:
            pass
        musiclist = await musicqueue.read(serverid)
    if await disconnected.read(serverid) == 0:
        ctx.voice_client.stop()
        if doeidruif == 1:
            ctx.voice_client.play(discord.FFmpegPCMAudio(source=config_file.doei_druif_path))
            with audioread.audio_open(config_file.doei_druif_path) as f:
                await asyncio.sleep(f.duration)
        await ctx.voice_client.disconnect()
