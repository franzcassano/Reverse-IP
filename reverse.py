import random, time, re
import requests, os, sys
from colorama import Fore, init
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup as sop
from requests.adapters import HTTPAdapter
from multiprocessing.dummy import Pool as ThreadPool

BLUE = Fore.BLUE
RED = Fore.LIGHTRED_EX
CYAN = Fore.LIGHTCYAN_EX
WHITE = Fore.LIGHTWHITE_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.LIGHTMAGENTA_EX

os.system("")
init(autoreset=True)

def rever(ips):
	try:
		session = requests.Session()
		retry = Retry(connect=3, backoff_factor=0.5)
		adapter = HTTPAdapter(max_retries=retry)
		session.mount('http://', adapter)
		session.mount('https://', adapter)
		url = 'https://www.ipaddress.com/reverse-ip-lookup'
		headers = {
			'authority': 'www.ipaddress.com', 
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
			'accept-language': 'en-US,en;q=0.9', 
			'cache-control': 'max-age=0', 
			'origin': 'https://www.ipaddress.com', 
			'referer': 'https://www.ipaddress.com/reverse-ip-lookup', 
			'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 
			'sec-fetch-dest': 'document', 
			'sec-fetch-mode': 'navigate', 
			'sec-fetch-site': 'same-origin', 
			'sec-fetch-user': '?1', 
			'upgrade-insecure-requests': '1', 
			'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.66 Mobile/15E148 Safari/604.1'
			}
		
		data = {'host': ips}
		get = session.post(url, headers=headers, data=data)
		soup = sop(get.text, 'html.parser')
		doma = soup.find('ol')
		gex = re.findall('https://www.ipaddress.com/site/(.*?)"', str(doma))
		with open('rev_res.txt', 'a', encoding="utf-8") as f:
			save = open('rev_res.txt', 'r').read()
			for x in gex:
				if x not in save:
					f.write(f'{x}\n')
			if len(gex) >= 1:
				print(f'{WHITE}IP: {CYAN}{ips} {WHITE}Reversing: {GREEN}{len(gex)} Domain')
			else:
				print(f'{WHITE}Bad IP: {RED}{ips}')
			f.close()
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		print(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	else:
		pass
		
def main():
	color = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLUE]
	ban =  ('''
  ____                                ___ ____  
 |  _ \ _____   _____ _ __ ___  ___  |_ _|  _ \ 
 | |_) / _ \ \ / / _ \ '__/ __|/ _ \  | || |_) |
 |  _ <  __/\ V /  __/ |  \__ \  __/  | ||  __/ 
 |_| \_\___| \_/ \___|_|  |___/\___| |___|_|    
                                                

Unlimited With Threading System
Contact For More Information.
Telegram: https://t.me/franzlc7
Whatsapp: https://wa.me/message/XCDZUUHYN6G5M1''')
	ran = random.choice(color)
	time.sleep(0.1)
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')
	print(ran+ban)
	try:
		ip = open(input(f'{CYAN}List Ips  :'),'r').read().splitlines()
		Thread = input(f'{CYAN}Thread : ')
		pool = ThreadPool(int(Thread))
		pool.map(rever, ip)
		pool.close()
		pool.join()
	except KeyboardInterrupt:
		sys.exit(f'{RED}\n\nShutdown Button Detected\nFinishing Program...!!!!\n')
	except (ConnectionAbortedError, ConnectionError, ConnectionResetError):
		sys.exit(f'{RED}\n\nCheck Your Connection And Try Again\nShutdown Program...!!!!\n')
	except FileNotFoundError:
		print(f'{RED}Please Input Valid File!!!')
	except ValueError:
		print(f'{RED}Please Input Valid Thread System!!!')
	else:
		pass

if __name__ == '__main__':
	main()
