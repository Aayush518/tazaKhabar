from django.http import HttpResponse
import datetime

def test(request):
    print("test function called")
    return HttpResponse("Hello, world. You're at the polls index."+str(datetime.datetime.now()))

def about(request):
    print("about function called")
    return HttpResponse("About page called at "+str(datetime.datetime.now()))