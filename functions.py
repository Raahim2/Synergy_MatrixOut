from bs4 import BeautifulSoup
import requests
import socket
from urllib.parse import urlparse


def gettitle(url):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.title 

def check_vulnerability(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(2)

        result = s.connect_ex((host, port))
        
        if result == 0:
            messege = f"Port {port} on {host} is open"
        else:
            messege = f"Port {port} on {host} is closed"
        
        s.close()
    except socket.error as e:
        messege = f"Error: {e}"

    return messege

def getip(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def count_external_resources(url):
    """
    This function counts the number of external CSS and JavaScript files used in a URL.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad response status

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract links to CSS and JavaScript files
        css_files = [link['href'] for link in soup.find_all('link', rel='stylesheet') if link.get('href')]
        js_files = [script['src'] for script in soup.find_all('script', src=True)]

        # Filter out external resources
        parsed_url = urlparse(url)
        external_css = [css for css in css_files if urlparse(css).netloc != '' or urlparse(css).scheme != '']
        external_js = [js for js in js_files if urlparse(js).netloc != '' or urlparse(js).scheme != '']

        # Return the count of external resources
        return len(external_css), len(external_js)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def detect_csrf(url):
    response = requests.get(url)
    if "anti-csrf-token" in response.headers:
        messege= "CSRF Protection Detected"
    else:
        messege = "CSRF Vulnerability Possibly Detected"
    return messege

print(gettitle('http://google.com'))
print(check_vulnerability("www.google.com" ,80))
print(getip('www.google.com'))
css,js=count_external_resources('http://github.com')
print(f"CSS = {css} and JS = {js}")
print(detect_csrf('http://google.com'))
