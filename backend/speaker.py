import asyncio
import edge_tts
import os
import tempfile
import threading
from playsound import playsound

VOICE = "en-US-AriaNeural"

last_spoken = None


async def generate_audio(text, filename):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )
    await communicate.save(filename)


def _speak(text):
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp_file.close()

    asyncio.run(
        generate_audio(
            text,
            temp_file.name
        )
    )

    playsound(temp_file.name)

    os.remove(temp_file.name)


def speak(text):
    global last_spoken

    if text == "UNKNOWN":
        return

    if text == last_spoken:
        return

    last_spoken = text

    threading.Thread(
        target=_speak,
        args=(text,),
        daemon=True
    ).start()