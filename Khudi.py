#20.1
def show_messages(*spisok):
    for spi in spisok:
        print(spi)
show_messages("Привет","Как дела?","До встречи")
#20.2
def show_messages(messages):
  for message in messages:
        msg = f'{message}'
        print(msg)

def send_messages(messages,sent_message):
    while messages:
        msg = messages.pop()
        sent_message.insert(0, msg)
    for message in sent_message:
        msg = f'{message}'
        print(msg)
message = ["Здарова брат","Как ты брат?"]
sent_message = []
show_messages(message)
print('--------------------------------------------')
send_messages(message,sent_message)
#20.3
def show_messages(messages):
    for message in messages:
         msg = f"{message}"
         print(msg)
def send_messages(messages, set_messages):
     while messages:
         msg = messages.pop()
         set_messages.insert(0, msg)
         for message in set_messages:
             msg = f'{message}'
             print(msg)
message = ['Утка','Гусь','Лебедь']
set_messages = []
show_messages(message)
send_messages(message[:], set_messages)
