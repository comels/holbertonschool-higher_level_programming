#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    html = req.text

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
