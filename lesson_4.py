import discord
from key import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)

@bot.command()
async def all_math(ctx, x:int, y:int):
    await ctx.send(f"Сумма {x + y}")
    await ctx.send(f"Разность {x - y}")
    await ctx.send(f"Произведение {x * y}")
    await ctx.send(f"Деление {x / y}")

@bot.command()
async def procent(ctx, z:int, w:int):
    await ctx.send(f"Процент-от-суммы {z / 100 * w}")
    await ctx.send(f"Процент-от-выражения {z / w *100}")
    await ctx.send(f"Процент-от-произведения {z * w / 100}")


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)



bot.run(token())



bot.run(token())
