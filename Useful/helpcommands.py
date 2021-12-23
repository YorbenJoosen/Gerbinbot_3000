async def helpcommands(ctx):
    await ctx.send('**__Music Commands__**\n' +
                   '**1)** __G!play + youtube-url__: Adds the given query to the queue.\n' +
                   '**2)** __G!pause__: Pauses the song currently playing.\n' +
                   '**3)** __G!resume__: Resumes the song currently playing.\n' +
                   '**4)** __G!disconnect__: Disconnects the bot.\n' +
                   '**5)** __G!skipto + position__: Skips to the given position in the queue.\n' +
                   '**6)** __G!skip__: Skips to the next song in the queue.\n' +
                   '**7)** __G!queue__: Shows all the songs currently in the queue.\n' +
                   '**8)** __G!clearqueue__: Clears the queue.\n' +
                   '**9)** __G!loopsong__: Loops the current song.\n' +
                   '**10)** __G!loopqueue__: Loops the whole queue.\n' +
                   '**11)** __G!shuffle__: Shuffles the queue.')
    await ctx.send('**__Useful Commands__**\n' +
                   '**1)** __G!password + length__: Generates a password of the desired length and sends it via dm.\n' +
                   '**2)** __G!leaderboardtext__: Shows the current leaderboard of text messages.\n' +
                   '**3)** __G!leaderboardvoice__: Shows the current leaderboard of being in a voice channel.\n' +
                   '**4)** __G!leaderboardcamera__: Shows the current leaderboard of having your camera on.\n' +
                   '**5)** __G!leaderboardstream__: Shows the current leaderboard of streaming.\n' +
                   '**6)** __G!time__: Gives you the current time and date.\n' +
                   '**7)** __G!info__: Shows server info.\n' +
                   '**8)** __G!addquote quote + @user__: Adds the quote to the database. \n' +
                   '**9)** __G!quotes__: Sends the quotes that are already in the database. \n' +
                   '**10)** __G!calculate + equation__: Calculates your equation.')
    await ctx.send('**__Random Commands__**\n' +
                   '**1)** __G!tutturu__: Plays tutturu.\n' +
                   '**2)** __G!gamedeals__: Shows the current free games in the subreddit GameDeals.\n' +
                   '**3)** __G!copypasta__: Sends a random copypasta from the subreddit copypasta.\n' +
                   '**4)** __G!meme__: Sends a random meme.\n' +
                   '**5)** __G!gayrate__: Shows you how gay you are.\n' +
                   '**6)** __G!simprate__: Shows how big of a simp you are.\n' +
                   '**7)** __G!dicklength__: Gives you the length of your dick.\n' +
                   '**8)** __G!vaginawidth__: Gives you the width of your vagina.\n' +
                   '**9)** __G!boobsize__: Gives you your boob size.\n' +
                   '**10)** __G!rps + Rock, Paper or Scissors__: Play Rock, Paper Scissors with the bot until somebody wins with 3 points.\n' +
                   '**11)** __G!coinflip__: The bot flips a coin for you.\n' +
                   '**12)** __G!repeat + text__: The bot repeats your message and deletes yours.')
