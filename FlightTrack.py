import requests;
import json;
import time;
import urllib
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
    'gjdepCity' : str(input("请输入出发城市:")),
    'gjarrCity' : str(input("请输入到达城市:")),
    'gjdepDate': str(input("请输入出发日期（格式YYYY-MM-DD）:")),
    'gjarrDate': str(input("请输入到达日期（格式YYYY-MM-DD）:")),
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
    journey = ""
    flight_cheapest = 9999999
    for flights in plan["availableJourneys"][0]["airFlights"] :
        journey += flights["airCarrierCorName"] + flights["airLine"] + flights["airFlightNo"]
    for prices in plan["cabinGroups"] : 
        if prices["totalAmount"] < flight_cheapest :
            flight_cheapest = prices["totalAmount"]
    duration_Array = plan["availableJourneys"][0]["duration"].split(':')
    flight_duration = duration_Array[0] + '小时' + duration_Array[1] +'分'
    print(journey + "--" + "最低价格为" + str(flight_cheapest) + "------飞行总时长:" + flight_duration)

