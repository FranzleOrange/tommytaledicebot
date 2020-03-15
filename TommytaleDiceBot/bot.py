import os
import discord
import random

TOKEN="token"

#dice imgs / immagini dadi
d4s = ["img/d4-1.png", "img/d4-2.png", "img/d4-3.png", "img/d4-4.png"]

d6s = ["img/d6-1.png", "img/d6-2.png", "img/d6-3.png", "img/d6-4.png", "img/d6-5.png", "img/d6-6.png"]

d8s = ["img/d8-1.png", "img/d8-2.png", "img/d8-3.png", "img/d8-4.png", "img/d8-5.png", "img/d8-6.png", "img/d8-7.png", "img/d8-8.png"]

d10s = ["img/d10-1.png", "img/d10-2.png", "img/d10-3.png", "img/d10-4.png", "img/d10-5.png", "img/d10-6.png", "img/d10-7.png",
        "img/d10-8.png", "img/d10-9.png", "img/d10-0.png"]

d12s = ["img/d12-1.png", "img/d12-2.png", "img/d12-3.png", "img/d12-4.png", "img/d12-5.png", "img/d12-6.png", "img/d12-7.png",
        "img/d12-8.png", "img/d12-9.png", "img/d12-10.png", "img/d12-11.png", "img/d12-12.png"]

d20s = ["img/d20-1.png", "img/d20-2.png", "img/d20-3.png", "img/d20-4.png", "img/d20-5.png", "img/d20-6.png", "img/d20-7.png",
        "img/d20-8.png", "img/d20-9.png", "img/d20-10.png", "img/d20-11.png", "img/d20-12.png", "img/d20-13.png", "img/d20-14.png",
        "img/d20-15.png", "img/d20-16.png", "img/d20-17.png", "img/d20-18.png", "img/d20-19.png", "img/d20-20.png"]

d100s = ["img/d100-00.png", "img/d100-10.png", "img/d100-20.png", "img/d100-30.png", "img/d100-40.png", "img/d100-50.png",
        "img/d100-60.png", "img/d100-70.png", "img/d100-80.png", "img/d100-90.png", ]

#those are the actual dice rollers / i generatori di dadi effettvi
def gen_d20():
    number = random.randint(0, 19)
    return d20s[number]
def gen_d6():
    number = random.randint(0, 5)
    return d6s[number]
def gen_d8():
    number = random.randint(0, 7)
    return d8s[number]
def gen_d10():
    number = random.randint(0, 9)
    return d10s[number]
def gen_d4():
    number = random.randint(0, 3)
    return d4s[number]
def gen_d100():
    number = random.randint(0, 9)
    return d100s[number]
def gen_d12():
    number = random.randint(0, 11)
    return d12s[number]

def run():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
            )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        #checks for the dice rolls and calls the relative function / controlla per i roll dei dadi tramite i comandi !d<> e chiama la relativa funzione
        if message.content.startswith('!d20'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d20()))
        elif message.content.startswith('!d4'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d4()))
        elif message.content.startswith('!d6'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d6()))
        elif message.content.startswith('!d8'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d8()))
        elif message.content.startswith('!d10'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d10()))
        elif message.content.startswith('!d12'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d12()))
        elif message.content.startswith('!d%'):
            await message.channel.send("Il dado ha per te deciso:", file=discord.File(gen_d100()))

    client.run(TOKEN)
run()