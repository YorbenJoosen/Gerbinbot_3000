from googleapiclient import discovery
from googleapiclient.discovery import build
from SQL import musicqueue
from Music import playvideo
import urllib.parse as urlparse
import config_file
youtube_api_key = config_file.youtube_api_key
youtube = build('youtube', 'v3', developerKey=youtube_api_key)


def video_id(value):
    query = urlparse.urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urlparse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None


async def playsingleurl(ctx, query, type):
    try:
        duration = 0
        title = ''
        videoid = video_id(query)
        durationrequest = youtube.videos().list(part='contentDetails', id=videoid)
        durationresponse = durationrequest.execute()
        for item in durationresponse['items']:
            duration = item['contentDetails']['duration']
            duration = duration.replace('PT', '')
            hours = '00'
            minutes = '00'
            seconds = '00'
            if 'H' in duration and 'M' in duration and 'S' in duration:
                hours = duration.split('H')[0]
                minutes = duration.split('H')[1].split('M')[0]
                seconds = duration.split('H')[1].split('M')[0].replace('S', '')
            elif 'H' in duration and 'M' in duration:
                hours = duration.split('H')[0]
                minutes = duration.split('H')[1].replace('M', '')
                seconds = '00'
            elif 'H' in duration and 'S' in duration:
                hours = duration.split('H')[0]
                minutes = '00'
                seconds = duration.split('H')[1].replace('S', '')
            elif 'H' in duration:
                hours = duration.replace('H', '')
                minutes = '00'
                seconds = '00'
            elif 'M' in duration and 'S' in duration:
                hours = '00'
                minutes = duration.split('M')[0]
                seconds = duration.split('M')[1].replace('S', '')
            elif 'M' in duration:
                hours = '00'
                minutes = duration.replace('M', '')
                seconds = '00'
            elif 'S' in duration:
                hours = '00'
                minutes = '00'
                seconds = duration.replace('S', '')
            if int(hours) < 10 and not int(hours) == 0:
                hours = '0' + str(hours)
            if int(minutes) < 10 and not int(minutes) == 0:
                minutes = '0' + str(minutes)
            if int(seconds) < 10 and not int(seconds) == 0:
                seconds = '0' + str(seconds)
            duration = str(hours) + ':' + str(minutes) + ':' + str(seconds)
        titlesrequest = youtube.videos().list(part='snippet', id=videoid)
        titleresponse = titlesrequest.execute()
        for item in titleresponse['items']:
            title = item['snippet']['title']
        await musicqueue.write(query, title, duration, ctx.guild.id)
        if type == 'normal':
            await ctx.reply('Song has been added to the queue.')
        elif type == 'slash':
            await ctx.respond('Song has been added to the queue.')
        musiclist = await musicqueue.read(ctx.guild.id)
        if len(musiclist) == 1:
            await playvideo.playvideo(ctx)
    except discovery.HttpError:
        if type == 'normal':
            await ctx.reply('This is not a correct url.')
        elif type == 'slash':
            await ctx.respond('This is not a correct url.')
