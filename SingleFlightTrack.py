import requests;
import json;
import time;
import urllib
import smtplib
from email.mime.text import MIMEText

def check_price() :
    headers = {
        'Host': "ijipiao.jd.com",
        'Accept-Language': "zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7",
        'Accept-Encoding': "gzip, deflate",
        'X-Requested-With' : 'XMLHttpRequest',
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "http://ijipiao.jd.com"
}

    body = {
        'journeyType' : "OW",
        'gjdepCity' : "悉尼",
        'gjarrCity' : "武汉",
        'gjdepDate': "2019-11-21",
        'gjarrDate': "2019-11-22",
        'directOnly': "false",
        'seatType': "ECONOMY",
        'adtNum': "1",
        'carrierShow': "不限",
        'carrier': "",
        'source': "5",
}

    headers['Referer'] = str("http://ijipiao.jd.com/international/query.action?_charset_=gbk&") +  urllib.parse.urlencode(body)



    #获取uuid
    captcha_url = 'http://ijipiao.jd.com/captcha/risk'
    captcha = requests.post(captcha_url , headers = headers)

#获取multiQueryKey
    headers['Cookie'] = "airplane_captcha_normal_user=" + captcha.cookies["airplane_captcha_normal_user"]

    multiQueryKey_url = "http://ijipiao.jd.com/international/doQuery.action?_charset_=utf-8"
    multiQueryKey = requests.post(multiQueryKey_url , headers = headers , data = body)
    body['requestUuid'] =  multiQueryKey.json()["requestUuid"]
    body['finished'] = "false"
    body['resultTag'] = "false"


    flight_url = "http://ijipiao.jd.com/international/doQuery.action?_charset_=utf-8"
    flight_information = requests.post(flight_url , headers = headers , data = body)

    page = flight_information.json()['results']


    for plan in page:
        if plan["transferCountType"] == "0" :
                journey = ""
                flight_cheapest = 9999999
                # for flights in plan["availableJourneys"][0]["airFlights"] :
                #         journey += flights["airCarrierCorName"] + flights["airLine"] + flights["airFlightNo"]
                for prices in plan["cabinGroups"] : 
                        if prices["totalAmount"] < flight_cheapest :
                                flight_cheapest = prices["totalAmount"]
                return flight_cheapest

                # duration_Array = plan["availableJourneys"][0]["duration"].split(':')
                # flight_duration = duration_Array[0] + '小时' + duration_Array[1] +'分'
                # print(journey + "--" + "最低价格为" + str(flight_cheapest) + "------飞行总时长:" + flight_duration)

mail_host = 'smtp.qq.com'  
#163用户名
mail_user = '5996013'  
#密码(部分邮箱为授权码) 
mail_pass = 'joboxjuuoqzobjgg'   
#邮件发送方邮箱地址
sender = '5996013@qq.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['5996013@qq.com']  

#设置email信息

preset_price = 3000

def send_email():
    now_price = check_price()
    now_price = check_price()
    now_price = check_price()
    if now_price < preset_price :
        #邮件内容设置
        message = MIMEText("价格已低于预设值，价格为：" + str(now_price),'plain','utf-8')
        #邮件主题       
        message['Subject'] = '机票追踪' 
        #发送方信息
        message['From'] = sender 
        #接受方信息     
        message['To'] = receivers[0]
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj = smtplib.SMTP_SSL(mail_host)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('成功！')
    else:
        print('最低价格未低于预设值')
# except smtplib.SMTPException as e:
#     print('error',e) #打印错误

def test():
    print("HelloWorld")