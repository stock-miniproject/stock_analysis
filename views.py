from django.shortcuts import render
import requests

def button(request):
    return render(request,'index.html')

def output(request):
    data = requests.get("https://reqres.in/api/users")
    print(data.text)
    data = data.text
    return render(request,'index.html',{'data':data})
    
