from PIL import Image
import telebot
bot = telebot.TeleBot("7323697551:AAHl_X_yllnsn99bKKrtCQhzbPwEKxlfTiY")

@bot.message_handler(commands = ['start'])
def start(msg):
    (print(msg)
@bot.photo_handler(content_types=['photo']))
def file_handler(msg):
    print(msg)
    raw = msg.photo[1].file_id
    path = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(msg.chat.id, text="Take your photo.Changning your photo,please wait...")



@bot.message_handler(content_types=['text'])
def text_handler(msg):
    print(msg)

try:
    img = Image.open('https://static1.squarespace.com/static/656f4e4dababbd7c042c4946/657236350931ee4538eea52c/65baf15103d8ad2826032a8a/1707422532886/how-to-stop-being-a-people-pleaser-1_1.jpg?format=1500w.jpg')
    width, height = img.size
    new_width = 3 * (height // 4)
    img = img.resize((new_width, height), Image.LANCZOS)
    img.save('resized_photo.jpg')


except Exception:
    print("Error")

@bot.photo_handler(content_types=['photo'])
def photo_handler(msg):
    print(msg)
    cid ='407221460'
    img = open('resized_photo.jpg', 'rb')
    bot.send_photo(cid, img)

bot.polling(none_stop=True)