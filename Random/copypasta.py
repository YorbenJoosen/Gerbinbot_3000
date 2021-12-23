import aiohttp
import random
import config_file


async def copypasta(ctx):
    subredditlink = config_file.copypasta_url
    copypastanumber = random.randrange(1, 29)
    async with aiohttp.ClientSession() as session:
        async with session.get(subredditlink) as response:
            data = await response.json()
            copypastatext = data['data']['children'][copypastanumber]['data']['selftext']
            if len(copypastatext) < 2000:
                await ctx.channel.send(copypastatext)
            else:
                await ctx.channel.send("The random copypasta I found was too long for Discord, but here is the link: " + data['data']['children'][copypastanumber]['data']['url'])
