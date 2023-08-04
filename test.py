import bs4 as BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup
from rich.progress import track
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json


domain = "https://regist.vlu.edu.vn/DangKyHocPhan"
while True:
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "_ga_0W1TYXS6P7=GS1.1.1681398369.9.1.1681399612.0.0.0; _gcl_au=1.1.692205431.1683621268; _tt_enable_cookie=1; _ttp=Wm9jBVtGHZJ8oKHfprP9VRluBqg; _fbp=fb.2.1684477645488.2012274824; __uidac=8f0645aee2928d492375de9925a0b718; _ga=GA1.1.253121138.1665078590; _ga_046CF2G3PS=GS1.1.1688516579.19.0.1688516646.60.0.0; _ga_NR74TZRFRS=GS1.1.1688516597.19.0.1688516646.0.0.0; _ga_NLSWEJR4JW=GS1.1.1688516597.19.0.1688516646.11.0.0; ASP.NET_SessionId=y50zm313pfhhhpmu224ngngz; _ga_S8NVNJR24D=GS1.1.1689172512.76.1.1689174024.0.0.0",
        "Referer": "https://regist.vlu.edu.vn/DangKyHocPhan",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    s = requests.Session()
    res = s.get(domain, headers = headers)
    output = res.content.decode('utf-8')
    print(output)