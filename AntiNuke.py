import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands import bot
from colorama import init, Fore, Back, Style
import datetime
init(convert=True)
bot = commands.Bot(command_prefix='!')

#Crea un bot, accede a OAuth2 y metelo al servidor en el que quieras limpiar los canales (Consedele permisos de Administrador).
tokentorun = "token"
channeltodelete = "nuke" #cambiar al nombre de los canales que desees borrar.
roletodelete = "get rolespammed" #cambiar al nombre de los roles que deseas borrar.

print(f"""
{Fore.CYAN}

 █████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗██╗  ██╗███████╗
██╔══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██║ ██╔╝██╔════╝
███████║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║█████╔╝ █████╗  
██╔══██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  
██║  ██║██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝██║  ██╗███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                 
!channelclean or !roleclean to clean!
""")

async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name="Cleaner bot.", url="https://www.twitch.tv/discord"))
    print("Ready to clean.")

@bot.command()
async def roleclean(ctx):
    await ctx.message.delete()
    for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                try:
                    await role.delete()
                except discord.HTTPException as e:
                    print(f"Failed to delete role: {role.name}. Likely missing perms")
                    continue
                else:
                    currentDT = datetime.datetime.now()
                    hour = str(currentDT.hour)
                    minute = str(currentDT.minute)
                    second = str(currentDT.second)
                    print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Deleted Role: {role.name}")
    print(f"\n\n{Fore.CYAN}Cleared all roles called '{roletodelete}'")


@bot.command()
async def channelclean(ctx):
    await ctx.message.delete()
    for channel in ctx.message.guild.channels:
        if channel == "Text Channels":
            continue
        elif channel == "Voice Channels":
            continue
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Channel Deleted - {channel.name}")




    print(f"\n\n{Fore.CYAN}Cleared all channels called '{channeltodelete}',be careful when adding unknown bots in the future.\nBe especially careful if the bot is in few servers,requires permissions \nor if the person who requested for it to be added seems desperate.\nAny bot with admin could've easily mass banned and wiped your server,\nthat I have no cure for, so do look out in the future!\n\nGood luck and I'm happy I was able to help!")

bot.run(tokentorun)
