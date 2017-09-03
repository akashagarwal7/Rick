import discord
import asyncio
import random
import json
import os
import datetime

client = discord.Client()

from chatbot import Morty
x = Morty()

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
    #Variables for Messages
#     ball = random.choice([' Maybe..', ' Who knows?', ' For sure!', ' Seems like YES!', ' Nooo.. I don\'t think so!', ' No.'])
#     flip = random.choice(['1', '0'])
#     #---------CHUCK-------------------
#     chuck = random.choice([
# 'When Chuck Norris was born he drove his mom home from the hospital.', 'Chuck Norris has a diary. It\'s called the Guinness Book of World Records.', 
# 'Chuck Norris threw a grenade and killed 50 people, then it exploded.', 'Chuck Norris doesn\'t worry about high gas prices. His vehicles run on fear.',
# 'Chuck Norris counted to infinity. Twice.'
# ])
#     ##

#     #---------HELPMSG-----------------
#     helpmsg = (
# '''**Here\'s a full list of my commands!**\n
# **!flip** - Flips a digital coin! Choices: 1 and 0!\n**!8ball** `[text]` - Ask Rick a question and you may find your answer!
# **!ping** - Pong\n**!echo** `[text]`\n**!chuck** - Random Chuck Norris jokes!\n**!lenny** - ( ͡° ͜ʖ ͡°)\n**!linux** - I'm not going to explain everything!'''
# )
    ##

    # Embed example
    from discord import Embed

    my_embed = Embed(title = 'Rock rocks', description = 'rock is a cool guy', color=0x00ff00)

    if message.content.startswith('!embed'):
        await client.send_message(message.channel, embed=my_embed)
        return

    # End of example
    
    await client.send_message(message.channel, x.predict(message.content))
    return # Don't need to execute code below this right now, it needs to be cleaned and the logic needs to be changed as well

    #Misc Messages
    if message.content.startswith('help'):
        await client.send_message(message.channel, helpmsg)
    elif message.content.startswith('lol'):
        await client.send_message(message.channel, 'What?')
    elif message.content.startswith('nothing'):
        await client.send_message(message.channel, 'Ok')
    elif message.content.startswith('beep'):
        await client.send_message(message.channel, 'boop')
    elif message.content.startswith('?'):
        await client.send_message(message.channel, '?')
    elif message.content.startswith('Where are you from?'):
        await client.send_message(message.channel, 'I\'m from a strange planet called "Earth"!')
    elif message.content.startswith('wtf'):
        await client.send_message(message.channel, 'What\'s wrong?')
    elif message.content.startswith('test') or message.content.startswith('Test'):
        await client.send_message(message.channel, 'I\'m Alive!')
    elif message.content.startswith('Rick, do you have protection?'):
        await client.send_message(message.channel, 'Yes, I\'m using Norton Antivirus..')
    ##

    #Messages with Prefix
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, helpmsg)
    elif message.content.startswith('!invite'):
        await client.send_message(message.channel, '**Invite me on your server:** https://goo.gl/C6CPEx')
    elif message.content.startswith('!flip'):
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!8ball'):
        await client.send_message(message.channel, ':crystal_ball: ' + '`' + message.content[6:] + '`' + ball )
    elif message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Do you wanna play ping pong {0.author.mention}?'.format(message))
    elif message.content.startswith('!echo'):
        await client.send_message(message.channel, message.content[5:])
    elif message.content.startswith('!chuck'):
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

client.run('MzQ5NjY2NjU3MzY4NTM5MTQ3.DH4z-Q.8Jhn1GNA4Bv2jpeqPNC8A6BQrBg')
#NOTES
# '{0.author.mention}'.format(message) - Mentions user!
# message.content - Sends user's input!
# [X:] - Skips a certain number of letters/numbers/characters where X is the number to be skipped!
