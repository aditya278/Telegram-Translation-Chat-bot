import requests
import json
import configparser as cfg

class telegramBot():

    def __init__(self, config):
        self.token = self.read_from_config_file(config)
        self.basePath = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset = None):
        url = self.basePath + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        req = requests.get(url)
        print(url)
        return json.loads(req.content)

    def send_message(self, msg, chat_id):
        url = self.basePath + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        print(url)
        if msg is not None:
            requests.get(url)
        
    def read_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')
