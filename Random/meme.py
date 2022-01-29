import random
import aiohttp
import config_file


async def meme(ctx, type):
    imagenumber = random.randrange(1, 20)
    subredditlink = random.choice(config_file.meme_urls)
    subreddit = subredditlink.replace("/hot/.json", "")
    subreddit = subreddit.replace("/hot/.json", "")
    async with aiohttp.ClientSession() as session:
        async with session.get(subredditlink) as response:
            data = await response.json()
            url = data['data']['children'][imagenumber]['data']['url']
            if type == 'normal':
                await ctx.reply("This meme came from the subreddit " + subreddit + ".\n" + url)
            elif type == 'slash':
                await ctx.respond("This meme came from the subreddit " + subreddit + ".\n" + url)
