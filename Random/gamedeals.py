import aiohttp
import config_file


async def gamedeals(ctx, type):
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
        if type == 'normal':
            await ctx.reply('There are currently no free games.')
        elif type == 'slash':
            await ctx.respond('There are currently no free games.')
    else:
        if type == 'normal':
            await ctx.reply(gamedeals)
        elif type == 'slash':
            await ctx.respond(gamedeals)
