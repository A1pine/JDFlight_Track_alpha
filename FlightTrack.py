import requests;
import json;

captcha_headers = {
    'Host': "ijipiao.jd.com",
    'Accept-Language': "zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7",
    'Accept-Encoding': "gzip, deflate",
    'X-Requested-With' : 'XMLHttpRequest',
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'Referer': "http://ijipiao.jd.com/international/query.action?_charset_=gbk&journeyType=OW&gjdepCity=%E6%82%89%E5%B0%BC(%E6%BE%B3)&gjdepCityCode=SYD&gjarrCity=%E6%AD%A6%E6%B1%89&gjarrCityCode=WUH&gjdepDate=2019-11-21&gjarrDate=2019-11-22&directOnly=true&seatType=ECONOMY&adtNum=1&chdNum=0&carrierShow=%E4%B8%8D%E9%99%90&carrier=&source=5",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Origin': "http://ijipiao.jd.com"
    #'Content-Length': "0"
}

multiQueryKey_headers = {
    'Host': "ijipiao.jd.com",
    'Accept-Language': "zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7",
    'Accept-Encoding': "gzip, deflate",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'Referer': "http://ijipiao.jd.com/international/query.action?_charset_=gbk&journeyType=OW&gjdepCity=%E6%82%89%E5%B0%BC(%E6%BE%B3)&gjdepCityCode=SYD&gjarrCity=%E6%AD%A6%E6%B1%89&gjarrCityCode=WUH&gjdepDate=2019-11-21&gjarrDate=2019-11-22&directOnly=true&seatType=ECONOMY&adtNum=1&chdNum=0&carrierShow=%E4%B8%8D%E9%99%90&carrier=&source=5",
    'Origin': "http://ijipiao.jd.com",
    'Content-Type': "application/x-www-form-urlencoded"
    #'Content-Length': "355"
}
multiQueryKey_body = {
    'journeyType' : "OW",
    'gjdepCity' : "悉尼(澳)",
    'gjdepCityCode' : "SYD",
    'gjarrCity' : "武汉",
    'gjarrCityCode':"WUH",
    'gjdepDate': "2019-11-21",
    'gjarrDate': "2019-11-22",
    'directOnly': "true",
    'seatType': "ECONOMY",
    'adtNum': "1",
    'carrierShow': "不限",
    'carrier': "",
    'source': "5"

}

flight_body = {
    'journeyType' : "OW",
    'gjdepCity' : "悉尼(澳)",
    'gjdepCityCode' : "SYD",
    'gjarrCity' : "武汉",
    'gjarrCityCode':"WUH",
    'gjdepDate': "2019-11-21",
    'gjarrDate': "2019-11-22",
    'directOnly': "true",
    'seatType': "ECONOMY",
    'adtNum': "1",
    'carrierShow': "不限",
    'carrier': "",
    'source': "5",
    'finished': "false",
    "requestUuid" : '',
    "resultTag" : 'false'
}

flight_headers = {
    'Host': "ijipiao.jd.com",
    'Accept-Language': "zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7",
    'Accept-Encoding': "gzip, deflate",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'X-Requested-With' : 'XMLHttpRequest',
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'Referer': "http://ijipiao.jd.com/international/query.action?_charset_=gbk&journeyType=OW&gjdepCity=%E6%82%89%E5%B0%BC(%E6%BE%B3)&gjdepCityCode=SYD&gjarrCity=%E6%AD%A6%E6%B1%89&gjarrCityCode=WUH&gjdepDate=2019-11-21&gjarrDate=2019-11-22&directOnly=true&seatType=ECONOMY&adtNum=1&chdNum=0&carrierShow=%E4%B8%8D%E9%99%90&carrier=&source=5",
    'Origin': "http://ijipiao.jd.com",
    'Content-Type': "application/x-www-form-urlencoded"
}
#last_session = requests.session()

#获取uuid
captcha_url = 'http://ijipiao.jd.com/captcha/risk'
captcha = requests.post(captcha_url , headers = captcha_headers)
#print (captcha.cookies["airplane_captcha_normal_user"])

#获取multiQueryKey
multiQueryKey_headers['Cookie'] = "airplane_captcha_normal_user=" + captcha.cookies["airplane_captcha_normal_user"]

#print(multiQueryKey_headers['Cookie'])

multiQueryKey_url = "http://ijipiao.jd.com/international/doQuery.action?_charset_=utf-8"
multiQueryKey = requests.post(multiQueryKey_url , headers = multiQueryKey_headers , data = multiQueryKey_body)
#print(multiQueryKey.json())
flight_body['requestUuid'] =  multiQueryKey.json()["requestUuid"]


flight_url = "http://ijipiao.jd.com/international/doQuery.action?_charset_=utf-8"
flight_information = requests.post(flight_url , headers = flight_headers , data = flight_body)

#print(flight_information.json())

#print(multiQueryKey_headers['Cookie'])
#print(flight_headers['Host'])
page = flight_information.json()['results']
#print ("一共查询到%s个航班"%(len(page)))
money_list = []
#print (page[1])
for plan in page:
    if plan['transferCountType'] == '0':
        #print (json.dumps(plan , indent=4 , ensure_ascii=False))
        #print(type(plan))
        flghtcarrier = plan["availableJourneys"][0]["airFlights"][0]["airLineName"]
        flghtcode = plan["availableJourneys"][0]["airFlights"][0]["airLine"] + plan["availableJourneys"][0]["airFlights"][0]["airFlightNo"]
        flight_price = int(plan["taxAmont"]) + int(plan["trueBasePrice"])       
        print(flghtcarrier+flghtcode+"--价格"+str(flight_price))
        #print(type(plan["activitys"]))
        #print(type(plan["availableJourneys"]))
        #print ("%s%s%s-最低价：%s"%(plan["availableJourneys"]["airFlights"]["airCarrierCorName"] , plan["availableJourneys"]["airFlights"]["airLine"] , plan["availableJourneys"]["airFlights"]["airFlightNo"] , "3864")) 

#print (len(page))