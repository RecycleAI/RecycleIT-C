import time
import logging
from telebot import TeleBot, types
import numpy as np
import os
from datetime import date

logging.basicConfig(filename='bot_log.log', filemode='a', level=logging.DEBUG)
logger = logging.getLogger(__name__)

ACCESS_TOKEN = "**********************"  # your bot token

WELCOME_MESSAGE = """🔸🔸 سلام! خوش آمدید.
برای ارسال عکس لطفاً به نکات زیر توجه کنید:

1⃣ ترجیحا عکس را از بالا گرفته و پس زمینه ی تصویر خاکستری باشد.

2⃣ سعی کنید تمام زباله در تصویر باشد.

3⃣ عکس از زباله های مچاله شده نیز ارسال کنید.

4⃣ عکس ها را به شکل فایل ارسال نکنید.

در صورت هرگونه مشکل در ارسال تصویر به آیدی @ARHPA پیام دهید.

پیشاپیش از همکاری شما متشکریم🙏
"""

RIGHT_SAMPLE_MESSAGE = 'عکس زیر یک نمونه ورودی صحیح را نمایش میدهد.'
CHOOSE_BUTTON_MESSAGE = 'لطفا نوع عکس را مشخص کنید'
PHOTO_MESSAGE = 'عکس خود را ارسال کنید'
SELFIE_PHOTO_FINISH = 'عکس با موفقیت ارسال شد.'
CHOOSE_PHOTO_MESSAGE = 'ابتدا نوع عکس را از لیست زیر مشخص سپس آن را آپلود کنید.'
WRONG_MESSAGE = 'لطفا طبق دستور العمل گفته شده عمل کنید'
PLASTIC_TYPES = 'از تصویر زیر میتوانید برای پیدا کردن نوع پلاستیک خود استفاده کنید👇'
MESSAGE_NOT_SEND = 'عکس ارسال نشد لطفا دوباره تلاش کنید'

bot = TeleBot(ACCESS_TOKEN)

# Define a markup to better interface
markup = types.ReplyKeyboardMarkup(row_width=2)
markup2 = types.ReplyKeyboardMarkup(row_width=3)
markup3 = types.ReplyKeyboardMarkup(row_width=2)

itembtn = types.KeyboardButton('ارسال عکس')

itembtn1 = types.KeyboardButton('پلاستیک نوع ۱ ♻️')
itembtn2 = types.KeyboardButton('پلاستیک نوع ۲ ♻️')
itembtn3 = types.KeyboardButton('پلاستیک نوع ۳ ♻️')
itembtn4 = types.KeyboardButton('پلاستیک نوع ۴ ♻️')
itembtn5 = types.KeyboardButton('پلاستیک نوع ۵ ♻️')
itembtn6 = types.KeyboardButton('پلاستیک نوع ۶ ♻️')
itembtn7 = types.KeyboardButton('نامشخص')
itembtn8 = types.KeyboardButton('شیشه')
itembtn9 = types.KeyboardButton('آلومینیوم')

itembtn_back = types.KeyboardButton('بازگشت به عقب')

markup.add(itembtn)
markup2.add(itembtn1, itembtn2, itembtn3, itembtn4,
            itembtn5, itembtn6, itembtn7, itembtn8,
            itembtn9)
markup3.add(itembtn_back)

# Define a global varible for check whether user specify the photo name or not.
photo_name = None


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.warning(message)
    bot.reply_to(message, WELCOME_MESSAGE)
    bot.send_message(message.chat.id, RIGHT_SAMPLE_MESSAGE, reply_markup=markup)
    photo = open('img0.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    # bot.send_message(message.chat.id, CHOOSE_BUTTON_MESSAGE, reply_markup=markup)


# Handle photo
@bot.message_handler(content_types=['photo'])
def save_photo(message):
    global photo_name
    if photo_name:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        name = str(np.random.rand(1, )[0])
        # image_path = '/var/lib/images/%s-%s.jpg' % (photo_name, name)

        today = date.today()
        directory = str(today)
        parent_dir = "/var/lib/images"
        path = os.path.join(parent_dir, directory)
        print(path)
        # bot.reply_to(message, path)
        try:
            os.mkdir(path)
        except:
            print("dir exist")
        image_path = '%s-%s.jpg' % (photo_name, name)
        image_path = os.path.join(path, image_path)

        with open(image_path, 'wb') as new_file:
            # bot.reply_to(message, f"new file opened --> {new_file}")
            print("ok")
            new_file.write(downloaded_file)

        logger.warning('A new photo saved {}'.format(message))
        photo_name = None
        bot.send_message(message.chat.id,
                         SELFIE_PHOTO_FINISH)
    else:
        bot.send_message(message.chat.id,
                         CHOOSE_PHOTO_MESSAGE,
                         reply_markup=markup)


# Handle all other messages with content_type 'text' specially when a button clicked.
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    logger.warning(message)
    global photo_name
    if message.text == 'ارسال عکس':
        photo_name = None
        bot.reply_to(message, CHOOSE_BUTTON_MESSAGE, reply_markup=markup2)
        bot.send_message(message.chat.id, PLASTIC_TYPES)
        photo = open('img1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == 'پلاستیک نوع ۱ ♻️':
        photo_name = 'PET'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'پلاستیک نوع ۲ ♻️':
        photo_name = 'PE-HD'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'پلاستیک نوع ۳ ♻️':
        photo_name = 'PVC'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'پلاستیک نوع ۴ ♻️':
        photo_name = 'PE-LD'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'پلاستیک نوع ۵ ♻️':
        photo_name = 'PP'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'پلاستیک نوع ۶ ♻️':
        photo_name = 'PS'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'نامشخص':
        photo_name = 'other'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'شیشه':
        photo_name = 'glass'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)

    elif message.text == 'آلومینیوم':
        photo_name = 'aluminium'
        bot.reply_to(message, PHOTO_MESSAGE, reply_markup=markup3)


    elif message.text == 'بازگشت به عقب':
        photo_name = None
        bot.reply_to(message, CHOOSE_BUTTON_MESSAGE, reply_markup=markup2)

    else:
        bot.reply_to(message, WRONG_MESSAGE, reply_markup=markup2)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        logger.error(err)
        time.sleep(5)
