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
day=""
name=""
ndm=""

# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)

# @bot.command()
# async def hoge(ctx,name):
#  conn = db.connect() # このconnを通じて操作する
#  if conn.exists('リスト')==0:#リストがない場合
#   conn.set('リスト', name)
#  else:
#   str=conn.get('リスト')
#   str=str+name
#   conn.set('リスト', str)
#  await ctx.send(name+"を加えました〜")

# @bot.command()
# async def fuga(ctx,name):
#  str=conn.get('リスト')

@bot.command()
async def GdbGSelect(ctx):
   URLCommonStr="https://gdbg.tv/release/"
   year=random.randint(2009,2021)#2009~2021
   albumnum=year-2009
   albumlist=[[7,7,6,6,6],[17,17,5],[12,12,11],[12,12,13],[12,12,12],[10,9,9,10],[10,10,10,11],[10,10,10,10],[20,20],[6,5,5,6,5,5,5,5],[10,9,10,10,10],[12,12,12,12],[12,12,12,12]]
   thisalbum=albumlist[albumnum]
   albumsize=len(thisalbum)
   discpos=random.randint(1,albumsize)#ディスクの決定
   disc=thisalbum[discpos-1]
   track=random.randint(1,disc)

   String=URLCommonStr+str(year)+"-"+str(discpos)+"-"+str(track)


   await ctx.send("今回のおすすめはこちら\n"+String)














token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
