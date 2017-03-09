import requests
import whois
from datetime import datetime, timedelta


def load_urls4check(path):
    with open(path, 'r') as file:
        content = file.read()
        urls = content.split('\n')
    return urls


def is_server_respond_with_200(url):
    request = requests.get(url)
    status_code = request.status_code
    if status_code == 200:
        return True
    return False


def get_domain_expiration_date(domain_name):
    domain = whois.whois(domain_name)
    domain_expiration_date = domain['expiration_date'][0]
    return domain_expiration_date


def get_date_difference(expiration_date):
    date_now = datetime.now()
    date_difference = expiration_date - date_now
    return date_difference


def output_to_console(url, http_status, date_difference):
    print()
    print(url)
    if http_status:
        print('HTTP Status: OK!')
    else:
        print('HTTP Status: Error!')
    print('Registration term of the domain expires after {0}.'.format(date_difference))
    print()
    print('#' * 80)


if __name__ == '__main__':
    file_path = input('Enter a path to the file: ')
    urls = load_urls4check(file_path)
    for url in urls:
        http_status = is_server_respond_with_200(url)
        expiration_date = get_domain_expiration_date(url)
        date_difference = get_date_difference(expiration_date)
        output_to_console(url, http_status, date_difference)
