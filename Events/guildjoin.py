from SQL import guildjoined


async def guildjoin(guild):
    await guildjoined.disconnected(guild)
    await guildjoined.skip(guild)
    await guildjoined.loops(guild)
    await guildjoined.pause(guild)
    await guildjoined.turnonoff(guild)