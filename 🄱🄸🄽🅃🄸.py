from nextcord import (
    Intents
)
from nextcord.ext import commands
from os import listdir,system
from asyncio import run
from Config import Config
from utils.Cybersafeapi import Cybersafeapi
from pystyle import Colors, Colorate

from colorama import Fore, Back, Style
bot = commands.Bot(
    command_prefix=Config().Get()["commnadPrefix"],
    help_command=None,
    intents=Intents.all(),
    case_insensitive=True,
    strip_after_prefix=True
)

async def loadCogs():
    for folder in listdir('cogs'):
        for file in listdir(f'./cogs/{folder}'):
            if file.endswith('.py'):
                try:
                    bot.load_extension(f'cogs.{folder}.{file[:-3]}')
                    print(f'Successfully to load {file[:-3]}')
                except Exception as error:
                    print(f'Fail to load {file[:-3]} -> {str(error)}')


apics = Cybersafeapi(Config().Get()["configweb"]["username"],Config().Get()["configweb"]["password"])
cslogin = apics.Login()

system("cls||clear")
system("title cybersafe bot")
print(Colorate.Horizontal(Colors.yellow_to_red, '''

            
██████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║  ██║    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║  ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                         🄲🅁🄴🄰🅃🄴🄳｡^‿^｡ 🄱🅈 ｡^‿^｡🄽🄰🄷🄸🄳.🄹🅁                                           
''', 1))
print(f'''
                {Fore.RED}─══════════════════════════{Fore.YELLOW}ቐቐ{Fore.RED}══════════════════════════─
                
                            {Fore.BLUE}Add points at store.cyber-safe.pro
                                {Fore.YELLOW}contact {Fore.LIGHTWHITE_EX}fb.me/cybersafe01
                                            {Fore.RED}and
                                {Fore.LIGHTWHITE_EX}https://{Fore.YELLOW}discord.gg{Fore.LIGHTWHITE_EX}/SHEUu9DBtG
                
                {Fore.RED}─══════════════════════════{Fore.YELLOW}ቐቐ{Fore.RED}══════════════════════════─
''')
if (__name__ == '__main__'):
    if cslogin.json()["status"] != "success":
        exit("login failed")

    Config().updateConfig("configweb","token",value_to_update=cslogin.json()["result"]["token"])

    run(loadCogs())
    token = Config().Get()["botToken"]
    bot.run(token)