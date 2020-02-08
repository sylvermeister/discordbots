#!/usr/local/bin/python3

# -*- coding: utf8 -*-

import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  """
  message is from the sender (remnant guild members)
  client is the bot (remnant-bot#9970)
  """
  print('message is from %s' % message.channel)
  print('getting channel info: %s' % client.get_channel(674876386623881246))
  print('client user: %s' % client.user)
  print('message author: %s' % message.author)
  
  # avoid processing message from bot
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run('Njc1NTU4ODk4OTYyMzk5Mjcy.Xj48Dw.Z6Fl-H6yoLtMNOXseO7r27jJTBM')