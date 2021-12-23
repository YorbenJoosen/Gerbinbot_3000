from SQL import rockpaperscissors, voice, text, camera, stream


async def memberleft(member):
    userid = member.id
    guildid = member.guild.id
    await rockpaperscissors.delete(userid)
    await voice.delete(userid, guildid)
    await text.delete(userid, guildid)
    await camera.delete(userid, guildid)
    await stream.delete(userid, guildid)