import const as c
import random
import telebot
import datetime
from time import sleep
leet = cipher = key = 0
bot = telebot.TeleBot(c.token)
now = datetime.datetime.now()

@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/caesar_cipher')
    user_markup.row('/atbash_cipher')
    user_markup.row('/1337_cipher')
    user_markup.row('/chiffre_de_vigenere')
    bot.send_message(message.from_user.id, 'If bot is not responding, send /start or /back')
    bot.send_message(message.from_user.id, 'Choose the cipher:', reply_markup=user_markup)

@bot.message_handler(commands=['caesar_cipher'])
def cr(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('1', '2', '3', '4', '5', '6', '7', '8', '9')
    user_markup.row('10', '11', '12', '13', '14', '15', '16', '17', '18')
    user_markup.row('19', '20', '21', '22', '23', '24', '25', '26')
    user_markup.row('/back')
    bot.send_message(message.from_user.id, 'Choose the rotation:', reply_markup=user_markup)
    global cipher
    cipher = 1

@bot.message_handler(commands=['atbash_cipher'])
def ah(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/back')
    bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)
    global cipher
    cipher = 2

@bot.message_handler(commands=['1337_cipher'])
def lt(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Encrypt')
    user_markup.row('Decrypt')
    user_markup.row('/back')
    bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)
    global cipher
    cipher = 3

@bot.message_handler(commands=['chiffre_de_vigenere'])
def ve(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Encrypt')
    user_markup.row('Decrypt')
    user_markup.row('/back')
    bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)
    global cipher
    cipher = 4

@bot.message_handler(command=['back'])
def bk(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/caesar_cipher')
    user_markup.row('/atbash_cipher')
    user_markup.row('/1337_cipher')
    user_markup.row('/chiffre_de_vigenere')
    bot.send_message(message.from_user.id, 'Choose the cipher:', reply_markup=user_markup)
    global cipher, leet, dec, dec1
    leet = cipher = dec = dec1 = 0

@bot.message_handler(content_types=['text'])
def tt(message):
    global keyword, txt, dec, dec1, shift, cipher, leet, vig, key
    keyword = caesar = atbash = l33t = vig = ''
    letter = 0

    if message.text == '/back':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/caesar_cipher')
        user_markup.row('/atbash_cipher')
        user_markup.row('/1337_cipher')
        user_markup.row('/chiffre_de_vigenere')
        bot.send_message(message.from_user.id, 'Choose the cipher:', reply_markup=user_markup)

        dec1 = 0
        dec = 0
        leet = 0
        cipher = 0

    elif cipher == 0 and message.text == 'Change rotation':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1', '2', '3', '4', '5', '6', '7', '8', '9')
        user_markup.row('10', '11', '12', '13', '14', '15', '16', '17', '18')
        user_markup.row('19', '20', '21', '22', '23', '24', '25', '26')
        user_markup.row('/back')
        bot.send_message(message.from_user.id, 'Choose the rotation:', reply_markup=user_markup)

        cipher = 1

    elif message.text == 'Change direction':
        if cipher == 3:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Encrypt')
            user_markup.row('Decrypt')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)

            dec = 0

        elif cipher == 4:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Encrypt')
            user_markup.row('Decrypt')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)

            dec1 = 0

    elif message.text == 'Encrypt':
        if cipher == 3:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

            dec = 1

        elif cipher == 4:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

            dec1 = 1

    elif message.text == 'Decrypt':
        if cipher == 3:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'There could be troubles with translation, we are working on it.\nUse less punctuation marks to not cause troubles.', reply_markup=user_markup)
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

            dec = 2

        elif cipher == 4:
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

            dec1 = 2

    elif cipher == 1:
        try:
            int(message.text)
            num = 1
        except ValueError:
            num = 2

        if num == 1:
            if int(message.text) in list(range(1, 27)):
                shift = int(message.text)
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Change rotation')
                user_markup.row('/back')
                bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

        elif message.text == 'Change rotation':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('1', '2', '3', '4', '5', '6', '7', '8', '9')
            user_markup.row('10', '11', '12', '13', '14', '15', '16', '17', '18')
            user_markup.row('19', '20', '21', '22', '23', '24', '25', '26')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Choose the rotation:', reply_markup=user_markup)

            cipher = 1

        else:
            while letter < len(message.text):
                if message.text[letter] not in c.eng_alphabet:
                    if message.text[letter] in c.eng_alphabet_up:
                        if c.eng_alphabet_up.index(message.text[letter]) > 25 - shift:
                            caesar = caesar + c.eng_alphabet_up[(c.eng_alphabet_up.index(message.text[letter]) + shift) - 26]
                        else:
                            caesar = caesar + c.eng_alphabet_up[c.eng_alphabet_up.index(message.text[letter]) + shift]
                    else:
                        caesar = caesar + message.text[letter]
                elif c.eng_alphabet.index(message.text[letter]) > 25 - shift:
                    caesar = caesar + c.eng_alphabet[(c.eng_alphabet.index(message.text[letter]) + shift) - 26]
                else:
                    caesar = caesar + c.eng_alphabet[c.eng_alphabet.index(message.text[letter]) + shift]
                letter += 1

            bot.send_message(message.from_user.id, caesar)

    elif cipher == 2:
        while letter < len(message.text):
            if message.text[letter] not in c.eng_alphabet:
                if message.text[letter] in c.eng_alphabet_up:
                    index = c.eng_alphabet_up.index(message.text[letter])
                    c.eng_alphabet_up.reverse()
                    atbash = atbash + c.eng_alphabet_up[index]
                else:
                    atbash = atbash + message.text[letter]
            else:
                index = c.eng_alphabet.index(message.text[letter])
                c.eng_alphabet.reverse()
                atbash = atbash + c.eng_alphabet[index]
            letter += 1
        bot.send_message(message.from_user.id, atbash)
        c.eng_alphabet.reverse()
    elif cipher == 3:

        if message.text == 'Encrypt':
            dec = 1
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

        elif message.text == 'Decrypt':
            dec = 2
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'There could be troubles with translation, we are working on it.\nUse less punctuation marks to not cause troubles.', reply_markup=user_markup)
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)

        elif message.text == 'Change direction':
            dec = 0
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Encrypt')
            user_markup.row('Decrypt')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)

        elif dec == 1:
            while letter < len(message.text):
                if message.text[letter] not in c.eng_alphabet and message.text[letter] not in c.eng_alphabet_up:
                    l33t = l33t + message.text[letter]
                elif message.text[letter] not in c.eng_alphabet and message.text[letter] in c.eng_alphabet_up:
                    l33t = l33t + c.leet_alphabet[c.eng_alphabet_up.index(message.text[letter])][
                        random.randrange(0, len(c.leet_alphabet[c.eng_alphabet_up.index(message.text[letter])]) - 1)]
                else:
                    l33t = l33t + c.leet_alphabet[c.eng_alphabet.index(message.text[letter])][
                        random.randrange(0, len(c.leet_alphabet[c.eng_alphabet.index(message.text[letter])]) - 1)]
                letter += 1
            bot.send_message(message.from_user.id, l33t)

        elif dec == 2:
            while letter < len(message.text):

                if message.text[letter] == 'A' or message.text[letter] == '4' or message.text[letter] == '@' or \
                        message.text[letter] == 'λ' or message.text[letter] == 'a':
                    l33t = l33t + 'a'
                elif message.text[letter] == '\\' and message.text[letter + 1] == '/' and message.text[
                    letter + 2] == '\\' and message.text[letter + 3] == '/':
                    l33t = l33t + 'w'
                    letter += 3
                elif message.text[letter] == 'L' and message.text[letter + 1] == '|':
                    l33t = l33t + 'u'
                    letter += 1
                elif message.text[letter] == '/' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] != '/' and message.text[letter + 3] != '\\':
                    l33t = l33t + 'a'
                    letter += 1
                elif message.text[letter] == 'B' or message.text[letter] == 'b' or message.text[letter] == '6' or \
                        message.text[letter] == '8' or message.text[letter] == 'β':
                    l33t = l33t + 'b'
                elif message.text[letter] == '1' and message.text[letter + 1] == '3':
                    l33t = l33t + 'b'
                    letter += 1
                elif message.text[letter] == 'I' and message.text[letter + 1] == '3':
                    l33t = l33t + 'b'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '3':
                    l33t = l33t + 'b'
                    letter += 1
                elif message.text[letter] == 'c' or message.text[letter] == '<' or message.text[letter] == '©':
                    l33t = l33t + 'c'
                elif message.text[letter] == '(' and message.text[letter + 1] != 'T' and message.text[
                    letter + 1] != ')' and message.text[letter + 1] != ',' and message.text[letter + 1] != '_':
                    l33t = l33t + 'c'
                elif message.text[letter] == 'C' and message.text[letter + 1] != '-' and message.text[
                    letter + 1] != '_':
                    l33t = l33t + 'c'
                elif message.text[letter] == 'D' or message.text[letter] == 'd':
                    l33t = l33t + 'd'
                elif message.text[letter] == '|' and message.text[letter + 1] == ')':
                    l33t = l33t + 'd'
                    letter += 1
                elif message.text[letter] == '[' and message.text[letter + 1] == ')':
                    l33t = l33t + 'd'
                    letter += 1
                elif message.text[letter] == 'I' and message.text[letter + 1] == ')':
                    l33t = l33t + 'd'
                    letter += 1
                elif message.text[letter] == 'E' or message.text[letter] == 'e' or message.text[letter] == '3' or \
                        message.text[letter] == 'ё' or message.text[letter] == '€':
                    l33t = l33t + 'e'
                elif message.text[letter] == '[' and message.text[letter + 1] == '-' and message.text[
                    letter + 2] != ']':
                    l33t = l33t + 'e'
                    letter += 1
                elif message.text[letter] == 'F' or message.text[letter] == 'f':
                    l33t = l33t + 'f'
                elif message.text[letter] == ']' and message.text[letter + 1] == '=':
                    l33t = l33t + 'f'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '=':
                    l33t = l33t + 'f'
                    letter += 1
                elif message.text[letter] == 'I' and message.text[letter + 1] == '=':
                    l33t = l33t + 'f'
                    letter += 1
                elif message.text[letter] == 'G' or message.text[letter] == 'g':
                    l33t = l33t + 'g'
                elif message.text[letter] == 'C' and message.text[letter + 1] == '-':
                    l33t = l33t + 'g'
                    letter += 1
                elif message.text[letter] == '(' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] == '+':
                    l33t = l33t + 'g'
                    letter += 2
                elif message.text[letter] == '(' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] == '-':
                    l33t = l33t + 'g'
                    letter += 2
                elif message.text[letter] == 'H' or message.text[letter] == 'h' or message.text[letter] == '#':
                    l33t = l33t + 'h'
                elif message.text[letter] == '/' and message.text[letter + 1] == '-' and message.text[
                    letter + 2] == '/':
                    l33t = l33t + 'h'
                    letter += 2
                elif message.text[letter] == '[' and message.text[letter + 1] == '-' and message.text[
                    letter + 2] == ']':
                    l33t = l33t + 'h'
                    letter += 2
                elif message.text[letter] == ']' and message.text[letter + 1] == '-' and message.text[
                    letter + 2] == '[':
                    l33t = l33t + 'h'
                    letter += 2
                elif message.text[letter] == ')' and message.text[letter + 1] == '-' and message.text[
                    letter + 2] == '(':
                    l33t = l33t + 'h'
                    letter += 2
                elif message.text[letter] == '}' and message.text[letter + 1] == '{':
                    l33t = l33t + 'h'
                    letter += 1
                elif message.text[letter] == 'I' or message.text[letter] == 'i' or message.text[letter] == '!':
                    l33t = l33t + 'i'
                elif message.text[letter] == '|' and message.text[letter + 1] != '\\' and message.text[
                    letter + 1] != '?' and message.text[letter + 1] != '_' and message.text[letter + 1] != '2' and \
                        message.text[letter + 1] != '<' and message.text[letter + 1] != '>' and message.text[
                    letter + 1] != 'V' and message.text[letter + 2] != '|' and message.text[letter + 1] != 'o' and \
                        message.text[letter + 1] != '(':
                    l33t = l33t + 'i'
                elif message.text[letter] == '1' and message.text[letter + 1] != '2' and message.text[
                    letter + 1] != '_':
                    l33t = l33t + 'i'
                elif message.text[letter] == 'J' or message.text[letter] == 'j':
                    l33t = l33t + 'j'
                elif message.text[letter] == '_' and message.text[letter + 1] == '|':
                    l33t = l33t + 'j'
                    letter += 1
                elif message.text[letter] == '_' and message.text[letter + 1] == '/':
                    l33t = l33t + 'j'
                    letter += 1
                elif message.text[letter] == '_' and message.text[letter + 1] == '7':
                    l33t = l33t + 'j'
                    letter += 1
                elif message.text[letter] == '_' and message.text[letter + 1] == ')':
                    l33t = l33t + 'j'
                    letter += 1
                elif message.text[letter] == 'K' or message.text[letter] == 'k':
                    l33t = l33t + 'k'
                elif message.text[letter] == '|' and message.text[letter + 1] == '<':
                    l33t = l33t + 'k'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '(':
                    l33t = l33t + 'k'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == 'X':
                    l33t = l33t + 'k'
                    letter += 1
                elif message.text[letter] == 'L' or message.text[letter] == 'l' or message.text[letter] == '£':
                    l33t = l33t + 'l'
                elif message.text[letter] == '1' and message.text[letter + 1] == '_':
                    l33t = l33t + 'l'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] != '|':
                    l33t = l33t + 'l'
                    letter += 1
                elif message.text[letter] == 'M' or message.text[letter] == 'm':
                    l33t = l33t + 'm'
                elif message.text[letter] == '/' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] == '/' and message.text[letter + 3] == '\\':
                    l33t = l33t + 'm'
                    letter += 3
                elif message.text[letter] == '|' and message.text[letter + 1] == 'V' and message.text[
                    letter + 2] == '|':
                    l33t = l33t + 'm'
                    letter += 2
                elif message.text[letter] == '(' and message.text[letter + 1] == 'T' and message.text[
                    letter + 2] == ')':
                    l33t = l33t + 'm'
                    letter += 2
                elif message.text[letter] == '|' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] == '/' and message.text[letter + 3] == '|':
                    l33t = l33t + 'm'
                    letter += 3
                elif message.text[letter] == '^' and message.text[letter + 1] == '^':
                    l33t = l33t + 'm'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '^' and message.text[
                    letter + 2] == '^' and message.text[letter + 3] == '|':
                    l33t = l33t + 'm'
                    letter += 3
                elif message.text[letter] == 'N' or message.text[letter] == 'n':
                    l33t = l33t + 'n'
                elif message.text[letter] == '|' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] == '|':
                    l33t = l33t + 'n'
                    letter += 2
                elif message.text[letter] == '/' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] == '/':
                    l33t = l33t + 'n'
                    letter += 2
                elif message.text[letter] == 'o' or message.text[letter] == 'Ω':
                    l33t = l33t + 'o'
                elif message.text[letter] == '0' and message.text[letter + 1] != ',':
                    l33t = l33t + 'o'
                elif message.text[letter] == 'O' and message.text[letter + 1] != ',':
                    l33t = l33t + 'o'
                elif message.text[letter] == '(' and message.text[letter + 1] == ')':
                    l33t = l33t + 'o'
                    letter += 1
                elif message.text[letter] == '[' and message.text[letter + 1] == ']':
                    l33t = l33t + 'o'
                    letter += 1
                elif message.text[letter] == 'P' or message.text[letter] == 'p' or message.text[letter] == '?' or \
                        message.text[letter] == '9':
                    l33t = l33t + 'p'
                elif message.text[letter] == '|' and message.text[letter + 1] == '*':
                    l33t = l33t + 'p'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == 'o':
                    l33t = l33t + 'p'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '>':
                    l33t = l33t + 'p'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == 'D':
                    l33t = l33t + 'p'
                    letter += 1
                elif message.text[letter] == 'Q' or message.text[letter] == 'q':
                    l33t = l33t + 'q'
                elif message.text[letter] == '(' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] == ',' and message.text[letter + 3] == ')':
                    l33t = l33t + 'q'
                    letter += 3
                elif message.text[letter] == 'O' and message.text[letter + 1] == ',':
                    l33t = l33t + 'q'
                    letter += 1
                elif message.text[letter] == '(' and message.text[letter + 1] == ',' and message.text[
                    letter + 2] == ')':
                    l33t = l33t + 'q'
                    letter += 2
                elif message.text[letter] == 'R' or message.text[letter] == 'r' or message.text[letter] == 'Я':
                    l33t = l33t + 'r'
                elif message.text[letter] == '1' and message.text[letter + 1] == '2':
                    l33t = l33t + 'r'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '?':
                    l33t = l33t + 'r'
                    letter += 1
                elif message.text[letter] == '|' and message.text[letter + 1] == '2':
                    l33t = l33t + 'r'
                    letter += 1
                elif message.text[letter] == 'S' or message.text[letter] == 's' or message.text[letter] == '5' or \
                        message.text[letter] == '$':
                    l33t = l33t + 's'
                elif message.text[letter] == 'T' or message.text[letter] == 't' or message.text[letter] == '7' or \
                        message.text[letter] == '+':
                    l33t = l33t + 't'
                elif message.text[letter] == '-' and message.text[letter + 1] == '|' and message.text[
                    letter + 2] == '-':
                    l33t = l33t + 't'
                    letter += 2
                elif message.text[letter] == 'U' or message.text[letter] == 'u':
                    l33t = l33t + 'u'
                elif message.text[letter] == '|' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] == '|':
                    l33t = l33t + 'u'
                    letter += 2
                elif message.text[letter] == '(' and message.text[letter + 1] == '_' and message.text[
                    letter + 2] == ')':
                    l33t = l33t + 'u'
                    letter += 2
                elif message.text[letter] == 'v' or message.text[letter] == '√':
                    l33t = l33t + 'v'
                elif message.text[letter] == 'V' and message.text[letter + 1] != 'V':
                    l33t = l33t + 'v'
                elif message.text[letter] == '\\' and message.text[letter + 1] == '/':
                    l33t = l33t + 'v'
                    letter += 1
                elif message.text[letter] == '\\' and message.text[letter + 1] == '\\' and message.text[
                    letter + 2] == '/' and message.text[letter + 3] == '/':
                    l33t = l33t + 'v'
                    letter += 3
                elif message.text[letter] == 'W' or message.text[letter] == 'w':
                    l33t = l33t + 'w'
                elif message.text[letter] == 'V' and message.text[letter + 1] == 'V':
                    l33t = l33t + 'w'
                    letter += 1
                elif message.text[letter] == '\\' and message.text[letter + 1] == 'V' and message.text[
                    letter + 2] == '/':
                    l33t = l33t + 'w'
                    letter += 2
                elif message.text[letter] == 'U' and message.text[letter + 1] == 'U':
                    l33t = l33t + 'w'
                    letter += 1
                elif message.text[letter] == '\\' and message.text[letter + 1] == '|' and message.text[
                    letter + 2] == '/':
                    l33t = l33t + 'w'
                    letter += 2
                elif message.text[letter] == 'X' or message.text[letter] == 'x' or message.text[letter] == '*':
                    l33t = l33t + 'x'
                elif message.text[letter] == '>' and message.text[letter + 1] == '<':
                    l33t = l33t + 'x'
                    letter += 1
                elif message.text[letter] == ')' and message.text[letter + 1] == '(':
                    l33t = l33t + 'x'
                    letter += 1
                elif message.text[letter] == 'Y' or message.text[letter] == 'y' or message.text[letter] == 'λ':
                    l33t = l33t + 'y'
                elif message.text[letter] == '"' and message.text[letter + 1] == '/':
                    l33t = l33t + 'y'
                    letter += 1
                elif message.text[letter] == 'Z' or message.text[letter] == 'z' or message.text[letter] == '2' or \
                        message.text[letter] == '%':
                    l33t = l33t + 'z'
                elif message.text[letter] == '7' and message.text[letter + 1] == '_':
                    l33t = l33t + 'z'
                    letter += 1
                elif message.text[letter] == '>' and message.text[letter + 1] == '_':
                    l33t = l33t + 'z'
                    letter += 1
                else:
                    l33t = l33t + message.text[letter]
                letter += 1

            bot.send_message(message.from_user.id, l33t)

    elif cipher == 4:
        if message.text == 'Encrypt':
            dec1 = 1
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)
        elif message.text == 'Decrypt':
            dec1 = 2
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Change direction')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'There could be troubles with translation, we are working on it.\nUse less punctuation marks to not cause troubles.', reply_markup=user_markup)
            bot.send_message(message.from_user.id, 'Write your message:', reply_markup=user_markup)
        elif message.text == 'Change direction':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Encrypt')
            user_markup.row('Decrypt')
            user_markup.row('/back')
            bot.send_message(message.from_user.id, 'Choose the direction:', reply_markup=user_markup)
            dec1 = 0
        else:

            if dec1 == 1:
                if key == 0:
                    txt = message.text
                    bot.send_message(message.from_user.id, 'Write key word:')
                    key += 1
                elif key == 1:
                    keyword = message.text
                    vig = c.encryptMessage(keyword, txt)
                    bot.send_message(message.from_user.id, vig)
                    bot.send_message(message.from_user.id, 'Write your message:')
                    key = 0
                    txt = ''

            elif dec1 == 2:
                if key == 0:
                    txt = message.text
                    bot.send_message(message.from_user.id, 'Write key word:')
                    key += 1
                elif key == 1:
                    keyword = message.text
                    vig = c.decryptMessage(keyword, txt)
                    bot.send_message(message.from_user.id, vig)
                    bot.send_message(message.from_user.id, 'Write your message:')
                    key = 0
                    txt = ''

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        ErrorLog = open('ErrorLog.txt', 'a')
        ErrorLog.write('**************************\n' + now.strftime('%d-%m-%Y %H:%M:%S') + '\n' + str(e) + '\n**************************\n\n')
        ErrorLog.close()
        sleep(10)
