import re
import os
import random
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ur
import json
from googletrans import Translator
from urllib.request import Request, urlopen

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


'''
#use it in raspbian
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname("/home/pi/test_programs/python_bot/"), ".env"))
os.environ.update(dotenv)
TOKEN = dotenv["DISCORD_TOKEN"]
'''

bot = commands.Bot(command_prefix='+')

@bot.command(name='skills', help="skills of characters`")
async def nine_nine(ctx, code: str):
	if code == "Lucia Crimson Abyss":
		translator = Translator()
		my_url = "https://wiki.biligame.com/zspms/%E9%9C%B2%E8%A5%BF%E4%BA%9A%C2%B7%E6%B7%B1%E7%BA%A2%E4%B9%8B%E6%B8%8A"
		uClient = ur(my_url)
		page_html = uClient.read()
		uClient.close()
		page_soup = soup(page_html, "html.parser")
		containers_1 = page_soup.findAll("div", {"class": "tj-left"})
		x = containers_1[0].findAll("table", {"class": "wikitable"})
		y = x[0].findAll("td")
		count = 0
		st = ""
		for i in y:
			a = translator.translate(str(i.text))
			st += a.text + "\n"
			count += 1
			if count%3 == 0:
				await ctx.send("```{}```".format(st))
				st = ""



