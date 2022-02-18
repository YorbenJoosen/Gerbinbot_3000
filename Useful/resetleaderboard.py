from SQL import guildleft


async def resetleaderboard(ctx, option, type):
    if option == 'all':
        await guildleft.leaderboardvoice(ctx.guild)
        await guildleft.leaderboardtext(ctx.guild)
        await guildleft.leaderboardcamera(ctx.guild)
        await guildleft.leaderboarstream(ctx.guild)
        if type == 'normal':
            await ctx.repy('All leaderboards have been reset.')
        elif type == 'slash':
            await ctx.respond('All leaderboards have been reset.')
    elif option == 'voice':
        await guildleft.leaderboardvoice(ctx.guild)
        if type == 'normal':
            await ctx.reply('Voice leaderboard has been reset.')
        elif type == 'slash':
            await ctx.respond('Voice leaderboard has been reset.')
    elif option == 'text':
        await guildleft.leaderboardtext(ctx.guild)
        if type == 'normal':
            await ctx.reply('Text leaderboard has been reset.')
        elif type == 'slash':
            await ctx.respond('Text leaderboard has been reset.')
    elif option == 'camera':
        await guildleft.leaderboardcamera(ctx.guild)
        if type == 'normal':
            await ctx.reply('Camera leaderboard has been reset.')
        elif type == 'slash':
            await ctx.respond('Camera leaderboard has been reset.')
    elif option == 'stream':
        await guildleft.leaderboarstream(ctx.guild)
        if type == 'stream':
            await ctx.reply('Stream leaderboard has been reset.')
        elif type == 'slash':
            await ctx.respond('Stream leaderboard has been reset.')
