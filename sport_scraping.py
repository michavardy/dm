import requests
import json
from pprint import pprint
import io


url = "https://cdnapi.bamboo-video.com/api/football/round?format=json&iid=573881b7181f46ae4c8b4567&filter={^%^22seasonName^%^22:^%^2222/23^%^22}&useCache=false&ts=27970131"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Origin': 'https://www.football.co.il',
  'Connection': 'keep-alive',
  'Referer': 'https://www.football.co.il/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'TE': 'trailers',
  'Cookie': 'AWSALB=8ZbMfF0vuveGqevVepnF8De1UYFwgby8I7MPloF/vDcj8HDjGAOOuYuHfESEa251htZr14EKxWH9jQMBFJVtYMRtpo5wzY6xLAY1roz4F1VEL1GMvLSzh/X+Se/s; AWSALBCORS=8ZbMfF0vuveGqevVepnF8De1UYFwgby8I7MPloF/vDcj8HDjGAOOuYuHfESEa251htZr14EKxWH9jQMBFJVtYMRtpo5wzY6xLAY1roz4F1VEL1GMvLSzh/X+Se/s; version=v2.16hf38'
}


response = requests.request("GET", url, headers=headers, data=payload)

result_dict = json.dumps(response.json(), ensure_ascii=False)

with io.open("test.txt", 'w', encoding='utf-8') as file:
    file.write(str(result_dict))



