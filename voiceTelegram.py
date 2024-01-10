import telepot
from telepot.loop import MessageLoop
import speech_recognition as sr
import urllib.request
import os
import requests
from pydub import AudioSegment

recognizer = sr.Recognizer()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'voice':
        file_id = msg['voice']['file_id']
        file_path = bot.getFile(file_id)['file_path']
        file_url = f'https://api.telegram.org/file/bot6661340612:AAHDPlnvPB9nf02cin94br-UrUwfozS3z60/{file_path}'
        file_name = 'voice_note.ogg'
        download_path = os.path.join('C:\\Users\\mmira\\PycharmProjects\\pythonProject2', file_name)
        wav_path = os.path.join('C:\\Users\\mmira\\PycharmProjects\\pythonProject2', 'voice_note.wav')

        try:
            # Download voice note to the specified directory
            urllib.request.urlretrieve(file_url, download_path)

            # Convert audio file to WAV format
            audio = AudioSegment.from_ogg(download_path)
            audio.export(wav_path, format="wav")

            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)

            bot.sendMessage(chat_id, f'Text from voice note: {text}')

        except Exception as e:
            bot.sendMessage(chat_id, f'Error: {str(e)}')
# Gantilah 'YOUR_BOT_TOKEN' dengan token bot Telegram Anda
bot = telepot.Bot('6661340612:AAHDPlnvPB9nf02cin94br-UrUwfozS3z60')

MessageLoop(bot, handle).run_as_thread()

while True:
    pass