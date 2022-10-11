from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import bomber
from get_info.get_information import get_information

class MainTest(MDScreen):
    def start_spam(self):
        get_phone = self.ids.enter_phone.text
        get_minutes = self.ids.minutes.text
        
        if '380' not in get_phone or get_phone == '':
            self.ids.start_spam_info.text = 'Не правильно введено номер'
        
        elif get_minutes == '':
            self.ids.start_spam_info.text = 'Введи хвилини'
            
        elif int(get_minutes) > 10:
            self.ids.start_spam_info.text = 'Воу-воу куда розігнався тигр?'
            
        else:
            get_inf = get_information(get_phone)
            self.ids.start_spam_info.text = 'Спам почався'
            
            self.ids.operator.text = f'Оператор: {get_inf[0]}'
            self.ids.country.text = f'Країна: {get_inf[1]}'
            self.ids.geo.text = f'Приблизна геолокація: {get_inf[2][0]}'
        
            #bomber.start(get_phone,get_minutes)
        
class FirstApp(MDApp):
    def build(self):
        self.icon = 'logo.png'
        self.theme_cls.theme_style = 'Dark'
        return MainTest()

FirstApp().run()
