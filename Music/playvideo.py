import asyncio
import audioread
import discord
import youtube_dl
import config_file
from SQL import musicqueue, loops, skipped, disconnected, turnonoff

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'cookiefile': r"C:\Users\yorbe\PycharmProjects\cookies.txt"
}
ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 15'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
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


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


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
            player = await YTDLSource.from_url(musiclist[0]['url'], stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
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
