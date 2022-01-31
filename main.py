#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("An online String Session Generator")
#Starting of repl to generate your string session.
print()
print("p ==> Pyrogram (docs.pyrogram.org)")
#Pyrogram 

print("t ==> Telethon (docs.telethon.dev)")
#Telethon 
print()
print("Select your required option: ")
#option is from pyrogram and telethon
print()
s_l = input("enter p / t ? ?? ")
#p is for pyrogram and t is for telethon

if s_l == "p":
    print("You selected Pyrogram")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")
    import pyrogram
    with pyrogram.Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
        session_str = app.export_session_string()
        s_m = app.send_message("me", session_str)
        s_m.reply_text(
            "⬆️ This StringSession is generated using https://replit.com/@QueenArzoo/VCPlayBot \nCredits @LaylaList Support @AwesomeSupport  ",
            quote=True)
        print(
            "Please check your Telegram Saved Messages for the String Session "
        )

elif s_l == "t":
    print("you selected Telethon")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        session_str = client.session.save()
        s_m = client.send_message("me", session_str)
        s_m.reply(
            "⬆️ This StringSession is generated using https://replit.com/@QueenArzoo/VCPlayBot! \nCredits @LaylaList Support @AwesomeSupport "
        )
        print(
            "please check your Telegram Saved Messages for the String Session "
        )

else:
    print("?? please select only p / t, ") 