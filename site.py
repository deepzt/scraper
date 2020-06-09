        #############################################################
        #Import of Modules

import os
import re
import requests as r
from bs4 import BeautifulSoup as bs
import sys
import pyperclip
import random
import time

        ############################################################
def intro():
    print("""          _______       ==========    |-------------|     -----------|""")
    time.sleep(0.3)
    print("""        /********       ****||****    -----|  |-----      | |--------|""")
    time.sleep(0.3)
    print("""       |*                  *||*            |  |           | |""")
    time.sleep(0.3)
    print("""        \*_______          *||*            |  |           |  ----|""")
    time.sleep(0.3)
    print("""          *******\         *||*            |  |           |  ----|""")
    time.sleep(0.3)
    print("""                *|         *||*            |  |           | |""")
    time.sleep(0.3)
    print("""         _______*/      ****||****         |  |           | |---------|""")
    time.sleep(0.3)
    print("""        *********       ==========         ----           ------------|""")
    time.sleep(0.3)
    print("""                                                               -- pH03niX
                                                                   v1.0.0
                                                            ThankYou For Using""")

intro()
        ############################################################
        #Requesting the server
def usage():
    print(" [*] Usage: python3 program_name.py url_link")
if not len(sys.argv[1:]):
    print (usage())    

req = r.request('GET', str(sys.argv[1]))
##  print(dir(req))
##  print(req.text)

##        print("Couldn't establish the connection.")
sp = bs(req.text, "lxml")
new_sp = sp.prettify()
##print(new_sp)
##print(dir(new_sp))
links = sp.findAll('a')
js = sp.findAll('script')
        ##############################################################
        #Getting the title and intro

title = sp.title.text
p=[]
para = sp.findAll('p')
for p_tag in para:
    info = p_tag
    p.append(info)

        ##############################################################
        # Getting Text of evry links

all_links_text=[]
for link in links:
    l=(link.text).replace('\n' , '')
        ##    print(l)
    all_links_text.append(l)

        #############################################################
        #Getting the links

##f = open("file_for_links.txt", "w+")
##for link in links:
##  for (key, value) in (link.attrs).items():
##      if key == "href":
##          f.write(key + " : " + value +"\n")
##
##f.close()

all_links=[]
try:
    for link in links:
        temp = link.attrs["href"]
        all_links.append(temp)
except:
    print(" [*] Not an usual thing!!")

        #############################################################
all_links_info = dict(zip(all_links_text, all_links))
fp = open("all_links_info.txt", "w+")
for every_entity in list(all_links_info.items()):
    fp.write(str(every_entity))
fp.close()


        #############################################################
        #Getting contact info

p = re.compile(r"[a-zA-Z0-9./+-_]+@[a-zA-Z]+(\.[a-zA-Z]{2-4})")
try:
    mtch = p.search(req.text)
    print(mtch.group())
except:
    print(" [*] Contact not Found!!")
            
        #############################################################
        #Saving the Infos in a File

##print(os.getcwd())
file = "details"+ str(random.randint(485823,247583894))
print(" [*] Your fileName is {0}".format(str(file)))
os.mkdir(file)
os.chdir(file)

def new_file(file_name, s):
    f = open(file_name,"w+")
    f.write(str(s))
    f.close()

new_file("src_code.txt", sp)
new_file("pretty_src_code.txt", new_sp)
new_file("js.txt", js)
new_file("all_links_text.txt", all_links_text)
new_file("all_links_info.txt", all_links_info)
##new_file("links.txt", all_links)
