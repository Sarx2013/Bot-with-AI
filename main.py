import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.command
async def hola(ctx):
    await ctx.send("Hola!")

@client.command
async def check(ctx):
    await ctx.send("Envia una imagen para analizar")

    def imagen(m):
        return m.author==ctx.author and len(m.attachmets) > 0
    
    mensaje = await client.wait_for("message", check=imagen, timeout=60)
    imagen = mensaje.attachments[0]
    imagen.save(f"img/{imagen.filename}")
    await ctx.send("Imagen recibida y guardada correctamente")

client.run("MTU3MDU0NTI3OTc2ODMzMDI5MA.GXjVrM.OEGineu76lOOErFdwre9EzNsxoWQqX5tSksWo4")
