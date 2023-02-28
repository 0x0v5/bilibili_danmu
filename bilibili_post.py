import time
import random
import requests
import json





class SendLiveRoll():
    def __init__(self, roomid=None):
        self.roomid = roomid
        self.index = 0
        self.url2 = 'https://api.live.bilibili.com/msg/send'

        # 默认使用小号
        self.csrf = '60dc07b30a01032284508bbee8825565'
        self.cookie = {'Cookie':'buvid3=85FA413D-65D8-4A44-1349-F7A65788534175345infoc; b_nut=1666096175; i-wanna-go-back=-1; _uuid=10C118CD10-5737-948C-4C42-224D12D7368989520infoc; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=0zbfvRPVwI|12KgNhpYb|4F|3w1OX8RT; LIVE_BUVID=AUTO5016699800347377; CURRENT_QUALITY=120; buvid4=8F832112-D680-C648-E44C-082899304B0732787-022020317-w62HZ4YiZO8ao4IZgsEyTqm9n2q1RBLq/51XLLw9aazJIZzBQQNxXg==; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; _dfcaptcha=96d47a686f425f19f7a0f6f3e51a1e3d; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1677415701,1677424170; innersign=0; b_lsid=8D31039D2_1868E54769B; bsource=search_bing; bp_video_offset_406276286=767021025462321300; b_ut=7; fingerprint=ca2ec8457fb43fa81d76ef15dc160708; SESSDATA=1c25d48b,1692977333,2a64b*22; bili_jct=60dc07b30a01032284508bbee8825565; DedeUserID=3493143567665318; DedeUserID__ckMd5=93cee22220a03683; sid=5gj6m333; buvid_fp=ca2ec8457fb43fa81d76ef15dc160708; PVID=11'}
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
        self.timestamp = int(time.time())
        # self.msg = msg

    def sendLiveRoll(self,msg='666'):
        #self.msg = msg
        
        # 开两个账户
        if self.index % 2 == 0:
            self.csrf = '60dc07b30a01032284508bbee8825565'
            self.cookie = {'Cookie':'buvid3=85FA413D-65D8-4A44-1349-F7A65788534175345infoc; b_nut=1666096175; i-wanna-go-back=-1; _uuid=10C118CD10-5737-948C-4C42-224D12D7368989520infoc; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=0zbfvRPVwI|12KgNhpYb|4F|3w1OX8RT; LIVE_BUVID=AUTO5016699800347377; CURRENT_QUALITY=120; buvid4=8F832112-D680-C648-E44C-082899304B0732787-022020317-w62HZ4YiZO8ao4IZgsEyTqm9n2q1RBLq/51XLLw9aazJIZzBQQNxXg==; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; _dfcaptcha=96d47a686f425f19f7a0f6f3e51a1e3d; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1677415701,1677424170; innersign=0; b_lsid=8D31039D2_1868E54769B; bsource=search_bing; bp_video_offset_406276286=767021025462321300; b_ut=7; fingerprint=ca2ec8457fb43fa81d76ef15dc160708; SESSDATA=1c25d48b,1692977333,2a64b*22; bili_jct=60dc07b30a01032284508bbee8825565; DedeUserID=3493143567665318; DedeUserID__ckMd5=93cee22220a03683; sid=5gj6m333; buvid_fp=ca2ec8457fb43fa81d76ef15dc160708; PVID=11'}
        else :
            self.csrf = 'c6671b17e3ab4ae5254e4dd26303eef9'
            self.cookie = {'Cookie':'i-wanna-go-back=-1; LIVE_BUVID=AUTO6816426526984652; CURRENT_BLACKGAP=0; buvid4=F1A0813C-DB2C-C2F2-CEA3-CBF03CB0C4BE88839-022022822-Q3aqzyFXT2hKwP1R8gLCqw%3D%3D; blackside_state=0; buvid_fp_plain=undefined; DedeUserID=406276286; DedeUserID__ckMd5=07e887690bcb113e; b_ut=5; nostalgia_conf=-1; CURRENT_QUALITY=120; CURRENT_FNVAL=4048; rpdid=0zbfvRPVwH|t2Aj2lV|4Fab|3w1OYwEZ; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1669375039; fingerprint=21fdd0a4f3c5a627cdbeabc78ae9461b; buvid_fp=21fdd0a4f3c5a627cdbeabc78ae9461b; innersign=0; buvid3=FBF38D24-B1D1-733A-82A1-0B6952C36F3C77004infoc; b_nut=1677417377; b_lsid=AAA36BD10_1868DDDF61A; _uuid=F7764A42-106A8-327E-D799-AA3104BB5E76779365infoc; header_theme_version=undefined; home_feed_column=5; SESSDATA=1b09f15e%2C1692969379%2C4d7f2%2A22; bili_jct=c6671b17e3ab4ae5254e4dd26303eef9; sid=qhrro7qk; _dfcaptcha=59473580dbd5982b79fbde0775a9a6a8; PVID=2; bp_video_offset_406276286=766987279866527700'}
        
        self.index += 1
        self.msg = msg
        data = {
            'bubble':0,
            'color': 14423100,
            'fontsize': 25,
            'mode': 1,
            'msg': self.msg,
            'rnd': self.timestamp,
            'roomid': self.roomid,
            'csrf':self.csrf,
            'csrf_token': self.csrf
        }
        print('send:',self.index, self.msg)
        # print(self.cookie)
        html = requests.post(self.url2, data=data, cookies=self.cookie, headers=self.header)
        
        try:
            json_dict = json.loads(html.text)
            if json_dict['code'] == 0:
                print('send success')
            else :
                print('recv:',json_dict['message'])
        except Exception:
            print(html.text)
            exit()



if __name__ == "__main__":
    
    # 房间号
    lolromid = 7734200     

    Praise_list = ['666','牛b','厉害','太强了','服气','精彩','秒啊','有点东西','赞','泪目','赢麻了','打扰了']

    sendliveroll = SendLiveRoll(lolromid)

    for a in range(1000):

        # 内置的彩虹屁弹幕
        msg = random.choice(Praise_list)

        # 发送弹幕
        sendliveroll.sendLiveRoll(msg)

        # 设置时间间隔
        num = random.random() + 5
        time.sleep(num)
