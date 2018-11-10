import requests


proxies = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}


def main():
    url = 'http://ifconfig.me/ip'

    response = requests.get(url)
    print('ip: {}'.format(response.text.strip()))

    response = requests.get(url, proxies=proxies)
    print('tor ip: {}'.format(response.text.strip()))


if __name__ == '__main__':
    main()