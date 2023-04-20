import asyncio
from operator import indexOf
from ssl import RAND_add
import discord
from discord.ext import commands
from interactions import Client, Intents, slash_command
from os import getenv
import traceback
import random
import database as db

intents = discord.Intents.all()
token = getenv('DISCORD_BOT_TOKEN')
bot = Client(intents=Intents.DEFAULT)
testchannel = int(getenv('TEST_CHANNEL'))
gdbgchannel = int(getenv('GDBG_CHANNEL'))

@slash_command(name="select", description="すべてのGdbG収録曲からランダムに1曲選出します。")
async def select(ctx: interactions.SlashContext):
  if(ctx.channel_id==testchannel)or(ctx.channel_id==gdbgchannel):
   URLCommonStr="https://gdbg.tv/release/"
   year=random.randint(2009,2022)#2009~2022
   albumnum=year-2009
   albumlist=[[7,7,6,6,6],[17,17,5],[12,12,11],[12,12,13],[12,12,12],[10,9,9,10],[10,10,10,11],[10,10,10,10],[20,20],[6,5,5,6,5,5,5,5],[10,9,10,10,10],[12,12,12,12],[12,12,12,12],[10,10,9,10,10]]
   thisalbum=albumlist[albumnum]
   albumsize=len(thisalbum)
   discpos=random.randint(1,albumsize)#ディスクきめ
   disc=thisalbum[discpos-1]
   track=random.randint(1,disc)

   String=URLCommonStr+str(year)+"-"+str(discpos)+"-"+str(track)
   await ctx.send("今回のおすすめはこの楽曲。\nThis is the song we recommend to you!\n"+String)
  else:
   await ctx.send("このチャンネルではコマンドの使用が許可されていません。\nThat command can use only #XXX channel.",ephemeral=True)#送信者のみ表示
  
@slash_command(
    name="select_in",
    description="特定年のGdbG収録曲からランダムに1曲選出します。",
    options = [
        interactions.Option(
            name="year",
            description="2009~2022までの年数4桁",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
 )
async def select_in(ctx: interactions.SlashContext,year:str):
  if(ctx.channel_id==testchannel)or(ctx.channel_id==gdbgchannel):
   if(2009<=int(year))and(int(year)<=2022):#対応年度
     URLCommonStr="https://gdbg.tv/release/"
     albumnum=int(year)-2009
     albumlist=[[7,7,6,6,6],[17,17,5],[12,12,11],[12,12,13],[12,12,12],[10,9,9,10],[10,10,10,11],[10,10,10,10],[20,20],[6,5,5,6,5,5,5,5],[10,9,10,10,10],[12,12,12,12],[12,12,12,12],[10,10,9,10,10]]
     thisalbum=albumlist[albumnum]
     albumsize=len(thisalbum)
     discpos=random.randint(1,albumsize)#ディスクきめ
     disc=thisalbum[discpos-1]
     track=random.randint(1,disc)
     String=URLCommonStr+str(year)+"-"+str(discpos)+"-"+str(track) 
     await ctx.send(year+"年おすすめの楽曲はこちら。\nThis is the song(released in "+year+") we recommend to you!\n"+String)
   else:#yearが範囲外
     await ctx.send("その年度のアルバムは存在しません。\nNo albums were released that year.",ephemeral=True)#送信者のみ表示

  else:#専用チャンネル範囲外
   await ctx.send("このチャンネルではコマンドの使用が許可されていません。\nThat command can use only #XXX channel.",ephemeral=True)#送信者のみ表示



bot.start(token)
