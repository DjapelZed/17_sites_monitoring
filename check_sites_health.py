import requests
import whois
from datetime import datetime 


def load_urls4check(path):
    with open(path, 'r') as file:
    	content = file.read()
    	urls = content.split('\n')
    	print(urls)
    return urls


def is_server_respond_with_200(url):
    request = requests.get(url)
    status_code = request.status_code
    print(status_code)
    if status_code == 200:
    	return True
    return False


def get_domain_expiration_date(domain_name):
    domain = whois.query(domain_name)
    domain_inspiration_date = domain['expiration_date']
    print(domain_inspiration_date)


if __name__ == '__main__':
    file_path = input('Введи путь к файлу с сайтами: ')
    urls = load_urls4check(file_path)
    for url in urls:
    	print(url)
    	http_status = is_server_respond_with_200(url)
    	get_domain_expiration_date('google.com')