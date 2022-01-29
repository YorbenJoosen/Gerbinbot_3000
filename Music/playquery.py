from youtube_search import YoutubeSearch
from SQL import musicqueue
from Music import playvideo


async def playquery(ctx, query, type):
    results = YoutubeSearch(query, max_results=10).to_dict()
    id = results[0]["id"]
    url = "https://www.youtube.com/watch?v=" + id
    title = results[0]["title"]
    duration = results[0]["duration"]
    if duration.count(":") == 0:
        seconds = int(duration)
        if seconds < 10:
            duration = "00:00:0" + duration
        else:
            duration = "00:00:" + duration
    elif duration.count(":") == 1:
        seconds = duration.split(":")[1]
        minutes = duration.split(":")[0]
        if int(minutes) < 10:
            minutes = "0" + duration.split(":")[0]
        if int(seconds) < 10:
            seconds = "0" + duration.split(":")[1]
        duration = "00:" + minutes + ":" + seconds
    elif duration.count(":") == 2:
        seconds = duration.split(":")[2]
        minutes = duration.split(":")[1]
        hours = duration.split(":")[0]
        if int(hours) < 10:
            hours = "0" + duration.split(":")[0]
        if int(minutes) < 10:
            minutes = "0" + duration.split(":")[1]
        if int(seconds) < 10:
            seconds = "0" + duration.split(":")[2]
        duration = hours + ":" + minutes + ":" + seconds
    await musicqueue.write(url, title, duration, ctx.guild.id)
    if type == 'normal':
        await ctx.reply('Song has been added to the queue.')
    elif type == 'slash':
        await ctx.respond('Song has been added to the queue.')
    musiclist = await musicqueue.read(ctx.guild.id)
    if len(musiclist) == 1:
        await playvideo.playvideo(ctx)
