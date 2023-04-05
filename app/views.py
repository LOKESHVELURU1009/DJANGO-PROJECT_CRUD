from django.shortcuts import render


from app.models import *

# Create your views here.
def display_topic(request):

    LOT=Topic.objects.all()
    d={'topics' : LOT}


    return render(request,'display_topic.html',context=d)