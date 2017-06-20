from collections import Counter
import urllib, re

url = 'http://www.rocklistmusic.co.uk/terroris.htm'
html = urllib.urlopen(url).read()

raw = re.findall(r'\d{1,2}\.\s+(.*)\s-\s(.*)<br', html)
bands_counter = Counter([ b for b, a in raw])
print bands_counter

rated = sorted(raw, key=lambda x: bands_counter[x[0]] + len(x[0])*0.1 , reverse=True)

for b, a in rated:
    print b, '-', a