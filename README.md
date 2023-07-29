# GPT4ALL-discord-bot

This will give you an AI of your choosing, that runs locally on your machine the abilty to send messages and reply's on any server you add the discord bot too!

## Set-up

+ Download the source-code
+ pip install everything under reqiurement.txt 
+ Open config.py in any text or code editor
+ Create a discord bot using this link: https://discord.com/developers/applications
+ Setup and invite the discord bot to one of your servers (required perms are Applications.commands, Bot, and all toggles under the Privileged Gateway Intents must be turned on)
+ Reset the bot's token and copy it into the varaiable discord_token, in the config.py file
+ Next go to https://gpt4all.io/index.html and find and copy the exact name of the AI model you want to use
+ Paste that name exactly as is into the config.py file under the varaible model_name: str =
+ Run the main.py file and the model file will download to your system and you will after have a running AI.

The default AI is a 7b paramater AI that will work on most systems, it is reccomended that you use that one unless you spesifically want another.
