import os
import telebot

bot = telebot.TeleBot('') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, Estoy disponible")
    print("Mandaron saludo")

@bot.message_handler(commands=['nombre', 'hi']) #definimos el comando
def nombre(mensaje):
    bot.reply_to(mensaje, "Mi nombre es Cinthia")
    print("Mandaron Nombre")

@bot.message_handler(commands=['edad', 'age'])
def edad(mensaje):
    bot.reply_to(mensaje, "Tengo 24 años")
    print("Mandaron Edad")

@bot.message_handler(commands=['direccion', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "Santa Cruz de Yojoa")
    print("Mandaron Direccion")

@bot.message_handler(commands=['comidafavorita', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "pizza")
    print("Mandaron comida favorita")

@bot.message_handler(commands=['carrera', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "Estudio Ingenieria en sistemas")
    print("Mandaron carrera que estudia")
bot.polling()