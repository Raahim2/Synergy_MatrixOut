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
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror as e:
        return f"Error: {e}"

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

def check_xss(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all input fields and iterate over them
    for input_field in soup.find_all('input'):
        # Check if the input field has an attribute vulnerable to XSS
        if 'value' in input_field.attrs:
            messege =  f"Potential XSS vulnerability found in input field: {input_field}"
            return messege
    
    # Find all output contexts (e.g., HTML tags) and iterate over them
    for output_context in soup.find_all():
        # Check if the output context contains user-controlled data
        if output_context.string:
            # Here, you can add more sophisticated checks to detect potential XSS
            if "<script>" in output_context.string:
                messege =  f"Potential XSS vulnerability found in output context: {output_context}"
                return messege

import sqlite3

def is_sql_injection(query):
    # Sample vulnerable SQL query
    vulnerable_query = "SELECT * FROM users WHERE username='%s' AND password='%s'"

    # Parameters to test for SQL injection
    malicious_input = ["' OR '1'='1", "' OR '1'='1' --"]

    for malicious_param in malicious_input:
        test_query = vulnerable_query % (malicious_param, malicious_param)
        if query.lower() in test_query.lower():
            return "Potential SQL injection detected!"
    return "Query seems safe."



is_sql_injection('https://www.google.com?')