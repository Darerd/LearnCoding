# coding : utf-8

import requests,json,random

if __name__ == '__main__' :
	target = 'https://unsplash.com/napi/photos?page=6&per_page=12'
	USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]
#IP地址列表，用于设置IP代理
	IP_AGENTS = [
        "http://58.240.53.196:8080", 
        "http://219.135.99.185:8088",
        "http://117.127.0.198:8080",
        "http://58.240.53.194:8080"  
]
 
#设置IP代理    
	proxies={"http":random.choice(IP_AGENTS)} 

	headers = {
	'authority':'unsplash.com',
	'method':'GET',
	'accept-encoding':'gzip, deflate', 
	'accept-language':'zh-CN,zh;q=0.9',
	'cookie':'ugid=a78e0069ee42f28ea8f8a824c306272e5153313; _ga=GA1.2.620133948.1545994135; uuid=2c302fa0-0a8e-11e9-93e1-4399318530fc; xpos=%7B%7D; _gid=GA1.2.1057340064.1553499105; _sp_ses.0295=*; lux_uid=155349910557040462; _gat=1; _sp_id.0295=848cb8e7-b16d-4159-9d9c-8f4d0cbd03e0.1545994135.5.1553499779.1553241497.13e41f1b-f6d3-45cd-bf4b-8b6b51566319',
	'referer':'https://unsplash.com/',
	'user-agent':random.choice(USER_AGENTS)
	}
	page=6
#设置url post请求的参数
	data={
      'page':page,
      'per_page':12
      }
#requests get请求####requests 是get请求
	req = requests.get(url=target, headers=headers, proxies=proxies)
	html = json.loads(req.text)### 得到了json格式的数据
	print(html)