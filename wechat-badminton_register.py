
import itchat, re
from itchat.content import *

@itchat.msg_register([TEXT],isGroupChat=True)
def text_reply(msg):
    match = re.search('地质所羽协', msg['Text'])
    zzy = re.search("张仲彦", msg['Text'])
    #error_stop = re.search("参数错误", msg['Text'])
    if (match and (not zzy) ) :
        itchat.send(('#报名a1'), msg['FromUserName'])

itchat.auto_login(True)
itchat.run()