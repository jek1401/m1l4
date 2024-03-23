import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

words = ["яблоко", "карандаш", "програмирование", "муха", "ноутбук", "школа"]

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def com(ctx):
    await ctx.send(f'Команды: $hello,$heh,$game,$anekdoti,$random_word,$tractor')

@bot.command()
async def game(ctx):
    await ctx.send(f'Привет!Я бот {bot.user},и я помогу тебе найти игру если тебе скучно.Что бы продолжить напиши $games')

@bot.command()
async def games(ctx):
    await ctx.send(f'Экшн:Grand Theft Auto V,Doom Eternal,Devil May Cry 5 ;Шутеры:Call of Duty,Warzone,Overwatch,Counter-Strike Global Offensive;Ролевые игры (RPG):The Witcher 3: Wild Hunt,Final Fantasy XV,Persona 5')

@bot.command()
async def random_word(ctx):
    random_word = random.choice(words)
    await ctx.send(f'Случайное слово: {random_word}')

@bot.command()
async def tractor(ctx):
    repeated_word = "трактор " * 100
    await ctx.send(repeated_word)

@bot.command()
async def power(ctx, a: float, b: float):
    result = a ** b
    await ctx.send(f'{a} в степени {b} равно {result}')

bot.run("")
