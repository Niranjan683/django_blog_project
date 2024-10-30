from django.shortcuts import render

def custom_page_not_found(request,exeception):
    return (request,'404.html')
