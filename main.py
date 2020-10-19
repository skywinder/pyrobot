from pyrogram import Client
import datetime


with Client("my_account") as app:
    now = datetime.datetime.now()
    app.send_message("me", "Greetings from **Pyrogram**! %s" % str(now)[:19] )
#
# from pyrogram import Client
#
# app = Client("my_account")
# app.run()