@bot.command(name='pics', help="pictures of characters ")
async def nine_nine(ctx, code: str):
	channel = bot.get_channel(615955484347990019)
	if code == "Lucia":
		names = """
		There are 3 types of Lucia battlesuits. Choose one by replying with the name...
1. Crimson Abyss
2. Dawn
3. Red Lotus
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Crimson Abyss":
				return m
			elif m.content == "Dawn":
				return m.content == "Dawn" and m.channel == channel
			elif m.content == "Red Lotus":
				return m.content == "Red Lotus" and m.channel == channel

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Crimson Abyss":
			file = discord.File('/home/ankanb49/STUFFFFFFF!!!!!!!!/python_works/discord bot/LuciaS.png', filename="LuciaS.png")
			embed = discord.Embed(title="Lucia Crimson Abyss", description="Lucia's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Dawn":
			file = discord.File('/home/ankanb49/STUFFFFFFF!!!!!!!!/python_works/discord bot/LuciaA.png', filename="LuciaA.png")
			embed = discord.Embed(title="Lucia Dawn", description="Lucia's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Red Lotus":
			file = discord.File('/home/ankanb49/STUFFFFFFF!!!!!!!!/python_works/discord bot/LuciaB.png', filename="LuciaB.png")
			embed = discord.Embed(title="Lucia Red Lotus", description="Lucia's B rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaB.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		#user = bot.get_user(514618549478883329)
		#await user.send(file=discord.File('/home/ankanb49/Downloads/luciaS2.png'))





@bot.command(name='nuke', help="search doujin ")
async def nine_nine(ctx, code: str):

	channel = bot.get_channel(615955484347990019)
	await channel.send("Another Man of Culture I guess..............( ͡° ͜ʖ ͡°)")
	link = "https://nhentai.net/g/" + code + "/"
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	page_soup = soup(webpage, "html.parser")
	containers_1 = page_soup.findAll("div", {"id": "info"})
	k = containers_1[0].text
	x = re.search("[0-9]+ pages", k)
	size = len(x[0])
	pageno = int(x[0][:size-6])
	title = containers_1[0].h1.text
	sub_title = containers_1[0].h2.text
	cover = link + "1/"
	req1 = Request(cover, headers={'User-Agent': 'Mozilla/5.0'})
	webpage1 = urlopen(req1).read()
	page_soup1 = soup(webpage1, "html.parser")
	containers_11 = page_soup1.findAll("div", {"class": "container"})
	img = containers_11[0].img["src"]
	embed = discord.Embed(title=title, description=str(sub_title) , color=0x00ff00)
	embed.set_thumbnail(url="https://i.redd.it/fkg9yip5yyl21.png")
	containers_2 = page_soup.findAll("div", {"class": "tag-container field-name"})
	ank = ''
	for i in containers_2:
		x = i.findAll("a")
		ank = ''
		for j in x:
			ank += j.text+","
		#ank = "\n"
		embed.add_field(name = "tmp", value=ank, inline=False)
    	
	embed.set_image(url=img)
	message = await channel.send(embed=embed)
	await message.add_reaction('\u23ee')
	await message.add_reaction('\u25c0')
	await message.add_reaction('\u25b6')
	await message.add_reaction('\u23ed')
	i = 1
	emoji = ''

	while True:
		def check1(reaction, user):
			if str(reaction.emoji) =='\u23ee':
				return user == ctx.author and str(reaction.emoji) == '\u23ee'
			if str(reaction.emoji)=='\u25c0':
				return user == ctx.author and str(reaction.emoji) == '\u25c0'
			if str(reaction.emoji) == '\u25b6':
				return user == ctx.author and str(reaction.emoji) == '\u25b6'
			if str(reaction.emoji) == '\u23ed':
				return user == ctx.author and str(reaction.emoji) == '\u23ed'
		try:
			reaction = await bot.wait_for('reaction_add', timeout= 120.0, check=check1)
		except asyncio.TimeoutError:
			#await message.remove_reaction('\u23ee')
			await channel.send("noob")
			break
		if str(reaction[0].emoji) == '\u23ee':
			i=1
			tmp = link+str(i)+'/'
			req1 = Request(tmp, headers={'User-Agent': 'Mozilla/5.0'})
			webpage1 = urlopen(req1).read()
			page_soup1 = soup(webpage1, "html.parser")
			containers_11 = page_soup1.findAll("div", {"class": "container"})
			pagei = containers_11[0].img["src"]
			page=discord.Embed(
        		title='Page '+str(i)+'/'+str(pageno),
        		colour=0x00ff00
    			)
			page.set_image(url=pagei)
			await message.edit(embed=embed)
		elif str(reaction[0].emoji) == '\u25c0':
			if i>1:
				i-=1
				tmp = link+str(i)+'/'
				req1 = Request(tmp, headers={'User-Agent': 'Mozilla/5.0'})
				webpage1 = urlopen(req1).read()
				page_soup1 = soup(webpage1, "html.parser")
				containers_11 = page_soup1.findAll("div", {"class": "container"})
				pagei = containers_11[0].img["src"]
				page=discord.Embed(
        			title='Page '+str(i)+'/'+str(pageno),
        			colour=0x00ff00
    				)
				page.set_image(url=pagei)
				await message.edit(embed=page)
		elif str(reaction[0].emoji) == '\u25b6':
			if i<pageno:
				i+=1
				tmp = link+str(i)+'/'
				req1 = Request(tmp, headers={'User-Agent': 'Mozilla/5.0'})
				webpage1 = urlopen(req1).read()
				page_soup1 = soup(webpage1, "html.parser")
				containers_11 = page_soup1.findAll("div", {"class": "container"})
				pagei = containers_11[0].img["src"]
				page=discord.Embed(
        			title='Page '+str(i)+'/'+str(pageno),
        			colour=0x00ff00
    				)
				page.set_image(url=pagei)
				await message.edit(embed=page)
		elif str(reaction[0].emoji) == '\u23ed':
			i = pageno
			tmp = link+str(i)+'/'
			req1 = Request(tmp, headers={'User-Agent': 'Mozilla/5.0'})
			webpage1 = urlopen(req1).read()
			page_soup1 = soup(webpage1, "html.parser")
			containers_11 = page_soup1.findAll("div", {"class": "container"})
			pagei = containers_11[0].img["src"]
			page=discord.Embed(
        		title='Page '+str(i)+'/'+str(pageno),
        		colour=0x00ff00
    			)
			page.set_image(url=pagei)
			await message.edit(embed=page)

bot.run(TOKEN)