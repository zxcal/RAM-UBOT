# Copyright by @danish
# Recode by @mrismanaziz
# 

import asyncio
import os
import time

import cv2
import PIL

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import bash, edit_or_reply, ram_cmd, progress


@ram_cmd(pattern="prg(?: |$)(.*)")
async def frg(animu):
    text = animu.pattern_match.group(1)
    xx = await edit_or_reply(animu, f"`Sabar, Sedang membuat kodok tolol mu....`")
    if not text:
        await edit_delete(xx, f"**Hoi, Kasih Gua satu pesan ngentot...**")
    else:
        sticcers = await animu.client.inline_query("honka_says_bot", f"{text}.")
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )
    except Exception:
        return await xx.edit(
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
        )
    await xx.delete()


@ram_cmd(pattern="rgif(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`Checking...`")
    download = await event.client.download_media(reply.media)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    danish = PIL.Image.open("danish.png")
    dark, python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=00ff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""
    await xx.edit(f"```Sabar, sedang memuat...```")
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await xx.edit(f"```Sedang meng upload {rambot}```")
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        "danish.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]")
        ),
    )
    await event.delete()
    await bash("rm -f downloads/*.png")
    await bash("rm -f *.png")
    os.remove("danish.mp4")


CMD_HELP.update(
    {
        "rgif": f"**Plugin : **`rgif`\
        \n\n  •  **Syntax :** `{cmd}gif` <sambil reply ke media>\
        \n  •  **Function : **Untuk mengubah gambar jadi gif memutar.\
    "
    }
)


CMD_HELP.update(
    {
        "fun": f"**Plugin : **`fun`\
        \n\n  •  **Syntax :** `{cmd}rst` <text>\
        \n  •  **Function : **Untuk membuat stiker teks dengan templat stiker acak.\
        \n\n  •  **Syntax :** `{cmd}prg` <text>\
        \n  •  **Function : **Untuk menyuruh kodok badut, menuliskan teks dalam bentuk stiker.\
    "
    }
)
