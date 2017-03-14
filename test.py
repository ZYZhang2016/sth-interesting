import itchat, time, re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('地质所羽协', msg['Text']).span()
    zzy = re.search("李佩",msg['Text']).span()
    if (match and (not zzy)) :
      itchat.send(('#报名a1'), msg['FromUserName'])

itchat.auto_login(True)
itchat.run()