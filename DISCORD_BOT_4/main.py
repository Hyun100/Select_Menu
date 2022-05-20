import discord
from discord.ui import View, Select
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')
token = "You need your bot token!"

@bot.event
async def on_ready():
    print('봇으로 로그인에 성공했어요!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("고민 중..."))

@bot.command()
async def 셀렉트메뉴호출(ctx):
    select = Select(
        placeholder = "선택되지 않음",
        options = [
        discord.SelectOption(label="dropdown 1", description="1번 설명"),
        discord.SelectOption(label="dropdown 2", description="2번 설명"),
        discord.SelectOption(label="dropdown 3", description="3번 설명")
    ])

    async def my_callback(interaction):
        if select.values[0] == "dropdown 1":
            await interaction.response.send_message("1번 선택함")
        elif select.values[0] == "dropdown 2":
            await interaction.response.send_message("2번 선택함")
        elif select.values[0] == "dropdown 3":
            await interaction.response.send_message("3번 선택함!")
            
    select.callback = my_callback
    view = View()
    view.add_item(select)

    await ctx.send("셀렉트메뉴 호출!", view = view)

bot.run(token)