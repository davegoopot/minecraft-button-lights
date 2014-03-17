from TwitterAPI import TwitterAPI
api = TwitterAPI("rzNCKnyX2QyK4XuVD9XDQ", "kkrKJd22TprHhhlyMpcsTpfOLDwvJCI2GM50xMpg", "5794112-zirz2uIfpYC0hKH2uQFGG95rVwkWfTIj6hE21JWwYr", "TcJEikn0uTbTv2B1rXNX1uwurhLG7xdxxIBbRT0bW1PlI")
print "Got the API"
r = api.request('statuses/filter', {'track' : 'pizza'})

for item in r:
	print item
	print(item['text'] if 'text' in item else item)
