
small pease of code for the Phonebook challange on HTB.

https://app.hackthebox.eu/challenges/phonebook#

```
the site will take the star sign '*' as a wildcard. 
this means that when we will put '*' under the username and password 
the site will refere us to a valid user profile, 
actually it refere us to the first user in the DB list. 
the challange is to seek the password of reeve, and its also the flag that we need. 
I have written a small script that trys to guess the next character in each position of the password. 
the script will try A-Z a-z 0-9 and valid symbols.
```

## usage
``` bash
pip install requests
python3 phonebookctf.py http://site.to/hack 

```
