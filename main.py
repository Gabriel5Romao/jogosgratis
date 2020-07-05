import discord
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.indiegamebundles.com/category/free/')  # Site da obtenção dos requests
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')

titulos = soup.find_all(class_ = 'entry-title td-module-title')    # Forma que encontrei para encontrar o título dos jogos grátis

lista_titulos = []  # Lista que guarda os títulos das notícias, consequentemente os jogos 

for i in range(1,10):
    lista_titulos.append((str(titulos[i]))[(str(titulos[i]).find('title=') + 7):str(titulos[i]).find('">',40)])  # Forma que encontrei para encontrar os títulos das notícias

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>help'):
        await message.channel.send('>help -> Exibe a lista de comandos do BOT. \n>jogos -> Exibe a lista de jogos grátis\nhttp://github.com/gabrielromao5')

    if message.content.startswith('>jogos'):   # Leitura do comando, para devolver umas lista com 9 jogos...
        await message.channel.send('@everyone')
        for i in range(0, len(lista_titulos)):
            await message.channel.send(str(lista_titulos[i]))
   
client.run('token')

"""
Esse é uma versão 0.1 de um BOT para discord que anuncia jogos grátis. Não poderei mantê-lo, pois tenho que estudar outras coisas. Fique a vontade para melhorar o código.
GITHUB: github.com/gabrielromao5
Entre no server do discord(só diversão): https://discord.gg/P7DAQgs
"""