import aiohttp
import config_file


async def gamedeals(ctx):
    gamedeals = ""
    async with aiohttp.ClientSession() as session:
        async with session.get(config_file.gamedeals_url) as response:
            data = await response.json()
            for post in data["data"]["children"]:
                title = post.get("data", {}).get('title')
                if any(name in title for name in
                       ('[STEAM]', '[Steam]', '[Epic Games]', '[Uplay]', '[Epic]', '[UPLAY]', '[Humble]', '[Humble Bundle]')) and any(
                        name in title for name in ('free', 'Free', '100%')):
                    gamedeals += title + "\n"
    if gamedeals == "":
        await ctx.channel.send('There are currently no free games.')
    else:
        await ctx.channel.send(gamedeals)
