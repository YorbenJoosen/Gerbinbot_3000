from googleapiclient import discovery
from googleapiclient.discovery import build
from SQL import musicqueue
from Music import playvideo
import config_file
youtube_api_key = config_file.youtube_api_key
youtube = build('youtube', 'v3', developerKey=youtube_api_key)


async def playlist(ctx, query, type):
    try:
        url = query
        nextPageToken = None
        videoids = []
        urls = []
        durations = []
        titles = []
        length = 0
        playlistid = url.replace('https://www.youtube.com/playlist?list=', '')
        while True:
            idsrequest = youtube.playlistItems().list(part='contentDetails', playlistId=playlistid, maxResults=50,
                                                      pageToken=nextPageToken)
            idsresponse = idsrequest.execute()
            for item in idsresponse['items']:
                if 'videoPublishedAt' in item['contentDetails']:
                    url = 'https://www.youtube.com/watch?v=' + item['contentDetails']['videoId']
                    urls.append(url)
                videoids.append(item['contentDetails']['videoId'])
            ids = ','.join(videoids)
            durationrequest = youtube.videos().list(part="contentDetails", id=ids)
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
                durations.append(duration)
            titlesrequest = youtube.videos().list(part='snippet', id=ids)
            titleresponse = titlesrequest.execute()
            for item in titleresponse['items']:
                title = item['snippet']['title']
                titles.append(title)
            for i in range(len(urls)):
                await musicqueue.write(urls[i], titles[i], durations[i], ctx.guild.id)
            length += len(urls)
            urls = []
            durations = []
            titles = []
            videoids = []
            nextPageToken = idsresponse.get('nextPageToken')
            if not nextPageToken:
                break
        if type == 'normal':
            await ctx.reply('Playlist has been added to the queue.')
        elif type == 'slash':
            await ctx.respond('Playlist has been added to the queue.')
        musiclist = await musicqueue.read(ctx.guild.id)
        if length == len(musiclist):
            await playvideo.playvideo(ctx)
    except discovery.HttpError:
        if type == 'normal':
            await ctx.reply('This is not a correct url.')
        elif type == 'slash':
            await ctx.respond('This is not a correct url.')
