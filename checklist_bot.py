import sys
import os

import task_teamplate as task
import discord
from discord.ext import commands
from task_teamplate import Task
from storage.storage import Storage
import CFG

TOKEN = CFG.TOKEN


bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
	print("Greetings!")

# create new task for version
@bot.command(pass_context=True)
async def test(ctx, *arg):
	print(ctx.author)
	print(arg)
	st = Storage()
	new_task = Task(arg, len(st.content.keys()), ctx.author).get_task_as_dictionary()
	print("here")
	st.content[new_task["id_nb"]] = new_task
	print("here2")
	st.save_to_storage()
	print("here3")
	# print(ctx, arg)
	await ctx.send(new_task["msg"])

# registration new tags
@bot.command(pass_context=True)
async def reg(ctx, *, arg):
	print(ctx, arg)
	await ctx.send("registration")




help_row = """
	```$ - for version and titels for boards
@ - who should complete a task
# - labels and hashtags```
	"""
@bot.command(pass_context=True)
async def h(ctx):
	await ctx.send(help_row)

@bot.command(pass_context=True)
async def help(ctx):
	await ctx.send(help_row)


bot.run(TOKEN)
