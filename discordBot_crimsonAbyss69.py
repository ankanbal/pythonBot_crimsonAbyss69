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
import mysql.connector

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

@bot.command(name='skills', help="skills of characters")
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


@bot.command(name='arms', help='quick summary of arms')
async def nine_nine(ctx):
	channel = bot.get_channel(615955484347990019)
	names = """
1. Shadow Strike-Reverse
2. Zero Degree Calibration
3. Chimera Retrograde
4. Zero Form
5. Sirius
6. Red Sakura
7. Ray Mill
8. God Giver
9. Dragon Wind
10. Wei Zi
11. Soul Slayer
12. Frenzied Fusion Canon
13. Leitning
14. Great God Power
15. Calender
16. Red Lotus Fanatic
17. Machine Rhyme
18. Wolf Eater
19. Nuclear-based red dragon
20. Sain
21. Pitch Black"""
	choice_embed = discord.Embed(title = "Following are the weapons in Punishing Gray Raven which come under 6-star rarity:", description = names)
	await channel.send(embed=choice_embed)
	def check(m):
		return m
	msg = await bot.wait_for('message', check=check)
	title = msg.content
	mydb = mysql.connector.connect(
    	host="localhost",
    	user="root",
    	passwd="",
    	database="Punishing Gray Raven",
	  		auth_plugin='mysql_native_password'
	)
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM Arms where Name = '{}';".format(title))
	myresult = mycursor.fetchall()
	name = myresult[0][0]
	link = myresult[0][1]
	uClient = ur(link)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	con = page_soup.findAll("table", {"class": "wikitable"})
	ans = con[0].findAll("img", {"class":"img-kk"})
	url = ans[0]["src"]
	wtype = myresult[0][2]
	rare = myresult[0][3]
	rr = ""
	for i in range(rare):
		rr += "✰"
	skill = myresult[0][4]
	embed = discord.Embed(title=name, description=" Details", color=0x00ff00)
	embed.set_thumbnail(url=url)
	embed.add_field(name="Type", value=wtype, inline=False)
	embed.add_field(name="Rarity", value=rr, inline=False)
	embed.add_field(name="Skills", value=skill, inline=False)
	await channel.send(embed=embed)


@bot.command(name='pics', help="pictures of characters ")
async def nine_nine(ctx, code: str):
	channel = bot.get_channel(615955484347990019)
	if code == "Lucia":
		names = """
		There are 3 types of Lucia battlesuits. Choose one by replying with the name...
1. Lucia Crimson Abyss
2. Lucia Dawn
3. Lucia Red Lotus
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Lucia Crimson Abyss":
				return m
			elif m.content == "Lucia Dawn":
				return m
			elif m.content == "Lucia Red Lotus":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Lucia Crimson Abyss":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/lucia/LuciaS.png', filename="LuciaS.png")
			embed = discord.Embed(title="Lucia Crimson Abyss", description="Lucia's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Lucia Dawn":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/lucia/LuciaA.png', filename="LuciaA.png")
			embed = discord.Embed(title="Lucia Dawn", description="Lucia's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Lucia Red Lotus":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/lucia/LuciaB.png', filename="LuciaB.png")
			embed = discord.Embed(title="Lucia Red Lotus", description="Lucia's B rank character", color=0x00ff00)
			embed.set_image(url="attachment://LuciaB.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Nanami":
		names = """
		There are 2 types of Lucia battlesuits. Choose one by replying with the name...
