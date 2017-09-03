import discord
import asyncio
import random
import json
import os
import datetime
from discord import Embed

#File not included in git
from client_secret import key 

client = discord.Client()

from chatbot import Morty
x = Morty()

command_prefix = '.'

#---------------HELPMSG----------------#
helpmsg = (
'''**Here\'s a full list of my commands!**\n
**!flip** - Flips a digital coin! Choices: 1 and 0!\n**!8ball** `[text]` - Ask Rick a question and you may find your answer!
**!ping** - Pong\n**!echo** `[text]`\n**!chuck** - Random Chuck Norris jokes!\n**!lenny** - ( ͡° ͜ʖ ͡°)\n**!linux** - I'm not going to explain everything!'''
)
#--------------------------------------#

def msg_starts_with_ignorecase(msg, str):
    return msg.content.startswith(str.lower())

@client.event
async def on_ready():
    print('Logged in as:')
    print('Username: ', client.user.name)
    print('ID: ', client.user.id)
    print('------')

@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name='discord.gg/zCVfeGx'))
    #-Makes the bot not respond to itself!-
    if message.author == client.user:
        return

    if not message.content.startswith(command_prefix) and client.user in message.mentions:
        await client.send_message(message.channel, x.predict(message.content))
        return

    if message.content.startswith('!embed'):
        my_embed = Embed(title = 'Rock rocks', description = 'rock is a cool guy', color=0x00ff00)
        await client.send_message(message.channel, embed=my_embed)

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, helpmsg)

    elif message.content.startswith('!invite'):
        await client.send_message(message.channel, '**Invite me on your server:** https://goo.gl/C6CPEx')

    elif message.content.startswith('!flip'):
        flip = random.choice(['1', '0'])
        await client.send_message(message.channel, flip)

    elif message.content.startswith('!8ball'):
        ball = random.choice([' Maybe..', ' Who knows?', ' For sure!', ' Seems like YES!', ' Nooo.. I don\'t think so!', ' No.'])
        await client.send_message(message.channel, ':crystal_ball: ' + '`' + message.content[6:] + '`' + ball )

    elif message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Do you wanna play ping pong {0.author.mention}?'.format(message))
    elif message.content.startswith('!echo'):
        await client.send_message(message.channel, message.content[5:])

    elif message.content.startswith('!chuck'):
        chuck = random.choice([
        'When Chuck Norris was born he drove his mom home from the hospital.', 'Chuck Norris has a diary. It\'s called the Guinness Book of World Records.', 
        'Chuck Norris threw a grenade and killed 50 people, then it exploded.', 'Chuck Norris doesn\'t worry about high gas prices. His vehicles run on fear.',
        'Chuck Norris counted to infinity. Twice.'
        ])
        await client.send_message(message.channel, chuck)

    elif message.content.startswith('!lenny'):
        await client.send_message(message.channel, '( ͡° ͜ʖ ͡°)')

    elif message.content.startswith('!linux'):
        await client.send_message(message.channel,
    '''
    ``` < Linux Master Race >
            \   ^__^
             \  (oO)\_______
                (__)\       )\/\/
                 U  ||----w |
                    ||     ||```
    ''')

client.run(key)
#NOTES
# '{0.author.mention}'.format(message) - Mentions user!
# message.content - Sends user's input!
# [X:] - Skips a certain number of letters/numbers/characters where X is the number to be skipped!
