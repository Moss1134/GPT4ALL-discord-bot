import discord
from discord.app_commands import CommandTree
from gpt4all import GPT4All
import config

aiclient = GPT4All(config.model_name)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = CommandTree(client)
client.tree = tree

@client.event

async def on_ready():
    synced = await client.tree.sync()
    print(str(len(synced)) + " commands have been loaded. \n systems are now a-go!")

@client.tree.command(name = "ai", description="Get's an AI's response", nsfw= False)
async def stop(interaction: discord.Integration, prompt: str):
    print(str(interaction.user) + " said: " + prompt)
    await interaction.response.defer()
    response: str = "bot response: " + aiclient.generate(prompt=prompt, n_batch=16) 
    print(response)
    await interaction.followup.send(response)
client.run(config.TOKEN)