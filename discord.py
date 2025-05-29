import os
import asyncio
import discord
from discord import AllowedMentions

TOKEN = os.getenv("DISCORD_TOKEN")  # À définir dans l'hébergeur
CHANNEL_ID = 123456789012345678     # Remplace par l'ID de ton salon

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    if not channel:
        print("❌ Salon introuvable, vérifie l'ID.")
        return

    allowed = AllowedMentions(everyone=True)

    while True:
        try:
            await channel.send("@everyone 🔊 Notification automatique du bot !", allowed_mentions=allowed)
            print("✅ Message envoyé.")
            await asyncio.sleep(1)  # 5 secondes entre chaque message (respect des limites)
        except Exception as e:
            print(f"⚠️ Erreur : {e}")
            await asyncio.sleep(10)

client.run(TOKEN)
