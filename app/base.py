#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import tornado.websocket
import uuid
import logging
import tornado.escape
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("user", str(uuid.uuid4()))
        self.render("index.html", messages=ChatSocketHandler.cache)

class TalkPair:
    talkerOne = null
    talkerTwo = null
    conversation = []

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    lonely = []
    talkpair = []
    cache = []
    cache_size = 200

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def open(self):
        print self.get_secure_cookie("user")
        print "new client opened"
        self.cookie = self.get_secure_cookie("user")
        if (len(lonely) > 0):
            pair = new TalkPair()
            pair.talkerOne = lonely[0]
            pair.talkerTwo = self
            remove_lonely[0]
        else:
            lonely.Append(self)
            
    def on_close(self):
        fine_self_and_remove

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        if self in lonely:
            waiter.write_message("you are alone")
        else:
            the_pair = get_the_pair
            the_pair.talkerOne.write_message(message)
            the_pair.talkerTwo.write_message(message)
