import telepot
from telepot.loop import MessageLoop
import speech_recognition as sr
import urllib.request
import os
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

                # Recognize the speech
                text = recognizer.recognize_google(audio_data, language="ar-SA,id-ID,en-US")

                # Retrieve confidence score if available
                confidence = recognizer.recognize_google(audio_data, show_all=True).get('alternative', [])[0].get(
                    'confidence', None)

                if confidence:
                    bot.sendMessage(chat_id, f'Text from voice note: {text}\nConfidence: {confidence}')
                else:
                    bot.sendMessage(chat_id, f'Text from voice note: {text}\nConfidence information not available.')

        except sr.UnknownValueError:
            bot.sendMessage(chat_id, 'Maaf, sistem tidak dapat memahami audio tersebut.')Text from voice note: Halo saya Edi
Confidence: 0.52206874

        except sr.RequestError as e:
            bot.sendMessage(chat_id,
                            f'Terdapat kesalahan saat terhubung ke layanan Google Speech Recognition; {str(e)}')

        except Exception as e:
            bot.sendMessage(chat_id, f'Terdapat kesalahan: {str(e)}')


# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot = telepot.Bot('-----------')

MessageLoop(bot, handle).run_as_thread()

while True:
    pass
