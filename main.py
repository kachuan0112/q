import discord
from discord.ext import commands
import asyncio
import os

from discord.ext import commands
from discord_components import *
from discord_slash import SlashCommand
from discord import embeds
from discord import message
from discord import activity

#----------------------------------------------------#

intents = discord.Intents.default()
intents.members = True

#----------------------------------------------------#

bot = commands.Bot(command_prefix= "=" ,case_insensitive=True, description="not gonna use help commands")

bot.remove_command("help")
#----------------------------------------------------#
@bot.event
async def on_ready():
    print("--------------------------------------------")
    print(f"{bot.user.name} is ready to use".format(bot))
    print("--------------------------------------------")
    activity4=discord.Activity(name="=help" , type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity4)

#---------------------------------------------------#

initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
            bot.load_extension(extension)
            print(extension)

#---------------------------------------------------#

slash = SlashCommand(bot, sync_commands=True)

#---------------------------------------------------#

DiscordComponents(bot)

#---------------------------------------------------#

@bot.command(name="help" , description="See what command you can use")
async def help(ctx):
    embed=(discord.Embed(title="**BOT COMMANDS**" , description="**See All Commands in here**" , color=discord.Color.blurple())
    .add_field(name='**Music Commands ! **', value="`help` , `play` , `skip` , `loop` , `forceskip` , `queue` , `summon` , `search` , `stop` , `pause` , `resume` , `join` , `leave`",inline=False)
    .add_field(name="**Other fun commands !** " , value=" `ping` , `lmao` , `lmfao`" , inline=False)
    .add_field(name="**Other Commands ! **" , value="`help` , `botstop` , `invite`" , inline=False)
    .set_footer(text="=help will show this commands. ",icon_url="https://cdn.discordapp.com/emojis/800566172600893450.gif?size=96")
    )

    await ctx.send(embed=embed)

@slash.slash(name="help" , description="See what command you can use")
async def help(ctx):
    embed=(discord.Embed(title="**BOT COMMANDS**" , description="**See All Commands in here**" , color=discord.Color.blurple())
    .add_field(name='**Music Commands ! **', value="`help` , `play` , `skip` , `loop` , `forceskip` , `queue` , `summon` , `search` , `stop` , `pause` , `resume` , `join` , `leave`",inline=False)
    .add_field(name="**Other fun commands !** " , value="`ping` , `lmao` , `lmfao`" , inline=False)
    .add_field(name="**Other Commands ! **" , value="`help` , `botstop` , `invite`" , inline=False)
    .set_footer(text="=help will show this commands. ",icon_url="https://cdn.discordapp.com/emojis/800566172600893450.gif?size=96")
    )
    await ctx.send(embed=embed)

@bot.command(name="invite")
async def invite(ctx):
    embed=(discord.Embed(title="**Invite link**" , 
        description="Please invite me QQ " ,
        color=discord.Color.blurple())
)
    await ctx.send(embed=embed , 
    components = [
        Button(style=ButtonStyle.URL , label="Invite me !" , url="https://discord.com/api/oauth2/authorize?client_id=865454711233708033&permissions=519326105152&scope=bot")

    ]

)

@slash.slash(name="invite" , description="If you want to invte me use this commands!")
async def invite(ctx):
    embed=(discord.Embed(title="**Invite link**" , 
        description="Please invite me QQ " ,
        color=discord.Color.blurple())
)
    await ctx.send(embed=embed , 
    components = [
        Button(style=ButtonStyle.URL , label="Invite me !" , url="https://discord.com/api/oauth2/authorize?client_id=865454711233708033&permissions=519326105152&scope=bot")

    ]

)

bot.run(TOKEN)
