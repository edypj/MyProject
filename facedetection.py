import cap as cap
import cv2
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# Inisialisasi Cascade Classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inisialisasi bot Telegram
bot = telepot.Bot('6661340612:AAHDPlnvPB9nf02cin94br-UrUwfozS3z60')

# Membuat menu sederhana
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Detect Face', callback_data='detect_face')],
    [InlineKeyboardButton(text='Stop Detection', callback_data='stop_detection')],
])

def detect_and_send_face(chat_id):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if len(faces) > 0:
            cv2.imwrite('detected_face.jpg', frame)
            bot.sendPhoto(chat_id, open('detected_face.jpg', 'rb'), caption='Wajah terdeteksi!')
            break
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Welcome to Face Detection Bot! Click a button to start or stop detection:', reply_markup=menu)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if query_data == 'detect_face':
        bot.sendMessage(from_id, 'Starting face detection...')
        detect_and_send_face(from_id)
    elif query_data == 'stop_detection':
        bot.sendMessage(from_id, 'Stopping face detection...')
        cv2.destroyAllWindows()

MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

while True:
    pass