import asyncio
from operator import indexOf
from ssl import RAND_add
import discord
from discord.ext import commands
from os import getenv
import traceback
import random
import database as db

bot = commands.Bot(command_prefix='!')

@bot.command()
async def GdbGSelect(ctx):
  if(ctx.message.channel.id ==='1013711594804498462'):
   URLCommonStr="https://gdbg.tv/release/"
   year=random.randint(2009,2021)#2009~2021
   albumnum=year-2009
   albumlist=[[7,7,6,6,6],[17,17,5],[12,12,11],[12,12,13],[12,12,12],[10,9,9,10],[10,10,10,11],[10,10,10,10],[20,20],[6,5,5,6,5,5,5,5],[10,9,10,10,10],[12,12,12,12],[12,12,12,12]]
   thisalbum=albumlist[albumnum]
   albumsize=len(thisalbum)
   discpos=random.randint(1,albumsize)#ディスクきめ
   disc=thisalbum[discpos-1]
   track=random.randint(1,disc)

   String=URLCommonStr+str(year)+"-"+str(discpos)+"-"+str(track)


   await ctx.send("今回のおすすめはこの楽曲。\nThis is the song We recommend to you!\n"+String)
  else:
   await ctx.send("このチャンネルではコマンドの使用が許可されていません。That command can use only #XXX channel.")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
