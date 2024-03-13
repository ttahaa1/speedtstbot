from pytube import YouTube

import os
#@KOK0KK

import telebot 
import random
from telebot import types
#@KOK0KK
#المطور

bot = telebot.TeleBot('6888638576:AAGzMZngCk_U6Cj07V4-Cnfm6idFe1R-4p8')
#@KOK0KK
print(' Go Bot /Start ')
@bot.message_handler(commands=['start'])
def message1(message):
    id1 = str(message.from_user.id)
    #@KOK0KK
    #@KOK0KK


    
    ty = types.InlineKeyboardButton(text='دخول البوت',callback_data='ty')
    kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
    bot.send_message(message.chat.id,'*اهلا بك في بوت تحميل من اليوتيوب*',parse_mode='markdown',reply_markup=kj)

@bot.callback_query_handler(func=lambda call:True)
def call(call):
    if call.data =='ty':
        nc = types.InlineKeyboardButton(text='تحميل فيديو',callback_data='nc')
        cn = types.InlineKeyboardButton(text='تحميل مقطع صوتي',callback_data='cn')
        ncc = types.InlineKeyboardMarkup(row_width=1)
        ncc.add(nc,cn)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*اختار التحميل المناسب*',reply_markup=ncc,parse_mode='markdown')
    elif call.data =='nc':
        mk = types.InlineKeyboardButton(text='قناة مطور لبوت',url='https://t.me/JG0Bot')
        mk1 = types.InlineKeyboardMarkup(row_width=1)
        mk1.add(mk)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*ارسل الان رابط المقطع من فضلك*',reply_markup=mk1,parse_mode='markdown')
        bot.register_next_step_handler(message,m1,message.id)
    elif call.data =='cn':
        mk = types.InlineKeyboardButton(text='قناة البوت',url='https://t.me/JG0Bot')
        mk1 = types.InlineKeyboardMarkup(row_width=1)
        mk1.add(mk)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*ارسل الان رابط المقطع من فضلك*',reply_markup=mk1,parse_mode='markdown')
        bot.register_next_step_handler(message,m2,message.id)
    #@KOK0KK
    #@KOK0KK
def m1(message,id):
    id1 = str(message.from_user.id)
    me = str(message.text)
    if ('https') in me :
        #@KOK0KK
        #@KOK0KK
        ty = types.InlineKeyboardButton(text='مبرمج البوت',url='https://t.me/KOK0KK')
        kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*جار التحميل الان..*',reply_markup=kj,parse_mode='markdown')
        video_url = me
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download()
        #@KOK0KK

    
        filem = video.default_filename
     
        ki='qwertyuioplkjhgfdsazxcvbn'
        uo = str(''.join(random.choice(ki)for ii in range(4)))
        #@KOK0KK
       
        namenew = f'{uo}.mp4'
        os.rename(filem, namenew)
        bot.send_video(id1,video=open(f'{uo}.mp4','rb'),caption='*تم التحميل بنجاح*',parse_mode='markdown',reply_markup=kj)
        os.remove(filem)
        os.remove(f'{uo}.mp4')
 #@KOK0KK       
    else:
        mi = types.InlineKeyboardButton(text='القائمة الرئسية',callback_data='ty')
        mi1 = types.InlineKeyboardMarkup(row_width=2);mi1.add(mi)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*عذرا ارسل رابط صحيح من فضلك*',parse_mode='markdown',reply_markup=mi1)
def m2(message,id):
    id1 = str(message.from_user.id)
    me = str(message.text)
    if ('https') in me :
        ty = types.InlineKeyboardButton(text='مبرمج البوت',url='https://t.me/KOK0KK')
        kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*جار التحميل الان..*',reply_markup=kj,parse_mode='markdown')
        video_url = me
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download()
#@KOK0KK
    
        filem = video.default_filename
     
        u='qwertyuioplkjhgfdsazxcvbn'
        rr = str(''.join(random.choice(u)for ii in range(4)))
        namenew = f'{rr}.mp4'
        os.rename(filem, namenew)
        with open(namenew,'rb') as ad:
            bot.send_audio(id1,ad,caption='*تم التحميل بنجاح*',parse_mode='markdown')
            os.remove(filem)
            os.remove(f'{rr}.mp3')   
            #@KOK0KK 
    else:
        mi = types.InlineKeyboardButton(text='القائمة الرئسية',callback_data='ty')
        mi1 = types.InlineKeyboardMarkup(row_width=2);mi1.add(mi)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*عذرا ارسل رابط صحيح من فضلك*',parse_mode='markdown',reply_markup=mi1)
#@KOK0KK



#@KOK0KK
def main():
    #@KOK0KK  
    while True:
        
        try:
            
            bot.polling()
            
        except:
            import os
            os.system('clear')
#@KOK0KK
            main()
        
        main()
        
    main()
    
main()


#حقوق @KOK0KK تخمط اضحك  فضيحه صبر شريف وخلي يوزر لمطور
#@KOK0KK
