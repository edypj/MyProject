import telepot
from gtts import gTTS
import os

# Ganti dengan token bot Anda
TOKEN = '---------'

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        text = msg['text']

        # Cek apakah pesan dimulai dengan /voice
        if text.startswith('/voice'):
            # Ambil teks setelah '/voice'
            message_text = text[7:].strip()

            if message_text:
                voice_file = text_to_speech(message_text)
                bot.sendVoice(chat_id, open(voice_file, 'rb'))
                os.remove(voice_file)
            else:
                bot.sendMessage(chat_id, "Mohon berikan teks setelah perintah /voice.")
        elif text == '/menu':
            send_menu(chat_id)
        else:
            # Respon default jika bukan perintah /voice atau /menu
            bot.sendMessage(chat_id, "Kirimkan /voice diikuti oleh teks untuk mengonversinya menjadi voice note.")

def text_to_speech(text):
    language = 'id'  # Kode bahasa Indonesia
    tts = gTTS(text=text, lang=language, slow=False)
    voice_file = 'voice_note.mp3'
    tts.save(voice_file)
    return voice_file

def send_menu(chat_id):
    menu_text = "Pilih opsi:\n/voice TeksAnda - Konversi Teks menjadi Voice Note"
    bot.sendMessage(chat_id, menu_text)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening for messages...')

import time
while True:
    time.sleep(10)