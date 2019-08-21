from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request): # 定义站点首页视图函数
    return render(request,'index.html')  #调用模版返回页面内容

#def news_list(request,news_type):
	#news_dict = {'economic': '经济', 'sport':'体育'} #创建参数字典
	#return render(request,'news_list.html',{'news_type':news_dict[news_type]})
	# 整合数据并返回页面内容
	#news_titles=[]
    #if news_type == 'economic':
        #news_titles = [('12/5','Darer'),('12/4','JackMa'),('12/3','PonyMa'),('12/2','HongKong')]
    #return render(request,'news_list.html',{'news_type':'news_dict[news_type]','news_titles':'news_titles'})

#def filter_test(request):
    #return render(request,'filter.html',{'letters':'abc','number':'1'}) 


