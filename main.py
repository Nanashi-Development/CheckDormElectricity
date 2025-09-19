import requests
import time
from bs4 import BeautifulSoup
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem

# Dingtalk Bot
webhook = ''
secret = ''
bot = DingtalkChatbot(webhook, secret=secret)

# Request Post Data
data_studentRoom = {
                    'openId':'None', 
                    'wxArea':'', 
                    'areaNo':'', 
                    'buildNo':'', 
                    'roomNo':'',
                    }
data_airConditionerRoom = {
                    'openId':'None', 
                    'wxArea':'', 
                    'areaNo':'', 
                    'buildNo':'', 
                    'roomNo':'',
                    }

# Request Web Address
request_address = 'https://jkschool.lsmart.cn/electric/electric_goAmount.shtml'

def message(msg, alarm=False):
    """发送钉钉消息"""
    print(msg)
    print(bot.send_text(msg=msg, is_at_all=alarm))

def get_electricity(data):
    """请求电量数据并解析"""
    try:
        resp = requests.post(url=request_address, data=data, timeout=10)
        resp.raise_for_status()
        bsd = BeautifulSoup(resp.text, 'lxml')
        ele_text = bsd.find('span', class_='font-16 elet-num')
        if ele_text is None:
            raise ValueError("未找到电量信息")
        return ele_text.text
    except Exception as e:
        raise RuntimeError(f"请求或解析失败: {e}")

def main():
    try:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        studentRoomElectricity = get_electricity(data_studentRoom)
        airConditionerRoomElectricity = get_electricity(data_airConditionerRoom)
        
        num_student = float(studentRoomElectricity.split()[0])
        num_air = float(airConditionerRoomElectricity.split()[0])

        msg = (f"Time: {now}\n"
               f"学生房间电量: {studentRoomElectricity}\n"
               f"空调房间电量: {airConditionerRoomElectricity}")
        
        if num_student < 10 or num_air < 10:
            message(msg + "\n该充电费了！\n", alarm=True)
        else:
            message(msg, alarm=False)

    except Exception as e:
        message(str(e), alarm=True)

if __name__ == "__main__":
    main()