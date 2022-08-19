#!/usr/bin/python3
"""script that takes in a URL and
an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":

    from urllib import request, parse
    from sys import argv

    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)

    with request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
