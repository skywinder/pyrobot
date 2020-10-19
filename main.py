# from pyrogram import Client
#
# with Client("my_account", api_id, api_hash) as app:
#     app.send_message("me", "Greetings from **Pyrogram**!")

from pyrogram import Client

app = Client("my_account")
app.run()
