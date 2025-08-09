# ===== INSTAGRAM GROUP WELCOME BOT + 24/7 FLASK SERVER =====

from instagrapi import Client
import time
from flask import Flask
from threading import Thread

# 🔒 Apna Session ID aur Group ka Thread ID yahan daalo:
SESSION_ID = "75871834464%3AEsnFdtAkmAp31T%3A3%3AAYexLdPpfb8ImBs00xWYfgxyEERZUEqqxSSuVK7upQ"
THREAD_ID = "23925784613709795"

# ================== FLASK SERVER (Keep Alive) ==================
app = Flask('')

@app.route('/')
def home():
    return "✅ Jarvis Instagram Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ================== START KEEP ALIVE SERVER ==================
keep_alive()

# ================== INSTAGRAM BOT ==================
cl = Client()
cl.login_by_sessionid(SESSION_ID)

# ✅ Get your own user ID
my_user = cl.account_info()
my_user_id = my_user.pk

last_message_id = None
print(f"🤖 Jarvis active as @{my_user.username} (ID: {my_user_id})")

while True:
    try:
        messages = cl.direct_messages(thread_id=THREAD_ID, amount=1)
        if messages:
            msg = messages[0]

            # ✅ Only reply if new message & not sent by the bot itself
            if msg.id != last_message_id and msg.user_id != my_user_id:
                sender = cl.user_info(msg.user_id)
                username = sender.username
                print(f"📨 @{username}: {msg.text}")

                reply = f"@{username}  message mat kar warna @offical__rehan_7.c ki ma xod dunga 🤣 👋"
                cl.direct_send(reply, thread_ids=[THREAD_ID])
                print(f"✅ Replied to @{username}")

                last_message_id = msg.id

        time.sleep(0.00000001)

    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(10)
