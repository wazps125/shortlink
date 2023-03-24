from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
import pyperclip as pc

# Create your views here.
def home(request):
    return render(request,'sortapp/home.html')
def copy(request):
    url = request.GET.get('inputlink')
    s = pyshorteners.Shortener()
    cp_link = s.tinyurl.short(url)
    pc.copy(cp_link)
    return render(request,'sortapp/cp.html',{"copy_link":cp_link})
