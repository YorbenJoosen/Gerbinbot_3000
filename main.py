import datetime
import config_file
import discord
from discord.ext import commands

from Events import voice_update, onmessage, memberleft, guildjoin, guildleave
from Hidden import invite, deleteinvite
from Music import play, loopqueue, loopsong, disconnect, clearqueue, pausemusic, resumemusic, queue, shuffle, skip, \
    skipto
from Random import tutturu, gamedeals, copypasta, meme, gayrate, simprate, dicklength, vaginawidth, boobsize, coinflip, \
    repeat, rps
from SQL import loops, musicqueue, pause, skipped, disconnected
from Useful import password, info, helpcommands, leaderboardvoice, leaderboardtext, addquote, sendquotes, calculate, \
    leaderboardcamera, leaderboardstream, leaderboardzevensprong, addzevensprong

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
        await password.password(ctx, length)

    # Gives back the time and date
    @commands.command()
    async def time(self, ctx):
        await ctx.channel.send(datetime.datetime.now())

    # Rickrolls the user
    @commands.command()
    async def info(self, ctx):
        await info.info(ctx)

    # Shows the available functions
    @commands.command(aliases=["help", "commands"])
    async def helpcommands(self, ctx):
        await helpcommands.helpcommands(ctx)

    # Prints the voice leaderboard
    @commands.command(aliases=["voice"])
    async def leaderboardvoice(self, ctx, *, user=None):
        await leaderboardvoice.leaderboardvoice(ctx, user)

    # Prints the text leaderboard
    @commands.command(aliases=["text"])
    async def leaderboardtext(self, ctx, *, user=None):
        await leaderboardtext.leaderboardtext(ctx, user)

    # Prints the camera leaderboard
    @commands.command(aliases=["camera", 'cam'])
    async def leaderboardcamera(self, ctx, *, user=None):
        await leaderboardcamera.leaderboardcamera(ctx, user)

    # Prints the stream leaderboard
    @commands.command(aliases=["stream"])
    async def leaderboardstream(self, ctx, *, user=None):
        await leaderboardstream.leaderboardstream(ctx, user)

    # Prints the zevensprong leaderboard
    @commands.command(aliases=["7sprong", "zevensprong", "zevesprong", "7"])
    async def leaderboardzevensprong(self, ctx, *, user=None):
        await leaderboardzevensprong.leaderboardzevensprong(ctx, user, bot)

    # Adds a zevensprong amount to the leaderboard
    @commands.command(aliases=["7add", "7sprongadd", "zeveadd", "zevenadd", "zevensprongadd", "zevesprongadd", "add7", "addzeven", "addzeve", "addzevesprong"])
    async def addzevensprong(self, ctx, *, zevensprongstring):
        await addzevensprong.addzevensprong(ctx, zevensprongstring)

    # Adds quotes to the database
    @commands.command(aliases=["quotesadd", "addquotes", "quoteadd"])
    async def addquote(self, ctx, *, quotestring):
        await addquote.addquote(ctx, quotestring)

    # Adds quotes to the database
    @commands.command(aliases=["quotes", "sendquote"])
    async def sendquotes(self, ctx, *, user=None):
        await sendquotes.sendquotes(ctx, user)

    @commands.command(aliases=["calc", "calculator"])
    async def calculate(self, ctx, *, calculation):
        await calculate.calculate(ctx, calculation)


class Randomcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Lets the bot join and play the sound tutturu
    @commands.command(aliases=["tuturu", "tutturuu", "tuturuu"])
    async def tutturu(self, ctx):
        await tutturu.tutturu(ctx)

    # Sends the free games from subreddit GameDeals
    @commands.command(aliases=["deals"])
    async def gamedeals(self, ctx):
        await gamedeals.gamedeals(ctx)

    # Sends a random copypasta from the subreddit copypasta
    @commands.command()
    async def copypasta(self, ctx):
        await copypasta.copypasta(ctx)

    # Sends a random meme
    @commands.command()
    async def meme(self, ctx):
        await meme.meme(ctx)

    # Sends the percentage of the user's gayness
    @commands.command(aliases=["gayness", "gay"])
    async def gayrate(self, ctx):
        await gayrate.gayrate(ctx)

    # Sends the percentage of the user's simpness
    @commands.command(aliases=["simp"])
    async def simprate(self, ctx):
        await simprate.simprate(ctx)

    # Sends the user dicklength
    @commands.command(aliases=["dick", "dicksize"])
    async def dicklength(self, ctx):
        await dicklength.dicklength(ctx)

    # Sends the user's vagina
    @commands.command(aliases=["vagina", "vaginasize"])
    async def vaginawidth(self, ctx):
        await vaginawidth.vaginawidth(ctx)

    # Sends the user's boobsize
    @commands.command(aliases=["boob"])
    async def boobsize(self, ctx):
        await boobsize.boobsize(ctx)

    # Tosses a coin for the user
    @commands.command(aliases=["toss", "cointoss"])
    async def coinflip(self, ctx):
        await coinflip.coinflip(ctx)

    # Makes the bot repeat the message the user sent
    @commands.command()
    async def repeat(self, ctx, *, message):
        await repeat.repeat(ctx, message)

    # Play rock, paper, scissors against the bot
    @commands.command(aliases=["rockpaperscissors", "rock, paper, scissors"])
    async def rps(self, ctx, *, answer):
        await rps.rps(ctx, answer)


class Musiccommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Plays the given query
    @commands.command(aliases=["search"])
    async def play(self, ctx, *, query):
        await play.play(ctx, query)

    # Loops the song that is playing atm
    @commands.command()
    async def loopsong(self, ctx):
        await loopsong.loopsong(ctx)

    # loops the queue
    @commands.command()
    async def loopqueue(self, ctx):
        await loopqueue.loopqueue(ctx)

    # Disconnects the bot and empties the url database
    @commands.command(aliases=["leave"])
    async def disconnect(self, ctx):
        await disconnect.disconnect(ctx)

    # Clears the queue
    @commands.command(aliases=["clear"])
    async def clearqueue(self, ctx):
        await clearqueue.clearqueue(ctx)

    # Pauses the queue
    @commands.command(aliases=["stop", "pause"])
    async def pausemusic(self, ctx):
        await pausemusic.pausemusic(ctx)

    # Resumes a paused queue
    @commands.command(aliases=["unpause", "resume"])
    async def resumemusic(self, ctx):
        await resumemusic.resumemusic(ctx)

    # Shows which songs are queued
    @commands.command(aliases=["list", "songs"])
    async def queue(self, ctx):
        await queue.queue(ctx)

    # Shuffles the current playlist
    @commands.command()
    async def shuffle(self, ctx):
        await shuffle.shuffle(ctx)

    # Skips to the next song
    @commands.command(aliases=["skipsong", "next", "nextsong"])
    async def skip(self, ctx):
        await skip.skip(ctx)

    # Skips to the song which corresponds to the given number
    @commands.command()
    async def skipto(self, ctx, *, number):
        await skipto.skipto(ctx, number)


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
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('You wrote the command wrong, you idiot!')


bot.add_cog(Hiddencommands(bot))
bot.add_cog(Musiccommands(bot))
bot.add_cog(Usefulcommands(bot))
bot.add_cog(Randomcommands(bot))
bot.run(discordtoken)
