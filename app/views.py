from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['tn']

            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('data inserted')
        else:
            return HttpResponse('Invalid data')







    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['tn']
            na=WFDO.cleaned_data['na']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']

            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
            WO.save()
            return HttpResponse('WEbapge is created')
        else:
            return HttpResponse('Invalid')






    return render(request,'insert_webpage.html',d)













