import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the hostname."

if __name__ == "__main__":
    url = input("Enter the URL: ")
    ip_address = get_ip_address(url)
    print("IP Address:", ip_address)


def count_signs(url):
    signs = {
        'dots': '.',
        'hyphens': '-',
        'at': '@',
        'qm': '?',
        'and': '&',
        'or': '|',
        'equal': '=',
        'underscore': '_',
        'tilde': '~',
        'percent': '%',
        'slash': '/',
        'star': '*',
        'colon': ':',
        'comma': ',',
        'semicolumn': ';',
        'dollar': '$',
        'space': ' ',
        'www': 'www',
        'com': '.com',
        'dslash': '//',
        'http_in_path': 'http://',
        'https_token': 'https://',
      
    }
    
    counts = {key: url.count(value) for key, value in signs.items()}
    return counts

sign_counts = count_signs(url)

print("Counts of signs in the URL:")
for sign, count in sign_counts.items():
    print(f"{sign}: {count}")

def digit_ratio(url):
    total_chars = len(url)
    digit_count = sum(1 for char in url if char.isdigit())
    if total_chars == 0:
        return 0  # Avoid division by zero
    return digit_count / total_chars

if __name__ == "__main__":

    ratio = digit_ratio(url)
    print("Ratio of digits in the URL:", ratio)


    from urllib.parse import urlparse

def host_digit_ratio(url):
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    digit_count = sum(1 for char in host if char.isdigit())
    total_chars = len(host)
    if total_chars == 0:
        return 0  # Avoid division by zero
    return digit_count / total_chars

if __name__ == "__main__":
  
    ratio = host_digit_ratio(url)
    print("Ratio of digits in the host part of the URL:", ratio)

    from urllib.parse import urlparse
import idna

def count_punycode(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')  # Split the domain into parts
    punycode_count = sum(1 for part in domain if part.startswith("xn--"))
    return punycode_count

if __name__ == "__main__":
 
    punycode_count = count_punycode(url)
    print("Number of Punycode-encoded parts in the URL:", punycode_count)

    from urllib.parse import urlparse

def get_port(url):
    parsed_url = urlparse(url)
    if parsed_url.port is not None:
        return parsed_url.port
    elif parsed_url.scheme == 'http':
        return 80
    elif parsed_url.scheme == 'https':
        return 443
    else:
        return None

if __name__ == "__main__":

    port = get_port(url)
    if port:
        print("Port of the URL:", port)
    else:
        print("Port not specified or not supported in the URL.")


from urllib.parse import urlparse

def find_tilde_in_path(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    tilde_count = path.count('~')
    return tilde_count

if __name__ == "__main__":

    tilde_count = find_tilde_in_path(url)
    print("Number of tildes (~) in the URL path:", tilde_count)

    from urllib.parse import urlparse

def find_tilde_in_subdomain(url):
    parsed_url = urlparse(url)
    subdomain = parsed_url.hostname.split('.')[0]
    tilde_count = subdomain.count('~')
    return tilde_count

if __name__ == "__main__":
    tilde_count = find_tilde_in_subdomain(url)
    print("Number of tildes (~) in the subdomain of the URL:", tilde_count)


from urllib.parse import urlparse

def count_subdomains(url):
    parsed_url = urlparse(url)
    subdomains = parsed_url.hostname.split('.')
    return len(subdomains) - 2  # Subtract 2 for the main domain and top-level domain

if __name__ == "__main__":
    num_subdomains = count_subdomains(url)
    print("Number of subdomains:", num_subdomains)






