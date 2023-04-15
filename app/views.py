from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
      #  return HttpResponse('DATA SUBMITTED SUCCESSFULLY')
    return render(request,'topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topicname=request.POST.get('topic')
        name=request.POST['name']
        url=request.POST.get('url')
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=topicname)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('DATA SUCESSFULLY ENTERED')
    return render(request,'webpage.html',d)


def insert_accessrecord(request):
    WPO=WebPage.objects.all()
    d={'web':WPO}
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST['author']
        date=request.POST.get('date')

        WO=WebPage.objects.get(name=name)
        AR=AccessRecords.objects.get_or_create(name=WO,author=author,date=date)[0]
        AR.save()
        return HttpResponse('DATA SUCESSFULLY ENTERED')

    return render(request,'access.html',d)