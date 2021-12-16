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
    await typew.edit("**IZINKAN SAYA INTRO**")
    sleep(1)
    await typew.edit("**GW ATHEIS**")
    sleep(1)
    await typew.edit("**SOLOYOLOO**")
    sleep(1)
    await typew.edit("**WAZZUP BRO**")
    sleep(1)
    await typew.edit("**SOBAT TOLOL GUA**")
    sleep(1)
    await typew.edit("**FAKKLAH..**")
    sleep(1)
    await typew.edit("**NGENTOT..**")
    sleep(1)
    await typew.edit("**ANJING ..**")
    sleep(1)
    await typew.edit("**KENALIN GUA EMON**")
    sleep(1)
    await typew.edit("**SUKA MELON**")
    sleep(1)
    await typew.edit("**GASUKA LEMON**")
    sleep(1)
    await typew.edit("**GW IMIGRAN DARI SURGA YANG DITURUNKAN KE BUMI**")
    sleep(2)
    await typew.edit("**DI MALAM PENGANTIN DAN TEGANG**")
    sleep(1)
    await typew.edit("**AYAH GUA GA BEKERJA SENDIRIAN, DIA DI BANTU IBU GUA**")
    sleep(2)
    await typew.edit("**IBU GUA TUGASNYA**")
    sleep(1)
    await typew.edit("**MENYIMPAN HASIL SELUNDUPAN**")
    sleep(1)
    await typew.edit("**GUA ANAK PERTAMA DARI TIGA BERSAUDARA**")
    sleep(2)
    await typew.edit("**UMUR GUA 19 DI TAMBAH 3 DI KURANGIN 1**")
    sleep(2)
    await typew.edit("**GUA TINGGAL BANTEN**")
    sleep(1)
    await typew.edit("**PAS NYA DI PANDEGLANG**")
    sleep(1)
    await typew.edit("**NTAR KALO MAU MAIN PC AJA, TAPI BAWA ROKOK AMA KOPI JANGAN NYUSAHIN GUA LOL**")
    sleep(3)

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
