from django.http import HttpResponse
def index(reqeust):
    return HttpResponse("We are in home page of MAC")