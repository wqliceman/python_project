import sqlite3
import requests
import win32crypt
import os
 
def get_chrome_cookies(url):
    os.system('copy "C:\\Users\\ntkodev\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies" D:\\python-chrome-cookies')
    conn = sqlite3.connect("d:\\python-chrome-cookies")
    ret_list = []
    ret_dict = {}
    for row in conn.execute("select host_key, name, path, value, encrypted_value from cookies"):
        if row[0] != url:
            continue
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_list.append((row[1], ret[1]))
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    os.system('del "D:\\python-chrome-cookies"')
    return ret_dict

cookies = get_chrome_cookies(".dianping.com")
print cookies