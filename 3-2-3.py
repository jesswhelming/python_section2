import requests, json

s = requests.Session()
r = s.get('http://httpbin.org/stream/20', stream=True)

print(r.text)
print(r.encoding)
print(type(r))

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = json.loads(line)
    for e in b.keys():
        print("key :", e)
        print("value :", b[e])
