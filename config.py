import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("TOKEN")
client_id = 901058816743989249
guild_id = 897965052278214728
prefix = '.'
leadbotdev = 897965647487729665
afkvc = 901082852567953418
error = "https://cdn.discordapp.com/attachments/796711597078347816/901847527362547722/error.png"
question = "https://media.discordapp.net/attachments/796711597078347816/917762066956296242/question.png"
welcomeChannel = 897965052278214731
verifyChannel = 898247739392004126
rulesChannel = 897965075334320168
verifycode = '164'
verifyrole = 898231182502817792
default_footer= "© Iris"
guildlogs = 906984963478540288
verifylogs = 901583672866639902
messagedeletelogs = 901585744173346938
messageeditlogs = 901602135970566164
banlogs = 901624378205282334
unbanlogs = 901630286197055518
kicklogs = 901937012528001064
joinlogs = 901636677062258738
leavelogs = 901632871666683946
channellogs = 901647506541281350
rolelogs = 906951097212600411
voicechannellogs = 901789906328760330
loadunloadreloadlogs = 901892552188362763
announcementlogs = 902201673320104027