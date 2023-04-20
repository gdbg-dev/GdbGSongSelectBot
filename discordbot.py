import asyncio
from operator import indexOf
from ssl import RAND_add
import discord
from discord.ext import commands
import interactions
from os import getenv
import traceback
import random
import database as db

token = getenv('DISCORD_BOT_TOKEN')
client = interactions.Client()
testchannel = int(getenv('TEST_CHANNEL'))
gdbgchannel = int(getenv('GDBG_CHANNEL'))

@interactions.slash_command(name="select", description="すべてのGdbG収録曲からランダムに1曲選出します。")
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
  
@interactions.slash_command(
    name="select_in",
    description="特定年のGdbG収録曲からランダムに1曲選出します。")
@interactions.slash_option(
            name="year",
            description="2009~2022までの年数4桁",
            opt_type=interactions.OptionType.INTEGER,
            min_value=2009,
            max_value=2022,
            required=True
        )
async def select_in(ctx: interactions.SlashContext,year:int):
  if(ctx.channel_id==testchannel)or(ctx.channel_id==gdbgchannel):
   if(2009<=year)and(year<=2022):#対応年度
     URLCommonStr="https://gdbg.tv/release/"
     albumnum=year-2009
     albumlist=[[7,7,6,6,6],[17,17,5],[12,12,11],[12,12,13],[12,12,12],[10,9,9,10],[10,10,10,11],[10,10,10,10],[20,20],[6,5,5,6,5,5,5,5],[10,9,10,10,10],[12,12,12,12],[12,12,12,12],[10,10,9,10,10]]
     thisalbum=albumlist[albumnum]
     albumsize=len(thisalbum)
     discpos=random.randint(1,albumsize)#ディスクきめ
     disc=thisalbum[discpos-1]
     track=random.randint(1,disc)
     String=URLCommonStr+str(year)+"-"+str(discpos)+"-"+str(track) 
     await ctx.send(str(year)+"年おすすめの楽曲はこちら。\nThis is the song(released in "+str(year)+") we recommend to you!\n"+String)
   else:#yearが範囲外
     await ctx.send("その年度のアルバムは存在しません。\nNo albums were released that year.",ephemeral=True)#送信者のみ表示

  else:#専用チャンネル範囲外
   await ctx.send("このチャンネルではコマンドの使用が許可されていません。\nThat command can use only #select_bot channel.",ephemeral=True)#送信者のみ表示



client.start(token)
