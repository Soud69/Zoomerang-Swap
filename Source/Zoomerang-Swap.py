try:
	import requests
	import json
	import os
	from os import system
	system("title " + "Soud Was Here - @_agf - Soud#0737 - Zoomerang Checker V1")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                              """, Fore.GREEN + "Credit @_agf - Soud#0737")
print(Fore.GREEN + "Zoomerang Checker + Swap By Soud,", Fore.RED+"Free And Not For Sell\n")

email = str(input("Enter Your Email: "))
password = str(input("Enter Your Password: "))
doo = 0
def login():
	url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAZyyldZdaECkbp9vEr0IkFFfghSgtv20U"
	headers = {
		"Host": "www.googleapis.com",
		"Content-Type": "application/json",
		"Accept": "*/*",
		"X-Ios-Bundle-Identifier": "com.yantech.zoomerang",
		"Connection": "keep-alive",
		"X-Client-Version": "iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS",
		"User-Agent": "FirebaseAuth.iOS/6.9.2 com.yantech.zoomerang/3.0.14 iPhone/14.2.1 hw/iPhone13_3",
		"Accept-Language": "en",
		"Accept-Encoding": "gzip, deflate, br"
		}
	data = {
		"email": email,
		"password": password,
		"returnSecureToken": "true"
		}
	req = requests.post(url, json=data, headers=headers)
	
	if "INVALID_EMAIL" in req.text:
		print(Fore.RED+"[-] Wrong Email")
		closee()
	elif "EMAIL_NOT_FOUND" in req.text:
		print(Fore.RED+"[-] Email Not Found")
		closee()
	elif "INVALID_PASSWORD" in req.text:
		print(Fore.RED+"[-] Wrong Password")
		closee()
	elif "idToken" in req.text:
		print(Fore.GREEN+"[+] Logged In Success")
		tt = json.loads(req.text)
		token = tt["idToken"]
		swap(token)

def closee():
	input()
	exit()

def swap(token):
	global doo
	input("Are You Ready For Swap Check?")
	ggg = open("User.txt", "r")
	while 1:
		user = ggg.readline().split("\n")[0]
		if user == "":
			closee()
		url = "https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/username"
		headers = {
		"Host": "us-central1-zoomerang-dcf49.cloudfunctions.net",
		"Content-Type": "application/json",
		"Connection": "keep-alive",
		"Accept": "application/json",
		"User-Agent": "Zoomerang/3.0.14 (com.yantech.zoomerang; build:1; iOS 14.2.1) Alamofire/5.2.2",
		"Authorization": f"Bearer {token}",
		"Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8"
		}
		
		data = {
		"username": user
		}
		ree = requests.put(url, json=data, headers=headers)
		if "Username is not available" in ree.text:
			doo += 1
			print(Fore.RED+f"Taken @{user} - Checked: {doo}")
		elif 'status":true,' in ree.text:
			doo += 1
			print(Fore.GREEN+f"Swapped @{user} - Checked: {doo}")
			closee()
login()
