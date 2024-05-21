import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado con {bot.user}")

@bot.command()
async def manualidades(ctx):
    ideas = ["Realezar ladrillos ecologiocos.",
             "Construir un arbol con tapitas de adorno."]
    
    await ctx.send(random.choice(ideas))


@bot.command
async def clacificacion(ctx,*,item:str):
    reciclables = ["botella de plastico", "carton", "papel", "lata"]
    no_reciclables = ["pañales", "comida"]

    if item.lower() in reciclables:
        await ctx.send("puede ser reciclado")

    elif item.lower() in no_reciclables:
        await ctx.send("no puede ser reciclado")
    
    else:
        await ctx.send("no tengo conocimiento de ellos, me falta entrenar")
