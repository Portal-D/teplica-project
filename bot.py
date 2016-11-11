# -*- coding: utf-8 -*-
import config
import telebot
import subprocess
import time
from telebot import types
import datetime
import os
from daba import getkey
from daba import sendup
from daba import getid
#from daba import newuser
#from temp import tep
import os
#f = open('путь к файлу для команд', 'tw', encoding='utf-8')
#f.close()


global par
par=0

#Тест для неавторизированного пользователя
global a
a="Вы не авторизированны. Пройдите авторизацию командой /auth [пароль]"

#Функция получение температуры
def get_temp():
  if os.path.isdir("/sys/bus/w1/devices/серийный номер"):


    tfile2=open("/sys/bus/w1/devices/серийный номер/w1_slave")
 
    ttext2=tfile2.read()
 
    tfile2.close()
 
    temp2=ttext2.split("\n")[1].split(" ")[9]
 
    t2=float(temp2[2:])/1000

    return t2

  else:

    print ('File not found')

  
#Пароль
keyword=str(getkey())[2:-3]


#Конфигурация токена
bot = telebot.TeleBot(config.token)
print (sendup())
#Создание кастомной клавиатуры

#########################Авторизациии##########################################
markup2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
markdown = types.ReplyKeyboardHide() #Деактивация
itembtn5 = types.KeyboardButton('🔐 Авторизация') #Название кнопки 5
markup2.add(itembtn5) #Занесение кнопок в матрицу

#########################Клавиатура авторизации##########################################


#########################Клавиатура главного меню##########################################
markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn1 = types.KeyboardButton('📸 Прислать снимок') #Название кнопки 1
itembtn4 = types.KeyboardButton('🖼 Управление окнами')
itembtn2 = types.KeyboardButton('🌡 Прислать температуру') #Название кнопки 2
markup.add(itembtn1, itembtn4, itembtn2) #Занесение кнопок в матрицу

#########################Клавиатура главного меню##########################################



markup3 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn10 = types.KeyboardButton('🤖 Выключить автоматику 🎾') #Название кнопки 1
itembtn11 = types.KeyboardButton('↕️ Ручное управление')
itembtn12 = types.KeyboardButton('🔙 Назад')
markup3.add(itembtn10, itembtn11, itembtn12) #Занесение кнопок в матрицу

markup4 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn13 = types.KeyboardButton('🤖 Включить автоматику 🔴') #Название кнопки 1
markup4.add(itembtn13, itembtn11, itembtn12) #Занесение кнопок в матрицу

markup5 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn14 = types.KeyboardButton('1⃣ Первое окно') #Название кнопки 1
itembtn15 = types.KeyboardButton('2⃣ Второе окно') #Название кнопки 1
itembtn16 = types.KeyboardButton('↩️ Назад') #Название кнопки 1
markup5.add(itembtn14, itembtn15, itembtn16) #Занесение кнопок в матрицу

markup6 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn17 = types.KeyboardButton('⬆️ Открыть окно 1⃣') #Название кнопки 1
itembtn18 = types.KeyboardButton('⬇️ Закрыть окно 1⃣') #Название кнопки 1
itembtn19 = types.KeyboardButton('🔼 Приоткрыть окно 1⃣') #Название кнопки 1
itembtn20 = types.KeyboardButton('🔽 Призакрыть окно 1⃣') #Название кнопки 1
itembtn21 = types.KeyboardButton('⬅️ Назад') #Название кнопки 1
markup6.add(itembtn17, itembtn18, itembtn19, itembtn20, itembtn21) #Занесение кнопок в матрицу

markup7 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, колва кнопок в одной ряду
itembtn22 = types.KeyboardButton('⬆️ Открыть окно 2⃣') #Название кнопки 1
itembtn23 = types.KeyboardButton('⬇️ Закрыть окно 2⃣') #Название кнопки 1
itembtn24 = types.KeyboardButton('🔼 Приоткрыть окно 2⃣') #Название кнопки 1
itembtn25 = types.KeyboardButton('🔽 Призакрыть окно 2⃣') #Название кнопки 1
markup7.add(itembtn22, itembtn23, itembtn24, itembtn25, itembtn21) #Занесение кнопок в матрицу

bot.send_message(99908516, "🔄Перезагрузка")


    

def pos():
    f = open('Путь к файлу с позициями окна')
    com = f.read()
    f.close()
    return com


def avtor(idi):
    global par
    if par==idi:
            return 0
    else:
            if getid(str(idi))==20:
                par=idi
                return 0;
            else:
                bot.send_message(idi, "Вы не авторизированны. Пройдите авторизацию командой /auth [пароль]", reply_markup=markup2)
                return 1;    
        


@bot.message_handler(regexp="🔐 Авторизация")
def auth(message):
    bot.send_message(message.chat.id, "Введите /auth [пароль]")

@bot.message_handler(commands=['auth'])
def start2(message):
    if message.text[6:]==keyword:
      if getid(str(message.chat.id))==20:
        bot.send_message(message.chat.id, "Вы уже авторизированы")
      else:
        global par
        bot.send_message(message.chat.id, "Успешно", reply_markup=markup)
        par=message.chat.id
        #print ("error", newuser(message.chat.id))
        f = open('Путь к фалу связи с базой', 'w')
        f.write(str(message.chat.id))
        f.close()
        os.system('./newuser.sh')
        print (message.chat.id)
        print (par)
    else:
        bot.send_message(message.chat.id, "Неверно")
        print (keyword)
        print (message.text[6:])
        print (message.chat.id)


# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
     global par
     if avtor(message.chat.id)!=0:
         print (par)
         bot.send_message(message.chat.id, "🔑 Вы не авторизированны. Пройдите авторизацию командой /auth [пароль]", reply_markup=markup2)
     else:
	     bot.send_message(message.chat.id, "✅ Вы авторизированный пользователь. Наберите /help, для того, чтобы узнать список команд.")



#Команда запроса помощи - /help
@bot.message_handler(commands=['help'])
def help(message):
  if avtor(message.chat.id)==0:
     mas='🏡 Данный бот управляет теплицей на моём участке. \n🤖 Список команд для помощи, в управление этим ботом:  \n📖 Получить справку - /help \n Остальное всё управляется при помощи клавиатуры :)'
     bot.send_message(message.chat.id, mas, reply_markup=markup)
     print (message.chat.id, message.text)

	
 
#Заменить интерфейс командной строки на клавиатуру
@bot.message_handler(commands=['show'])
def show(message):
  if avtor(message.chat.id)==0:
     mas='⌨Клавиатура включена'
     bot.send_message(message.chat.id, mas, reply_markup=markup)
     print (message.chat.id, message.text)



#получить температуру
@bot.message_handler(regexp="🌡 Прислать температуру")
def temp(message):
  if avtor(message.chat.id)==0:
     tp=get_temp()
     mas='🌡  Температура в теплице: '+str(tp)+'°C'
     bot.send_message(message.chat.id, mas)
     print (message.chat.id, message.text)
    

#прислать снимок
@bot.message_handler(regexp="📸 Прислать снимок")
def photo(message): 
     if avtor(message.chat.id)==0:
         now=str(datetime.datetime.now()) #Получаем дату
         minute=int(now[15:16]) #Вырезаем минуты
         if minute<6: #Заменяем минуты, на близжайшее время получение фотоснимка
           minute=0
         else:
           minute=5
         path='/mnt/yandex/photo/'+now[0:4]+now[5:7]+now[8:10]+"-"+now[11:13]+now[14:15]+str(minute)+'-snapshot.jpg' #Путь к папку со снимком
         print (path)
         try:
             f = open(path, 'rb') #Открытия файла - снимка
             bot.send_photo(message.chat.id, f) #Отправка снимка
             print (message.chat.id, message.text)
         except:
             bot.send_message(message.chat.id, "Фоток нет :(")



@bot.message_handler(regexp="🖼 Управление окнами")
def windows(message):
   if avtor(message.chat.id)==0:
       print ("window")
       print (pos())
       if str(pos())[0]=='1':
           bot.send_message(message.chat.id, "Ок", reply_markup=markup3)
       else: 
           bot.send_message(message.chat.id, "Ок", reply_markup=markup4)
@bot.message_handler(regexp="🔙 Назад")
def windows(message):
   if avtor(message.chat.id)==0:
       bot.send_message(message.chat.id, "Ок",  reply_markup=markup)

@bot.message_handler(regexp="🤖 Выключить автоматику 🎾")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('30')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup4)

@bot.message_handler(regexp="🤖 Включить автоматику 🔴")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('31')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup3)


@bot.message_handler(regexp="↕️ Ручное управление")
def windows(message):
   if avtor(message.chat.id)==0:
       bot.send_message(message.chat.id, "Ок",  reply_markup=markup5)
@bot.message_handler(regexp="↩️ Назад")
def windows(message):
   if avtor(message.chat.id)==0:
       if str(pos())[0]=='1':
           bot.send_message(message.chat.id, "Ок", reply_markup=markup3)
       else: 
           bot.send_message(message.chat.id, "Ок", reply_markup=markup4)


@bot.message_handler(regexp="⬅️ Назад")
def windows(message):
   if avtor(message.chat.id)==0:
       bot.send_message(message.chat.id, "Ок",  reply_markup=markup5)

@bot.message_handler(regexp="1⃣ Первое окно")
def windows(message):
   if avtor(message.chat.id)==0:
       bot.send_message(message.chat.id, "Ок",  reply_markup=markup6)
@bot.message_handler(regexp="2⃣ Второе окно")
def windows(message):
   if avtor(message.chat.id)==0:
       bot.send_message(message.chat.id, "Ок",  reply_markup=markup7)

@bot.message_handler(regexp="⬆️ Открыть окно 1⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('11')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('/mnt/raw/wind')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup6)

@bot.message_handler(regexp="⬇️ Закрыть окно 1⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('10')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup6)

@bot.message_handler(regexp="🔼 Приоткрыть окно 1⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('13')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup6)
@bot.message_handler(regexp="🔽 Призакрыть окно 1⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('12')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup6)


@bot.message_handler(regexp="⬆️ Открыть окно 2⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('21')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup7)

@bot.message_handler(regexp="⬇️ Закрыть окно 2⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('20')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup7)

@bot.message_handler(regexp="🔼 Приоткрыть окно 2⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('23')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами)
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup7)
@bot.message_handler(regexp="🔽 Призакрыть окно 2⃣")
def windows(message):
   if avtor(message.chat.id)==0:
       f = open('Файл с командами', 'w')
       f.write('22')
       f.close()
       k="No"
       while k[0:2]!="OK":
           time.sleep(5)           
           f = open('Файл с командами')
           k = f.read()
           f.close()
           print(k[0:2])
       bot.send_message(message.chat.id, "Успешно",  reply_markup=markup7)

#Реакция на команды, не приведённые выше
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
   if avtor(message.chat.id)==0:
         bot.send_message(message.chat.id, "Я не знаю такой команды. Набери /help, чтобы получить список команд")
         print (message.chat.id, message.text)

		 
if __name__ == '__main__':
       # tep()
        bot.polling()
