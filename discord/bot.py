# # bot.py
# import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# client.run(TOKEN)








# import os
# import random

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# token = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)

# client.run(token)


















# # bot.py
# import os
# import random

# from discord.ext import commands
# from dotenv import load_dotenv

# load_dotenv()
# token = os.getenv('DISCORD_TOKEN')

# bot = commands.Bot(command_prefix='!')

# @bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
# async def nine_nine(ctx):
# 	brooklyn_99_quotes = [
# 	    'I\'m the human form of the 💯 emoji.',
# 	    'Bingpot!',
# 	    (
# 	        'Cool. Cool cool cool cool cool cool cool, '
# 	        'no doubt no doubt no doubt no doubt.'
# 	    ),
# 	]

# 	response = random.choice(brooklyn_99_quotes)
# 	await ctx.send(response)

# bot.run(token)












import os
import random

from discord.ext import commands
from dotenv import load_dotenv

import re

import sqlite3
from sqlite3 import Error

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='check:', help='This will see if you have that movie (check: "movie")')
async def check_cmd(ctx, movie):
	found = False
	conn = sqlite3.connect('movies.db')
	c = conn.cursor()
	for row in c.execute('SELECT * FROM movies'):
		if movie.lower() == row[1].lower():
			found = True

	if found:
		response = "YA! WE HAVE IT!"
	else:
		response = "Not Found\n\n"
		response += "Similar:\n"
		count = 0
		for x in re.findall(r'\S+', movie):
			for row in c.execute('SELECT * FROM movies'):
				if x.lower() in row[1].lower():
					if count <= 20:
						response += row[1] + "\n"
						count += 1
	await ctx.send(response)

@bot.command(name='get:', help='This will download a movie (get: "movie")')
async def get_cmd(ctx, movie):
	
	response = movie
	await ctx.send(response)

@bot.command(name='send:', help='This will send you a movie to where you want (send: "movie")', pass_context=True)
async def send_cmd(ctx, movie):

	# await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

	file = open("test.txt", "r") 
	await ctx.send(file.read())

	# await commands.File("test.txt",filename="Hello",spoiler=False)

	# area=ctx.message.channel
	# await bot.send(area, r"test.txt",filename="Hello",content="Message test")

	# response = movie
	# await ctx.send(response)

print ("Bot running...")
bot.run(token)





