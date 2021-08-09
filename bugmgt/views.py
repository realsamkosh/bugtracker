from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return  HttpResponse('<h1>Test</h1>')
    # return  render(request,'index.html')
    name = 'Yomi'
    return  render(request,'index.html', {'name':name})