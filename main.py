import datetime

from discord import Option
from discord.ext.commands import has_guild_permissions, MissingPermissions, CommandNotFound

import config_file
import discord
from discord.ext import commands

from Events import voice_update, onmessage, memberleft, guildjoin, guildleave
from Hidden import invite, deleteinvite
from Music import play, loopqueue, loopsong, disconnect, clearqueue, pausemusic, resumemusic, queue, shuffle, skip, \
    skipto, record
from Random import tutturu, gamedeals, copypasta, meme, gayrate, simprate, dicklength, vaginawidth, boobsize, coinflip, \
    repeat, rps
from SQL import loops, musicqueue, pause, skipped, disconnected
from Useful import password, info, helpcommands, leaderboardvoice, leaderboardtext, addquote, sendquotes, calculate, \
    leaderboardcamera, leaderboardstream, leaderboardzevensprong, addzevensprong, turnoff, turnon, randomsound, \
    resetleaderboard, leaderboardcoffee, addcoffee

discordtoken = config_file.bot_token
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="G!", intents=intents, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="G!help"))
    serverids = bot.guilds
    for i in range(len(serverids)):
        serverid = serverids[i].id
        await musicqueue.empty(serverid)
        await loops.update("song", 0, serverid)
        await loops.update("queue", 0, serverid)
        await pause.update(0, serverid)
        await skipped.update(0, serverid)
        await disconnected.update(0, serverid)
    print('Gerbinbot 3000 ready for duty!')


class Usefulcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Generates a password of a desired length and sends it via dm
    @commands.command()
    async def password(self, ctx, *, length):
        await password.password(ctx, length, 'normal')

    @commands.slash_command(name='password', description='The bot sends you a password of the desired length.')
    async def slashpassword(self, ctx, length: Option(int, "Enter your desired length.", min_value=1, max_value=1999, required=True)):
        await password.password(ctx, length, 'slash')

    # Gives back the time and date
    @commands.command()
    async def time(self, ctx):
        await ctx.channel.send(datetime.datetime.now())

    @commands.slash_command(name='time', description='The bot gives you the time.')
    async def slashtime(self, ctx):
        await ctx.respond(datetime.datetime.now())

    # Rickrolls the user
    @commands.command()
    async def info(self, ctx):
        await info.info(ctx, 'normal')

    @commands.slash_command(name='info', description='The bot gives you some general info.')
    async def slashinfo(self, ctx):
        await info.info(ctx, 'slash')

    # Shows the available functions
    @commands.command(aliases=["help", "commands"])
    async def helpcommands(self, ctx):
        await helpcommands.helpcommands(ctx, 'normal')

    @commands.slash_command(name='help', description='The bot shows you all available commands.')
    async def slashhelp(self, ctx):
        await helpcommands.helpcommands(ctx, 'slash')

    # Prints the voice leaderboard
    @commands.command(aliases=["voice"])
    async def leaderboardvoice(self, ctx, *, user=None):
        await leaderboardvoice.leaderboardvoice(ctx, user, 'normal')

    @commands.slash_command(name='leaderboardvoice', description='The bot sends the voice leaderboard.')
    async def slashleaderboardvoice(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardvoice.leaderboardvoice(ctx, user, 'slash')

    # Prints the text leaderboard
    @commands.command(aliases=["text"])
    async def leaderboardtext(self, ctx, *, user=None):
        await leaderboardtext.leaderboardtext(ctx, user, 'normal')

    @commands.slash_command(name='leaderboardtext', description='The bot sends the text leaderboard.')
    async def slashleaderboardtext(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardtext.leaderboardtext(ctx, user, 'slash')

    # Prints the camera leaderboard
    @commands.command(aliases=["camera", 'cam'])
    async def leaderboardcamera(self, ctx, *, user=None):
        await leaderboardcamera.leaderboardcamera(ctx, user, 'normal')

    @commands.slash_command(name='leaderboardcamera', description='The bot sends the camera leaderboard.')
    async def slashleaderboardcamera(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardcamera.leaderboardcamera(ctx, user, 'slash')

    # Prints the stream leaderboard
    @commands.command(aliases=["stream"])
    async def leaderboardstream(self, ctx, *, user=None):
        await leaderboardstream.leaderboardstream(ctx, user, 'normal')

    @commands.slash_command(name='leaderboardstream', description='The bot sends the stream leaderboard.')
    async def slashleaderboardstream(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardstream.leaderboardstream(ctx, user, 'slash')

    # Prints the zevensprong leaderboard
    @commands.command(aliases=["7sprong", "zevensprong", "zevesprong", "7"])
    async def leaderboardzevensprong(self, ctx, *, user=None):
        await leaderboardzevensprong.leaderboardzevensprong(ctx, user, bot, 'normal')

    @commands.slash_command(name='leaderboardzevensprong', description='The bot sends the zevensprong leaderboard.')
    async def slashleaderboardzevensprong(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardzevensprong.leaderboardzevensprong(ctx, user, bot, 'slash')

    # Adds a zevensprong amount to the leaderboard
    @commands.command(aliases=["7add", "7sprongadd", "zeveadd", "zevenadd", "zevensprongadd", "zevesprongadd", "add7", "addzeven", "addzeve", "addzevesprong"])
    async def addzevensprong(self, ctx, *, zevensprongstring):
        await addzevensprong.addzevensprong(ctx, zevensprongstring, amount=0, user=None, type='normal')

    @commands.slash_command(name='addzevensprong', description='Add a zevensprong.')
    async def slashaddzevensprong(self, ctx, amount: Option(int, 'Amount of zevensprongen.', required=True), user: Option(discord.Member, 'Define the user.', required=True)):
        await addzevensprong.addzevensprong(ctx, zevensprongstring='', amount=amount, user=user, type='slash')

    # Prints the koffie leaderboard
    @commands.command(aliases=["coffee"])
    async def leaderboardcoffee(self, ctx, *, user=None):
        await leaderboardcoffee.leaderboardcoffee(ctx, user, bot, 'normal')

    @commands.slash_command(name='leaderbordcoffee', description='The bot sends the coffee leaderboard.')
    async def slashleaderboardcoffee(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await leaderboardcoffee.leaderboardcoffee(ctx, user, bot, 'slash')

    # Adds a koffie amount to the leaderboard
    @commands.command(aliases=["addcoffee"])
    async def addcoffee(self, ctx, *, coffeestring):
        await addcoffee.addcoffee(ctx, coffeestring, amount=0, type='normal')

    @commands.slash_command(name='addcoffee', description='Add coffee.')
    async def addcoffee(self, ctx, amount: Option(int, 'Amount of coffee.', required=True)):
        await addcoffee.addcoffee(ctx, coffeestring='', amount=amount, type='slash')

    # Adds quotes to the database
    @commands.command(aliases=["quotesadd", "addquotes", "quoteadd"])
    async def addquote(self, ctx, *, quotestring):
        await addquote.addquote(ctx, quotestring, quote='', user=None, type='normal')

    @commands.slash_command(name='addquote', description='Add a quote.')
    async def slashaddquote(self, ctx, quote: Option(str, 'The quote.', required=True), user: Option(discord.Member, 'Define the user.', required=True)):
        await addquote.addquote(ctx, quotestring='', quote=quote, user=user, type='slash')

    # Adds quotes to the database
    @commands.command(aliases=["quotes", "sendquote"])
    async def sendquotes(self, ctx, *, user=None):
        await sendquotes.sendquotes(ctx, user, 'normal')

    @commands.slash_command(name='sendquotes', description='The bot sends the saved quotes.')
    async def slashsendquotes(self, ctx, user: Option(discord.Member, "Request a certain user.", required=False)):
        await sendquotes.sendquotes(ctx, user, 'slash')

    @commands.command(aliases=["calc", "calculator"])
    async def calculate(self, ctx, *, calculation):
        await calculate.calculate(ctx, calculation, 'normal')

    @commands.slash_command(name='calculate', description='The bot calculates your equation.')
    async def slashcalculate(self, ctx, calculation: Option(str, "The equation to be calculated.", required=True)):
        await calculate.calculate(ctx, calculation, 'slash')

    # Used to turn off certain functions
    @commands.command(aliases=["off"])
    @has_guild_permissions(administrator=True)
    async def turnoff(self, ctx, *, option):
        await turnoff.turnoff(ctx, option, 'normal')

    @commands.slash_command(name='turnoff', description='Turn off a certain function.')
    @has_guild_permissions(administrator=True)
    async def slashturnoff(self, ctx, option: Option(str, "Which function to turn off.", required=True, choices=config_file.functions)):
        await turnoff.turnoff(ctx, option, 'slash')

    # Used to turn on certain options
    @commands.command(aliases=["on"])
    @has_guild_permissions(administrator=True)
    async def turnon(self, ctx, *, option):
        await turnon.turnon(ctx, option, 'normal')

    @commands.slash_command(name='turnon', description='Turn on a certain function.')
    @has_guild_permissions(administrator=True)
    async def slashturnon(self, ctx, option: Option(str, "Which function to turn on.", required=True, choices=config_file.functions)):
        await turnon.turnon(ctx, option, 'slash')

    # Random sound
    @commands.command(aliases=["sound"])
    async def randomsound(self, ctx):
        await randomsound.randomsound(ctx, 'normal')

    @commands.slash_command(name='randomsound', description='Plays a random sound.')
    async def slashrandomsound(self, ctx):
        await randomsound.randomsound(ctx, 'slash')

    # Used to reset leaderboards
    @commands.command(aliases=["reset"])
    @has_guild_permissions(administrator=True)
    async def resetleaderboard(self, ctx, *, option):
        await resetleaderboard.resetleaderboard(ctx, option, 'normal')

    @commands.slash_command(name='reset', description="Reset a leaderboard")
    @has_guild_permissions(administrator=True)
    async def slashresetleaderboard(self, ctx, option: Option(str, "Which leaderboard do you want to reset", required=True, choices=['voice', 'text', 'camera', 'stream', 'all'])):
        await resetleaderboard.resetleaderboard(ctx, option, 'slash')


class Randomcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Lets the bot join and play the sound tutturu
    @commands.command(aliases=["tuturu", "tutturuu", "tuturuu"])
    async def tutturu(self, ctx):
        await tutturu.tutturu(ctx, 'normal')

    @commands.slash_command(name='tutturu', description='Plays the tutturu sound.')
    async def slashtutturu(self, ctx):
        await tutturu.tutturu(ctx, 'slash')

    # Sends the free games from subreddit GameDeals
    @commands.command(aliases=["deals"])
    async def gamedeals(self, ctx):
        await gamedeals.gamedeals(ctx, 'normal')

    @commands.slash_command(name='gamedeals', description='The bot sends the available gamedeas.')
    async def slashgamedeals(self, ctx):
        await gamedeals.gamedeals(ctx, 'slash')

    # Sends a random copypasta from the subreddit copypasta
    @commands.command()
    async def copypasta(self, ctx):
        await copypasta.copypasta(ctx, 'normal')

    @commands.slash_command(name='copypasta', description='The bot sends a random copypasta.')
    async def slashcopypasta(self, ctx):
        await copypasta.copypasta(ctx, 'slash')

    # Sends a random meme
    @commands.command()
    async def meme(self, ctx):
        await meme.meme(ctx, 'normal')

    @commands.slash_command(name='meme', description='The bot sends a random meme.')
    async def slashmeme(self, ctx):
        await meme.meme(ctx, 'slash')

    # Sends the percentage of the user's gayness
    @commands.command(aliases=["gayness", "gay"])
    async def gayrate(self, ctx, *, user=None):
        await gayrate.gayrate(ctx, 'normal', user, bot)

    @commands.slash_command(name='gayrate', description='The bot shows your gayness.')
    async def slashgayrate(self, ctx, user: Option(discord.Member, "Define a user.", required=False)):
        await gayrate.gayrate(ctx, 'slash', user, bot)

    # Sends the percentage of the user's simpness
    @commands.command(aliases=["simp"])
    async def simprate(self, ctx, *, user=None):
        await simprate.simprate(ctx, 'normal', user, bot)

    @commands.slash_command(name='simprate', description='The bot shows your simpness.')
    async def slashsimprate(self, ctx, user: Option(discord.Member, "Define a user.", required=False)):
        await simprate.simprate(ctx, 'slash', user, bot)

    # Sends the user dicklength
    @commands.command(aliases=["dick", "dicksize"])
    async def dicklength(self, ctx, *, user=None):
        await dicklength.dicklength(ctx, 'normal', user, bot)

    @commands.slash_command(name='dicklength', description='The bot shows your dicklength.')
    async def slashdicklength(self, ctx, user: Option(discord.Member, "Define a user.", required=False)):
        await dicklength.dicklength(ctx, 'slash', user, bot)

    # Sends the user's vagina
    @commands.command(aliases=["vagina", "vaginasize"])
    async def vaginawidth(self, ctx, *, user=None):
        await vaginawidth.vaginawidth(ctx, 'normal', user, bot)

    @commands.slash_command(name='vaginawidth', description='The bot shows your vaginawidth.')
    async def slashvaginawidth(self, ctx, user: Option(discord.Member, "Define a user.", required=False)):
        await vaginawidth.vaginawidth(ctx, 'slash', user, bot)

    # Sends the user's boobsize
    @commands.command(aliases=["boob"])
    async def boobsize(self, ctx, *, user=None):
        await boobsize.boobsize(ctx, 'normal', user, bot)

    @commands.slash_command(name='boobsize', description='The bot shows your boobsize.')
    async def slashboobsize(self, ctx, user: Option(discord.Member, "Define a user.", required=False)):
        await boobsize.boobsize(ctx, 'slash', user, bot)

    # Tosses a coin for the user
    @commands.command(aliases=["toss", "cointoss"])
    async def coinflip(self, ctx):
        await coinflip.coinflip(ctx, 'normal')

    @commands.slash_command(name='coinflip', description='The bot flips a coin for you.')
    async def slashcoinflip(self, ctx):
        await coinflip.coinflip(ctx, 'slash')

    # Makes the bot repeat the message the user sent
    @commands.command()
    async def repeat(self, ctx, *, message):
        await repeat.repeat(ctx, message, 'normal')

    @commands.slash_command(name='repeat', descirption='The bot repeats your message.')
    async def slashrepeat(self, ctx, *, message: Option(str, 'The message.', required=True)):
        await repeat.repeat(ctx, message, 'slash')

    # Play rock, paper, scissors against the bot
    @commands.command(aliases=["rockpaperscissors", "rock, paper, scissors"])
    async def rps(self, ctx, *, answer):
        await rps.rps(ctx, answer, 'normal')

    @commands.slash_command(name='rps', description='Play rock, paper, scissors against the bot.')
    async def slashrps(self, ctx, answer: Option(str, 'Give your answer.', choices=['Rock', 'Paper', 'Scissors'])):
        await rps.rps(ctx, answer, 'slash')


class Musiccommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Plays the given query
    @commands.command(aliases=["search"])
    async def play(self, ctx, *, query):
        await play.play(ctx, query, 'normal')

    @commands.slash_command(name='play', description='Add a song to the queue.')
    async def slashplay(self, ctx, query: Option(str, 'Url or search query.', required=True)):
        await play.play(ctx, query, 'slash')

    # Loops the song that is playing atm
    @commands.command()
    async def loopsong(self, ctx):
        await loopsong.loopsong(ctx, 'normal')

    @commands.slash_command(name='loopsong', description='Loops the current song.')
    async def slashloopsong(self, ctx):
        await loopsong.loopsong(ctx, 'slash')

    # loops the queue
    @commands.command()
    async def loopqueue(self, ctx):
        await loopqueue.loopqueue(ctx, 'normal')

    @commands.slash_command(name='loopqueue', description='Loop the queue.')
    async def slashloopqueue(self, ctx):
        await loopqueue.loopqueue(ctx, 'slash')

    # Disconnects the bot and empties the url database
    @commands.command(aliases=["leave"])
    async def disconnect(self, ctx):
        await disconnect.disconnect(ctx, 'normal')

    @commands.slash_command(name='disconnect', description='Disconnect the bot.')
    async def slashdisconnect(self, ctx):
        await disconnect.disconnect(ctx, 'slash')

    # Clears the queue
    @commands.command(aliases=["clear"])
    async def clearqueue(self, ctx):
        await clearqueue.clearqueue(ctx, 'normal')

    @commands.slash_command(name='clearqueue', description='Clear the queue.')
    async def slashclearqueue(self, ctx):
        await clearqueue.clearqueue(ctx, 'slash')

    # Pauses the queue
    @commands.command(aliases=["stop", "pause"])
    async def pausemusic(self, ctx):
        await pausemusic.pausemusic(ctx, 'normal')

    @commands.slash_command(name='pausemusic', description='Pause the music.')
    async def slashpausemusic(self, ctx):
        await pausemusic.pausemusic(ctx, 'slash')

    # Resumes a paused queue
    @commands.command(aliases=["unpause", "resume"])
    async def resumemusic(self, ctx):
        await resumemusic.resumemusic(ctx, 'normal')

    @commands.slash_command(name='resumemusic', description='Resume the music.')
    async def slashresumemusic(self, ctx):
        await resumemusic.resumemusic(ctx, 'slash')

    # Shows which songs are queued
    @commands.command(aliases=["list", "songs"])
    async def queue(self, ctx):
        await queue.queue(ctx, 'normal')

    @commands.slash_command(name='queue', description='See the current queue.')
    async def slashqueue(self, ctx):
        await queue.queue(ctx, 'slash')

    # Shuffles the current playlist
    @commands.command()
    async def shuffle(self, ctx):
        await shuffle.shuffle(ctx, 'normal')

    @commands.slash_command(name='shuffle', description='Shuffle the queue.')
    async def slashshuffle(self, ctx):
        await shuffle.shuffle(ctx, 'slash')

    # Skips to the next song
    @commands.command(aliases=["skipsong", "next", "nextsong"])
    async def skip(self, ctx):
        await skip.skip(ctx, 'normal')

    @commands.slash_command(name='skip', description='Skip the current song.')
    async def slashskip(self, ctx):
        await skip.skip(ctx, 'slash')

    # Skips to the song which corresponds to the given number
    @commands.command()
    async def skipto(self, ctx, *, number):
        await skipto.skipto(ctx, number, 'normal')

    @commands.slash_command(name='skipto', description='Skips to a certain spot in the queue.')
    async def slashskipto(self, ctx, number: Option(int, "Position of the song.", required=True)):
        await skipto.skipto(ctx, number, 'slash')

    # Records the audio
    @commands.command()
    async def record(self, ctx, *, option):
        await record.record(ctx, option, 'normal')

    @commands.slash_command(name='record', description='Start or stop a recording.')
    async def slashrecord(self, ctx, option: Option(str, 'Give your answer.', choices=['start', 'stop'])):
        await record.record(ctx, option, 'slash')


class Hiddencommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Let's the bot create a sneaky invite
    @commands.command()
    async def invite(self, ctx):
        await invite.invite(ctx)

    # Deletes the sneaky invite
    @commands.command()
    async def deleteinvite(self, ctx):
        await deleteinvite.deleteinvite(ctx)


@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
    await voice_update.voice_update(member, before, after)


@bot.event
async def on_message(message):
    emojiguild = bot.get_guild(config_file.emojiguildid)
    await onmessage.onmessage(message, emojiguild)
    await bot.process_commands(message)


@bot.event
async def on_member_remove(member):
    await memberleft.memberleft(member)


@bot.event
async def on_guild_join(guild):
    await guildjoin.guildjoin(guild)


@bot.event
async def on_guild_remove(guild):
    await guildleave.guildleave(guild)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('You wrote the command wrong, you idiot!')
    elif isinstance(error, MissingPermissions):
        await ctx.reply('You do not have the required permissions!')


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond('You do not have the required permissions!')

bot.add_cog(Hiddencommands(bot))
bot.add_cog(Musiccommands(bot))
bot.add_cog(Usefulcommands(bot))
bot.add_cog(Randomcommands(bot))
bot.run(discordtoken)
