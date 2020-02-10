#!/usr/local/bin/python3

# -*- coding: utf8 -*-

import discord

from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX=("$")
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
  print ("------------------------------------")
  print ("Bot Name: %s" % bot.user.name)
  print ("Bot ID: %s" % bot.user.id)
  print ("Discord Version: %s" % discord.__version__)
  print ("------------------------------------")

@bot.command(pass_context=True)
async def smvp(ctx):
  message = ctx.message
  channel = message.channel
  print("from: %s" % channel)
  print("message: %s" % message)
  print("user: %s" % bot.user)
  print("message author: %s" % message.author)
  if message.author == bot.user:
    return

  await channel.send("Hello!")

bot.run("Njc1NTU4ODk4OTYyMzk5Mjcy.Xj6_Bg.8OvcynpH-Hk_a8XoFuRhgPtiuZo")