from django.shortcuts import render
from joblib import load
from urllib.parse import urlparse

def count_url(url):
    url_lower = url.lower()
    
    and_count = url_lower.count('&')
    or_count = url_lower.count('|')
    equal_count = url.count('=')

    dot_count = url.count('.')
    hyphen_count = url.count('-')
    at_count = url.count('@')
    question_mark_count = url.count('?')
    return dot_count, hyphen_count, at_count, question_mark_count , and_count , or_count , equal_count


def index(request):
    if request.method=="POST":
        url = request.POST.get('text')
        model = load('app/model.pkl')

        

        dot,hypen,at,qm,andc,orc,eql= count_url(url)

        a = model.predict([[len(url ),1,0,dot,hypen,at,qm,andc,orc,eql]])
        if(a>1):
            messege = f"unsafe"
        else:
            messege = f"safe"
        
        return render(request , 'index.html'  , {'messege': f"{url} is {messege}"})
    return render(request , 'index.html' ,  {'messege' : "Enter a url"}  )