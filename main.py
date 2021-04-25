# -*- coding: utf8 -*-
# python >=3.7

import requests

sckey = ''
login_cookie = ''
signin_cookie = ''
auth_refresh_url = ''

Referer = 'https://v.qq.com'
Agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers_login = {
  'User-Agent': Agent,
  'Cookie': login_cookie,
  'Referer': Referer
}

# 测试一个签到请求
login = requests.get(url=auth_refresh_url, headers=headers_login)
cookie = requests.utils.dict_from_cookiejar(login.cookies)
# 如果请求返回信息包含no login说明cookie已经失效
if not cookie:
    print("auth_refresh error")
    send_url = f"https://tdtt.top?alias={sckey}&title=腾讯视频签到失败&content=获取Cookie失败，Cookie失效"
    requests.get(send_url)

urls = [
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694',
    # 下载签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385',
    # 签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765 ',
    # 弹幕签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=Zepto1582997031843',
    # 观看60分钟签到
]
count = 0
resultContent = ''
for url in urls:
    count += 1
    if (count == 1):
        print("发送每日下载任务请求")
    elif (count == 2):
        print("发送每日签到任务请求")
    elif (count == 3):
        print("发送每日弹幕任务请求")
    elif (count == 4):
        print("发送每日观影60分钟任务请求")
    refresh_cookie = cookie['vqq_vusession']
    headers_signin = {
      'User-Agent': Agent,
      'Cookie': signin_cookie + refresh_cookie + ';_video_qq_vusession=' + refresh_cookie + ';',
      'Referer': Referer
    }
    response = requests.get(url=url, headers=headers_signin)
    responseContent = response.content.decode("utf-8")
    print(responseContent)
    resultContent += responseContent + '\n\n'

send_url = f"https://tdtt.top?alias={sckey}&title=腾讯视频签到&content={resultContent}"
requests.get(send_url)
print('已推送到mipush')
