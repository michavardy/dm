import json
city = 'חיפה'
#print(json.dumps(city))
#print(json.dumps(city, ensure_ascii=False))

print(city.encode('utf-8').decode('raw_unicode_escape'))

