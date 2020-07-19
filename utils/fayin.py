import requests

def get_mp3(word):
    url="http://dict.youdao.com/dictvoice?audio={}&type=1".format(word)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    r=requests.get(url,headers=headers)
    print(type(r.content))
    with open("static/{}.mp3".format(word),"wb") as f:
        f.write(r.content)
if __name__=="__main__":
    get_mp3("common")