import sys
import os
import CFG


import task_teamplate as task
import discord
from discord.ext import commands
from task_teamplate import Task
from storage.storage import Storage
from discord_tables.tables import DiscordTable

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
	# st = Storage()
	author = str(ctx.author.name) + "#" + str(ctx.author.discriminator)
	new_task = Task(arg, author).get_task_as_dictionary()
	print("here3")
	# print(ctx, arg)
	await ctx.send(new_task["msg"])

# show tables by its name
@bot.command(pass_context=True)
async def show_table(ctx, *, arg):
	print(ctx, arg)
	if len(arg) == 0:
		await ctx.send("I need a name of the table")
	table_name = ""
	for w in arg:
		if w == " " or w == " ":
			break
		table_name += str(w)
	print("table name ",table_name)
	st = Storage()
	unformated_tasks = st.get_table(table_name)
	print("unforameted tasks\n",unformated_tasks)
	if unformated_tasks:
		table = DiscordTable(unformated_tasks)
		rows = table.get_table()
		print("table after formatting\n", table )
		print("row\n")
		print(rows)
		print("\n")
	await ctx.send(rows)


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
