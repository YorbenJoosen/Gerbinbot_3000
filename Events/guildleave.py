from SQL import guildleft


async def guildleave(guild):
    await guildleft.disconnected(guild)
    await guildleft.skip(guild)
    await guildleft.loops(guild)
    await guildleft.pause(guild)
    await guildleft.turnonoff(guild)
    await guildleft.leaderboardvoice(guild)
    await guildleft.leaderboardtext(guild)
    await guildleft.leaderboardcamera(guild)
    await guildleft.leaderboarstream(guild)
    await guildleft.quotes(guild)