import requests,telebot
bot=telebot.TeleBot("#token")
send_down="bot.send_message(message.chat.id,'Wait please🔄')"
@bot.message_handler(commands=["start"])
def start(me):
    bot.send_message(me.chat.id,str("hello {} \n Welcome to github installer bot \nsend the repo url to send the files here").format(me.chat.first_name))
@bot.message_handler(func=lambda m:True)
def main(message):
    exec(send_down)
    try:
        if str(message.text).endswith("/"):
            req=req=requests.get(f"{message.text}archive/refs/heads/main.zip")
            if not req.text=="404: Not Found":
                with open("test.zip","wb") as f:
                    f.write(req.content)
                with open("test.zip","rb") as w:
                    bot.send_document(message.chat.id,w)
            else:
                req=requests.get("{}archive/refs/heads/master.zip".format(message.text))
                with open("test.zip","wb") as f:
                    f.write(req.content)
                with open("test.zip","rb") as l:
                    bot.send_document(message.chat.id,l)
        if not str(message.text).endswith("/"):
             req=req=requests.get(f"{message.text}/archive/refs/heads/master.zip")
             if not req.text=="404: Not Found":
                 with open("test.zip","wb") as f:
                     f.write(req.content)
                 with open("test.zip","rb") as w:
                     bot.send_document(message.chat.id,w)
             else:
                 req=requests.get("{}archive/refs/heads/master.zip".format(message.text))
                 with open("test.zip","wb") as f:
                    f.write(req.content)
                 with open("test.zip","rb") as l:
                    bot.send_document(message.chat.id,l)
    except :
        bot.send_message(message.chat.id,"Erorr")
bot.polling()
