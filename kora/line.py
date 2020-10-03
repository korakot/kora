import os, logging, json
from flask import Flask, request
from requests import post
from threading import Thread
os.system("pip install pyngrok")
from pyngrok import ngrok


log = logging.getLogger('werkzeug')  # Flask
log.setLevel(logging.ERROR)     # silence it


class Webhook:
    """ Line Webhook 
    
    Usage: 
    > webhook = Webhook(access_token)
    > webhook.start()   # then setup with this URL 
    > webhook.reply = lambda x: x   # just repeat
    """
    def __init__(self, access_token, port=5000):
        self.a_token = access_token
        self.port = port
        app = Flask("Line")   # to be webhook
        app.add_url_rule('/', None, self.serve, methods=['GET','POST'])
        app.add_url_rule('/shutdown', None, self.shutdown)
        self.app = app

    def shutdown(self):
        request.environ.get('werkzeug.server.shutdown')()
        return 'Server shutting down...'

    def serve(self):
        try:
            event = request.json['events'][0]
            self.event = event # save event for further
            token = event['replyToken']
            text = event['message']['text']
            self.send_reply(token, text)    
            return '{}', 200
        except:
            return "OK", 200

    def send_reply(self, token, text):
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {'Authorization': 'Bearer ' + self.a_token}
        data = {
            "replyToken": token,
            "messages":[{
                "type":"text",
                "text": self.reply(text) 
            }]
        }
        post(url, headers=headers, json=data)

    def reply(self, text):
        """ change this to what you like """
        return text

    def start(self, port=None):
        if port:
            self.port = port  # remember
        else:
            port = self.port
        url = ngrok.connect(port)
        self.url = url.replace('http', 'https')
        print(f"Webhook URL = {self.url}")
    
        self.thread = Thread(None, self.app.run, kwargs={"port":port})
        self.thread.start()

    def stop(self):
        """ must stop so many things"""
        ngrok.kill()
        os.system(f"curl 127.0.0.1:{self.port}/shutdown")
        self.thread.join()
    
########### debug mode ###########
    def debug(self, text):
        '''
          to debug, can use `self.reply = self.debug`
        '''
        return json.dumps(self.event)
        
    def debug_mode(self):
        ''' 
          to activate reployraw run
          self.debug_mode()
        '''
        self.reply = self.debug
        
