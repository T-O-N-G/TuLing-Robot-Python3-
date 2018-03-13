import json
import requests
apiKey='63a7bc****************'
userId='23****'

# 我只需要传入文字，如果你需要其他的，自己添加参数传入
def robot(content):
    try:
        url = "http://openapi.tuling123.com/openapi/api/v2"
        reqType = 0
        # 传入的图片地址 可以为空
        inputImage = {'url': ''}
        # 请求的地理位置 可以为空
        selfInfo = {'location': {'city': '', 'province': '', 'street': ''}}
        inputText = {'text': content}
        perception = {'inputText': inputText,
                      'inputImage': inputImage, 'selfInfo': selfInfo}
        userInfo = {'apiKey': apiKey,
                    'userId': userId}
        payload = {'reqType': reqType,
                   'perception': perception, 'userInfo': userInfo}
        r = requests.post(url, data=json.dumps(payload))
        rp = json.loads(r.text)
        tuling = rp['results'][0]['values']['text']
        # 图灵机器人在不会回答的时候，会学用户说一句话
        if tuling == content:
            tuling = '老娘不会啊'
    # 各种错误，懒得写2333
    except Exception as err:
        tuling = '哎呀，出错了'
    return tuling


while True:
    ask = input("我:")
    result = "机器人:"+robot(ask)
    print(result)