1. Nanami Storm
2. Nanami Pulse
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Nanami Storm":
				return m
			elif m.content == "Nanami Pulse":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Nanami Storm":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/nanami/NanamiA.png', filename="NanamiA.png")
			embed = discord.Embed(title="Nanami Storm", description="Nanami's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://NanamiA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Nanami Pulse":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/nanami/NanamiS.png', filename="NanamiS.png")
			embed = discord.Embed(title="Nanami Pulse", description="Nanami's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://NanamiS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Liv":
		names = """
		There are 3 types of Liv battlesuits. Choose one by replying with the name...
1. Liv Hope
2. Liv Streamer
3. Liv Eclipse
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Liv Hope":
				return m
			elif m.content == "Liv Streamer":
				return m
			elif m.content == "Liv Eclipse":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Liv Hope":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/liv/LivS.png', filename="LivS.png")
			embed = discord.Embed(title="Liv Hope", description="Liv's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://LivS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Liv Streamer":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/liv/LivA.png', filename="LivA.png")
			embed = discord.Embed(title="Liv Streamer", description="Liv's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://LivA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Liv Eclipse":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/liv/LivB.png', filename="LivB.png")
			embed = discord.Embed(title="Liv Eclipse", description="Liv's B rank character", color=0x00ff00)
			embed.set_image(url="attachment://LivB.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Lee":
		names = """
		There are 2 types of Lee battlesuits. Choose one by replying with the name...
1. Lee Ghostfire
2. Lee Random numbers
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Lee Ghostfire":
				return m
			elif m.content == "Lee Random numbers":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Lee Random numbers":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/lee/LeeS.png', filename="LeeS.png")
			embed = discord.Embed(title="Lee Random numbers", description="Lee's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://LeeS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Lee Ghostfire":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/lee/LeeA.png', filename="LeeA.png")
			embed = discord.Embed(title="Lee Ghostfire", description="Lee's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://LeeA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Kamui":
		names = """
		There are 2 types of Kamui battlesuits. Choose one by replying with the name...
1. Kamui Heavy power
2. Kamui Dark Energy
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Kamui Heavy power":
				return m
			elif m.content == "Kamui Dark Energy":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Kamui Dark Energy":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/kamui/KamuiS.png', filename="KamuiS.png")
			embed = discord.Embed(title="Kamui Dark Energy", description="Kamui's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://KamuiS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Kamui Heavy power":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/kamui/KamuiA.png', filename="KamuiA.png")
			embed = discord.Embed(title="Kamui Heavy power", description="Kamui's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://KamuiA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Karen":
		names = """
		There are 2 types of Karenina battlesuits. Choose one by replying with the name...
1. Karenina Amber
2. Karenina Burst
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Karenina Amber":
				return m
			elif m.content == "Karenina Burst":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Karenina Amber":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/karen/KarenS.png', filename="KarenS.png")
			embed = discord.Embed(title="Karenina Amber", description="Karen's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://KarenS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Karenina Burst":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/karen/KarenA.png', filename="KarenA.png")
			embed = discord.Embed(title="Karenina Burst", description="Karen's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://KarenA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Watanabe":
		names = """
		There are 2 types of Watanabe battlesuits. Choose one by replying with the name...
1. Watanabe NightBlade
2. Watanabe Phoenix Star
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Watanabe NightBlade":
				return m
			elif m.content == "Watanabe Phoenix Star":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Watanabe NightBlade":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/watanabe/WataA.png', filename="WataA.png")
			embed = discord.Embed(title="Watanabe NightBlade", description="Watanabe's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://WataA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Watanabe Phoenix Star":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/watanabe/WataA2.png', filename="WataA2.png")
			embed = discord.Embed(title="Watanabe Phoenix Star", description="Watanabe's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://WataA2.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Bianca":
		names = """
		There are 2 types of Bianca battlesuits. Choose one by replying with the name...
1. Bianca Zero
2. Bianca Truth
		"""
		choice_embed = discord.Embed(title = names)
		await channel.send(embed=choice_embed)
		def check(m):
			if m.content == "Bianca Zero":
				return m
			elif m.content == "Bianca Truth":
				return m

		msg = await bot.wait_for('message', check=check)
		if msg.content == "Bianca Truth":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/bianca/BiancaS.png', filename="BiancaS.png")
			embed = discord.Embed(title="Bianca Truth", description="Bianca's S rank character", color=0x00ff00)
			embed.set_image(url="attachment://BiancaS.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
		elif msg.content == "Bianca Zero":
			file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/bianca/BiancaA.png', filename="BiancaA.png")
			embed = discord.Embed(title="Bianca Zero", description="Bianca's A rank character", color=0x00ff00)
			embed.set_image(url="attachment://BiancaA.png")
			embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
			await channel.send(file=file, embed=embed)
	elif code == "Ayla":
		file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/ayla/AylaA.png', filename="AylaA.png")
		embed = discord.Embed(title="Ayla ", description="Ayla's A rank character", color=0x00ff00)
		embed.set_image(url="attachment://AylaA.png")
		embed.add_field(name="Comments", value="Don't fap to her, she will cut ur nut", inline=False)
		await channel.send(file=file, embed=embed)
	elif code == "Sophia":
		file = discord.File('/home/ankanb49/STUFFFFFFF/python_works/discord bot/sophia/SophiaA.png', filename="SophiaA.png")
		embed = discord.Embed(title="Sophia", description="Sophia's A rank character", color=0x00ff00)
		embed.set_image(url="attachment://LuciaS.png")
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