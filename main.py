from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import bomber
from get_info.get_information import get_information


class MainTest(FloatLayout):
    def press(self):
        self.get_phone = self.ids.phone.text
        get_phone = self.get_phone
        if '380' not in get_phone:
            print('ЧООООООООООО')
            self.ids.start_bomb.text = 'Не правильно введено номер!'
        elif len(get_phone) == 12 and '380' in get_phone:
            self.ids.start_bomb.text = 'Спам почався!'
            phone_inf = get_information(get_phone)
            
            self.ids.operator.text = f'Оператор: {phone_inf[0]}'
            self.ids.country.text = f'Країна: {phone_inf[1]}'
            self.ids.geo.text = f'Приблизна геолокація: {phone_inf[2][0]}'
            
            bomber.start(get_phone)
        else:
            print('ПОМИЛКА')
        
        

class FirstApp(App):
    def build(self):
        return MainTest()

FirstApp().run()