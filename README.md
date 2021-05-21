# Discord Moderation Bot
> This project was made by Kingman and written in Python using the Discord library

It is a simple administrative bot that contains a number of administrative commands that work with specific Roles **(RoleID)** on the server

------------

- Step 1
clone the project
```py
git clone https://github.com/MeKINGMAN/MyDiscordModBot
```
- Step 2
Now you have to upload files to a hosting provider to run the files 7/24h
LIKE http://repl.it/
Or you can shorten the time and click here [AUTO CLONE TO REPLIT](https://replit.com/github/MeKINGMAN/MyDiscordModBot)
- Step 3
Go  to **.replit** File and Paste the
```
language = "python3"
run = "python main.py"
```
- Step 4
make a **.env** File and paste This Info
```
# your bot token
TOKEN        = Yor Bot Token
# support role
# can active members / clear chat / lock channel / mute members /set nick / warn
SUPPORT_ROLE = 826543776360038421
# member role
MEMBER_ROLE = 826543779678781511
#admine role
# can kick & ban & addrole
ADMINE_ROLE = 826543777355005982
# ban log
BAN_LOG = 826543748120051755 
#black list manager
# can add blacklist role
BLACK_LIST_MANAGER = 826543776067485736 
# black list role
BLACK_LIST_ROLE = 826535037197353010
# black list log
BLACK_LIST_LOG = 826543748120051755
# kick log
KICK_LOG = 826543748120051755
# the mute role
MUTE_ROLE = 826543778508701697
# add role log
ADD_REMOVE_ROLES_LOG = 826543748120051755
# warn log
WARN_LOG = 826543748120051755
# mute log 
MUTELOG = 826543748120051755
```
- Step 5 
add this Code To Main.py file
```
from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
    return "KMCodes!"
def run():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()
keep_alive()
```

------------

# بوت سيستم ديسكورد
> تم إنشاء هذا المشروع بواسطة Kingman وكُتب بلغة Python باستخدام مكتبة Discord

هو روبوت إداري بسيط يحتوي على عدد من الأوامر الإدارية التي تعمل مع أدوار معينة (دوريد) على الخادم

------------

- الخطوه الاولى 
انسخ البروجيكت على جهازك عبر الامر الاتي 
```
git clone https://github.com/MeKINGMAN/First-ModerationBot
```
- الخطوة الثانية
عليك رفع البوت على خادم لكي يعمل البوت 24 اعة انا انصحك بريبل ات او اختصر الخطوة الاولى عبر الضغط هنا 
 [AUTO CLONE TO REPLIT](https://replit.com/github/MeKINGMAN/First-ModerationBot)
 
- الخطوة الثالثة
 عليك الذهاب الى ملف **.replit ** ولصق المعلومات 
 ```
 language = "python3"
run = "python main.py"
 ```
- الخطوة الرابعة 
عليك انشاء ملف باسم **.env**
ولصق هذا الكود 
```
# your bot token
TOKEN        = Yor Bot Token
# support role
# can active members / clear chat / lock channel / mute members /set nick / warn
SUPPORT_ROLE = 826543776360038421
# member role
MEMBER_ROLE = 826543779678781511
#admine role
# can kick & ban & addrole
ADMINE_ROLE = 826543777355005982
# ban log
BAN_LOG = 826543748120051755 
#black list manager
# can add blacklist role
BLACK_LIST_MANAGER = 826543776067485736 
# black list role
BLACK_LIST_ROLE = 826535037197353010
# black list log
BLACK_LIST_LOG = 826543748120051755
# kick log
KICK_LOG = 826543748120051755
# the mute role
MUTE_ROLE = 826543778508701697
# add role log
ADD_REMOVE_ROLES_LOG = 826543748120051755
# warn log
WARN_LOG = 826543748120051755
# mute log 
MUTELOG = 826543748120051755
```
وعليك استبدال المعلومات الموجوده 
- الخطوة الخامسة 
اذهب الى ملف main.py
و قم بلصق هذه المعلومات
```
from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
  return "KMCodes!"
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()
keep_alive()
```


