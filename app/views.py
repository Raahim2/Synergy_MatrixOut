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

# your_app/views.py

def index(request):
    # 1. Define a default context for the initial (GET) page load.
    #    This sets the flag to False and prevents template errors.
    context = {
        'form_submitted': False,
        'url': '',
        'title': '',
        'vern': '',
        'ip': '',
        'exr': '',
        'csrf': '',
        'xss': '',
        'sql': '',
    }

    if request.method == "POST":
        url = request.POST.get('text')
        
        # --- Your scanning logic (this remains the same) ---
        title = functions.gettitle(url)
        vern = functions.check_vulnerability(remove_http(url), 80)
        ip = functions.getip(remove_http(url))
        css, js = functions.count_external_resources(url)
        exresour = f"CSS = {css} and JS = {js}"
        csrf = functions.detect_csrf(url)
        xss = functions.check_xss(url)
        sql = functions.is_sql_injection(url)

        # 2. Update the context with the scan results AND
        #    set the crucial 'form_submitted' flag to True.
        context = {
            'form_submitted': True,
            'url': url,
            'title': title,
            'vern': vern,
            'ip': ip,
            'exr': exresour,
            'csrf': csrf,
            'xss': xss,
            'sql': sql,
        }

    # 3. Use a single render call at the end. This will send the
    #    correct context (either default or with results) to the template.
    return render(request, 'index.html', context)