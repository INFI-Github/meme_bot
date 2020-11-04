import random

import aiohttp
import discord
import time

import praw as praw

intents = discord.Intents.all()
client = discord.Client(intents=intents)


reddit = praw.Reddit(client_id='JQGiY5EzRhDwwg',
                     client_secret='f4nFjO6XLJtHjt7MJ3eIRwxg9x463Q',
                     user_agent='INFI_MEMES')


@client.event
async def on_message(message):
    Channel_general = client.get_channel(773150585099911178)
    if message.content == ".meme":
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await Channel_general.send(submission.url)


client.run("NzczMTQ5MDYxMjIxODQyOTU1.X6FBLA.cwaHyrXeeQNoIT8WrxtKNqTKijU")