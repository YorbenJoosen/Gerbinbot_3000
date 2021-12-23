import datetime

from SQL import musicqueue, loops, pause, voice, skipped, disconnected, camera, stream


async def voice_update(member, before, after):
    if member.bot:  # If the bot disconnects or is force disconnected, it resets its music values
        if before.channel and not after.channel:  # Checks if the bot was in a channel and then disconnected
            serverid = before.channel.guild.id
            await musicqueue.empty(serverid)
            await loops.update("queue", 0, serverid)
            await loops.update("song", 0, serverid)
            await pause.update(0, serverid)
            await skipped.update(0, serverid)
            await disconnected.update(1, serverid)
    else:  # If a user joins a channel or goes unmuted or leaves the afk channel, the bot.leaderboardvoice will start counting
        if (not before.channel and after.channel) or (before.self_mute and not after.self_mute) or (before.afk and not after.afk and after.channel):
            i = 0
            begintime = datetime.datetime.now()
            begintime_total = begintime.hour * 60 + begintime.minute
            voicelist = await voice.read()
            while i < len(voicelist):
                if voicelist[i]['userid'] == member.id and voicelist[i]['serverid'] == after.channel.guild.id:  # Checks if a user is already in the bot.leaderboardvoice list
                    voicelist[i]['begintime'] = begintime_total
                    await voice.update(voicelist[i]["userid"], voicelist[i]["begintime"], voicelist[i]["endtime"], voicelist[i]["score"], voicelist[i]["serverid"])
                    i = len(voicelist)
                elif i == len(voicelist) - 1:  # If the code gets to the end of the list without finding the user, it adds the user to the list
                    voicelist.append({'userid': member.id, 'begintime': begintime_total, 'endtime': 0, 'score': 0, "serverid": after.channel.guild.id})
                    i += 1
                    await voice.write(voicelist[i]["userid"], voicelist[i]["begintime"], voicelist[i]["endtime"], voicelist[i]["score"], voicelist[i]["serverid"])
                else:
                    i += 1
        # If a user disconnects or goes muted or goes to the afk channel, the counting stops and the score is refreshed
        if (not before.self_mute and after.self_mute) or (not before.afk and after.afk):
            i = 0
            voicelist = await voice.read()
            endtime = datetime.datetime.now()
            endtime_total = endtime.hour * 60 + endtime.minute
            while i < len(voicelist):
                if voicelist[i]['userid'] == member.id and voicelist[i]['serverid'] == before.channel.guild.id:
                    voicelist[i]['endtime'] = endtime_total
                    if voicelist[i]['endtime'] < voicelist[i]['begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                        voicelist[i]['score'] += 24 * 60 - (voicelist[i]['begintime'] - voicelist[i]['endtime'])
                    else:
                        voicelist[i]['score'] += voicelist[i]['endtime'] - voicelist[i]['begintime']
                    await voice.update(voicelist[i]["userid"], voicelist[i]["begintime"], voicelist[i]["endtime"], voicelist[i]["score"], voicelist[i]["serverid"])
                    i = len(voicelist)
                else:
                    i += 1
        # If a user disconnects, all counters stop and the scores are refreshed
        if before.channel and not after.channel:
            i = 0
            voicelist = await voice.read()
            endtime = datetime.datetime.now()
            endtime_total = endtime.hour * 60 + endtime.minute
            while i < len(voicelist):
                if voicelist[i]['userid'] == member.id and voicelist[i]['serverid'] == before.channel.guild.id:  # We loop trough the list until we find the right user from the right server
                    voicelist[i]['endtime'] = endtime_total  # If we find the right user we update his endtime
                    if voicelist[i]['endtime'] < voicelist[i][
                        'begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                        voicelist[i]['score'] += 24 * 60 - (voicelist[i]['begintime'] - voicelist[i]['endtime'])
                    else:
                        voicelist[i]['score'] += voicelist[i]['endtime'] - voicelist[i]['begintime']
                    await voice.update(voicelist[i]["userid"], voicelist[i]["begintime"], voicelist[i]["endtime"], voicelist[i]["score"], voicelist[i]["serverid"])
                    i = len(voicelist)  # If we found the right user from the right server and updated his score and endtime, we get out of the loop
                else:
                    i += 1  # If the user and server don't match, we keep looping trough the list
            i = 0
            if before.self_video:
                cameralist = await camera.read()
                while i < len(cameralist):
                    if cameralist[i]['userid'] == member.id and cameralist[i]['serverid'] == before.channel.guild.id:  # We loop trough the list until we find the right user from the right server
                        cameralist[i]['endtime'] = endtime_total  # If we find the right user we update his endtime
                        if cameralist[i]['endtime'] < cameralist[i]['begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                            cameralist[i]['score'] += 24 * 60 - (cameralist[i]['begintime'] - cameralist[i]['endtime'])
                        else:
                            cameralist[i]['score'] += cameralist[i]['endtime'] - cameralist[i]['begintime']
                        await camera.update(cameralist[i]["userid"], cameralist[i]["begintime"], cameralist[i]["endtime"], cameralist[i]["score"], cameralist[i]["serverid"])
                        i = len(cameralist)  # If we found the right user from the right server and updated his score and endtime, we get out of the loop
                    else:
                        i += 1  # If the user and server don't match, we keep looping trough the list
            i = 0
            if before.self_stream:
                streamlist = await stream.read()
                while i < len(streamlist):
                    if streamlist[i]['userid'] == member.id and streamlist[i]['serverid'] == before.channel.guild.id:  # We loop trough the list until we find the right user from the right server
                        streamlist[i]['endtime'] = endtime_total  # If we find the right user we update his endtime
                        if streamlist[i]['endtime'] < streamlist[i]['begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                            streamlist[i]['score'] += 24 * 60 - (streamlist[i]['begintime'] - streamlist[i]['endtime'])
                        else:
                            streamlist[i]['score'] += streamlist[i]['endtime'] - streamlist[i]['begintime']
                        await stream.update(streamlist[i]["userid"], streamlist[i]["begintime"], streamlist[i]["endtime"], streamlist[i]["score"], streamlist[i]["serverid"])
                        i = len(streamlist)  # If we found the right user from the right server and updated his score and endtime, we get out of the loop
                    else:
                        i += 1  # If the user and server don't match, we keep looping trough the list
        # If a user starts their camera, bot.leaderboardcamera will begin
        if not before.self_video and after.self_video:
            i = 0
            begintime = datetime.datetime.now()
            begintime_total = begintime.hour * 60 + begintime.minute
            cameralist = await camera.read()
            while i < len(cameralist):
                if cameralist[i]['userid'] == member.id and cameralist[i]['serverid'] == after.channel.guild.id:  # Checks if a user is already in the bot.leaderboardcameralist
                    cameralist[i]['begintime'] = begintime_total
                    await camera.update(cameralist[i]["userid"], cameralist[i]["begintime"], cameralist[i]["endtime"], cameralist[i]["score"], cameralist[i]["serverid"])
                    i = len(cameralist)
                elif i == len(cameralist) - 1:  # If the code gets to the end of the list without finding the user, it adds the user to the list
                    cameralist.append({'userid': member.id, 'begintime': begintime_total, 'endtime': 0, 'score': 0, "serverid": after.channel.guild.id})
                    i += 1
                    await camera.write(cameralist[i]["userid"], cameralist[i]["begintime"], cameralist[i]["endtime"], cameralist[i]["score"], cameralist[i]["serverid"])
                else:
                    i += 1
        # If a user starts streaming, bot.leaderboardstream will begin
        if not before.self_stream and after.self_stream:
            i = 0
            begintime = datetime.datetime.now()
            begintime_total = begintime.hour * 60 + begintime.minute
            streamlist = await stream.read()
            while i < len(streamlist):
                if streamlist[i]['userid'] == member.id and streamlist[i]['serverid'] == after.channel.guild.id:  # Checks if a user is already in the bot.leaderboardstreamlist
                    streamlist[i]['begintime'] = begintime_total
                    await stream.update(streamlist[i]["userid"], streamlist[i]["begintime"], streamlist[i]["endtime"], streamlist[i]["score"], streamlist[i]["serverid"])
                    i = len(streamlist)
                elif i == len(streamlist) - 1:  # If the code gets to the end of the list without finding the user, it adds the user to the list
                    streamlist.append({'userid': member.id, 'begintime': begintime_total, 'endtime': 0, 'score': 0, "serverid": after.channel.guild.id})
                    i += 1
                    await stream.write(streamlist[i]["userid"], streamlist[i]["begintime"], streamlist[i]["endtime"], streamlist[i]["score"], streamlist[i]["serverid"])
                else:
                    i += 1
        # If a user stops their camera, bot.leaderboardcamera will stop
        if before.self_video and not after.self_video:
            i = 0
            endtime = datetime.datetime.now()
            endtime_total = endtime.hour * 60 + endtime.minute
            cameralist = await camera.read()
            while i < len(cameralist):
                if cameralist[i]['userid'] == member.id and cameralist[i]['serverid'] == before.channel.guild.id:  # Checks if a user is already in the list
                    cameralist[i]['endtime'] = endtime_total
                    if cameralist[i]['endtime'] < cameralist[i]['begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                        cameralist[i]['score'] += 24 * 60 - (cameralist[i]['begintime'] - cameralist[i]['endtime'])
                    else:
                        cameralist[i]['score'] += cameralist[i]['endtime'] - cameralist[i]['begintime']
                    await camera.update(cameralist[i]["userid"], cameralist[i]["begintime"], cameralist[i]["endtime"], cameralist[i]["score"], cameralist[i]["serverid"])
                    i = len(cameralist)
                else:
                    i += 1
        # If a user stops streaming, bot.leaderboardstream will stop
        if before.self_stream and not after.self_stream:
            i = 0
            endtime = datetime.datetime.now()
            endtime_total = endtime.hour * 60 + endtime.minute
            streamlist = await stream.read()
            while i < len(streamlist):
                if streamlist[i]['userid'] == member.id and streamlist[i]['serverid'] == before.channel.guild.id:  # Checks if a user is already in the list
                    streamlist[i]['endtime'] = endtime_total
                    if streamlist[i]['endtime'] < streamlist[i]['begintime']:  # When the endtime is lower then the begintime, it means that it's the next day and we need to change the formula
                        streamlist[i]['score'] += 24 * 60 - (streamlist[i]['begintime'] - streamlist[i]['endtime'])
                    else:
                        streamlist[i]['score'] += streamlist[i]['endtime'] - streamlist[i]['begintime']
                    await stream.update(streamlist[i]["userid"], streamlist[i]["begintime"], streamlist[i]["endtime"], streamlist[i]["score"], streamlist[i]["serverid"])
                    i = len(streamlist)
                else:
                    i += 1
