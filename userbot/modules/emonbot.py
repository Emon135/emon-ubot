from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu burik`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah goyangan kamu kurang asik 😊`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi boleh minta pap nya Kk..**")


@register(outgoing=True, pattern='^.emon(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**kyy Peler☑️**")
    await typew.edit("**kyy Peler✅**")
    sleep(2)
    await typew.edit("**Rendi Gilaa☑️**")
    await typew.edit("**Rendi Gilaa✅**")
    sleep(2)
    await typew.edit("**Skyzu Depresi☑️**")
    await typew.edit("**Skyzu Depresi✅**")
    sleep(2)
    await typew.edit("**Kitaro Gajelas☑️**")
    await typew.edit("**Kitaro Gajelas✅**")
    sleep(2)
    await typew.edit("**Bagas gila!☑️**")
    await typew.edit("**Bagas gila!✅**")
    sleep(2)
    await typew.edit("**Kyy² kang gabut!☑️**")
    await typew.edit("**Kyy² kang gabut!✅**")
    sleep(2)
    await typew.edit("**Tonic,MengRibet☑️**")
    await typew.edit("**Tonic,MengRibet✅**")
    sleep(2)
    await typew.edit("**erna,Mengintil☑️**")
    await typew.edit("**erna,Mengintil✅**")
    sleep(2)
    await typew.edit("**Grey,Stres☑️**")
    await typew.edit("**Grey,stres✅**")
    sleep(2)
    await typew.edit("**Gery,autis☑️**")
    await typew.edit("**Gery,autis✅**")
    sleep(2)
    await typew.edit("**Xander,jelek☑️**")
    await typew.edit("**Xander,jelek✅**")
    sleep(2)
    await typew.edit("**Mamed,Atheis☑️**")
    await typew.edit("**Mamed,Atheis✅**")
    sleep(2)
    await typew.edit("**Fidz,Sagapung☑️**")
    await typew.edit("**Fids,Sagapung✅**")
    sleep(2)
    await typew.edit("**CUMA EMON YG GANTENG WARAS DAN TIDAK SOMBONG !**")
    sleep(3
)

@register(outgoing=True, pattern='^.lah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")
    
@register(outgoing=True, pattern='^.gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`SUPPORT.. `")
    sleep(1)
    await typew.edit("`CENGHA...`")
    sleep(1)
    await typew.edit("`SUCCESSFULLY COMPELED`")
    sleep(1)
    await typew.edit("`💀SUPPORT` @greysupport 💀 CENGHA` @chipmunkchanel")




CMD_HELP.update({
    "emonbot":
    "`.sayo`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \n\n`.lah`\
    \nUsage: hiks\
    \n\n`.gc`\
    \nUsage: support\
    \n\n`.punten` ; `.emon`\
    \nUsage: misi."
})
