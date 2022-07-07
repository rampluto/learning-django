from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello,Django World!")



# Create your views here.
