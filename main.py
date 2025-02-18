import telebot
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8183421812:AAHMH86TYH0_6_gtYRw3TiRASQbAO1LYCSY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот .Я буду сортировать мусор и говорить куда выбрасывать")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
            
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r", encoding='utf-8').readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(file_name).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    bot.reply_to(message, "ИИ может ошибатся")
    bot.reply_to(message, f"Уверенность: {confidence_score}")
    if class_name.strip() == "0 Пластик":
        bot.reply_to(message,  "Пластик можно выбросить в желтый  контейнер")

    if class_name.strip() == "1 бумага":
        bot.reply_to(message,  "бумага можно выбросить в синий контейнер")

    if class_name.strip() == "2 стекло бутылка":
        bot.reply_to(message,  "стекло можно выбросить в специальные контейнеры")

    if class_name.strip() == "3 сигаретные окурки":
        bot.reply_to(message,  "сигаретные окурки можно выбросить в черные баки")

    if class_name.strip() == "4 картон":
        bot.reply_to(message,  "картон можно выбросить в Зеленый или синий бак: Бумага и картон, например, бумажные пакеты, газеты, каталоги, писчая бумага, коробки")

    if class_name.strip() == "5 батарейки":
        bot.reply_to(message,  "батарейки лушеё на переработку выбросить")

    if class_name.strip() == "6 градусники":
        bot.reply_to(message,  "Градусники лушеё cдать в пункт утилизации")
        
# Запускаем бота
bot.polling()