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

bot.run(TOKEN)
