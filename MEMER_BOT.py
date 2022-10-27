import random


import discord


import praw as praw

client = discord.Client()


reddit = praw.Reddit(client_id='your client id here',
                     client_secret='your client secret here',
                     user_agent='INFI')


@client.event
async def on_message(message):
    Channel_general = client.get_channel(773150585099911178)
    if message.content == ".meme":
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await message.channel.send(submission.url)


client.run("NzczMTQ5MDYxMjIxODQyOTU1.X6FBLA.cwaHyrXeeQNoIT8WrxtKNqTKijU")
