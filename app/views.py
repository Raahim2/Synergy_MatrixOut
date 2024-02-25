from django.shortcuts import render
from urllib.parse import urlparse
import functions

def remove_http(url):
    if url.startswith("http://"):
        return url[len("http://"):]
    elif url.startswith("https://"):
        return url[len("https://"):]
    else:
        return url

def index(request):
    if request.method=="POST":
        url = request.POST.get('text')
        title = functions.gettitle(url)
        vern = functions.check_vulnerability(remove_http(url) , 80)
        ip = functions.getip(remove_http(url))
        css , js = functions.count_external_resources(url)
        exresour= f"CSS = {css} and JS = {js}"
        csrf = functions.detect_csrf(url)

        context = {
        'url': url,
        'title': title , 
        'vern' : vern,
        'ip':ip,
        'exr':exresour,
        'csrf':csrf
    }



        
        return render(request , 'index.html'  , context)
    return render(request , 'index.html' )