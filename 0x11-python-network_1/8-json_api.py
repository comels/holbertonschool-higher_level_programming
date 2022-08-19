#!/usr/bin/python3
"""script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""


if __name__ == "__main__":

    import requests
    from sys import argv

    letter = {"q": ""} if len(argv) == 1 else {"q": argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=letter)

    

