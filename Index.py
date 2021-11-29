# Created by MD. Ferdous Ibne Abu Bakar

"SOLOLEARN ID HACKER - first time in Sololearn"
'⚠️PLEASE VIEW THE FULL OUTPUT⚠️'
"You can run with your own and other's profile link"
#Sample input: https://www.sololearn.com/Profile/1/?ref=app
#My profile link: https://www.sololearn.com/Profile/20905876/?ref=app

"⚠️Don't understand what to do? enter - help  or just submit withut any input⚠️"

try:
#all imports:
  import os 
  import pytz 
  from urllib.request import urlopen
  import urllib.request as request
  
#get user input:
  i=input()

#array:
  hlp = ['''<style>h4{color: green;}</style><h3><font color="green">[Help]</h3><h4>How to use?</font></h4><p>it\'s very easy. If you are using browser, then: <ol><li>Login your profile</li>
<li>Copy the profile link 

example link: https://sololearn<span>.com/profile/1/?ref=app</span>
*you can copy & RUN▶ the above link</li> 
    <li>Paste the link here and Run▶</li></ol>*You can only input your or other\'s Sololearn Profile link.</p>
    <h4>How do I get URL from app?</h4><p>If you use "sololearn app", then follow the following steps<ol>
    <li>Go to profile</li> 
    <li>You will find a triple dot (:) on top right corner. Tap on it. </li> 
    <li>Then tap on "Share" option and copy the link. </li></ol>
    <h4>Is this safe to use?</h4><p>Yes! It is 100% safe to use!</p>
    <h4>What can do this programme?</h4><p>This programme can do many things. If you enter a valid profile link, then it can print:</p><ol><li>User name</li>
    <li>User ID</li>
    <li>Followers</li>
    <li>Following</li>
    <li>Level</li>
    <li>Bio</li>
    <li>User avatar/profile pic (With link)</li>''',''' <sub style="background-color:gold;padding-top:1px;padding-bottom:1px; padding-left:5px;padding-right:5px; text-align: center;border-radius:10px; color:#171717ff; font-size: 10px">''','20905876','''<h5 style="color:gray;">Avatar link: <span>https://</span>''','''<h4 style="color: Red;font-size:14px;">Hacker: MD. Ferdous Ibne Abu Bakar<sub style="background-color:gold;padding-top:1px;padding-bottom:1px; padding-left:5px;padding-right:5px; text-align: center;border-radius:10px; color:#171717ff; font-size: 10px">''']
#help:  
  if i=='help' or i=='Help' or i=="":
   print('<body style="background-color:limegreen">'+hlp[0])

   
#main content:
  elif i.startswith("https://www.sololearn.com") or i.startswith("https://sololearn.com"):

#decode user input...[1]:
   code=urlopen(i)
   x = code.read().decode('utf-8')
   
#user name:    
   s = int(x.find("</title>"))-12

#avater link:
   start = int(x.find("blob.sololearn.com/avatars"))
   end = int(x.find(".jpg"))+4
  
   y = x[start:end]

   a = 'https://'+str(y)
   b = str(a)
   url = b.strip('\'"')

#user info from [1]:
   infs = int(x.find("<script>window."))
   infe = int(x.find("</head>"))

   usr_info = x[infs:infe]

#total xp:
   xps = int(usr_info.find("xp"))+4
   xpe = int(usr_info.find("countryCode"))-2
   xp = usr_info[xps:xpe]

#user ID: 
   ids = int(usr_info.find('"id"'))+5
   ide = int( usr_info.find(',"name"'))
   id =  usr_info[ids:ide]
   
#pro, mod & others:
   pros = int(usr_info.find('"isPro"'))+8
   proe = int( usr_info.find(',"followers"'))
   mods = int(usr_info.find('_mod"'))+1
   mode = int( usr_info.find(',"priority"'))-1
   
   pro =  usr_info[pros:proe]
   mod =  usr_info[mods:mode]

#pro, mod, creator:
   if pro == "true":
    pro = hlp[1]+'PRO</sub>'
   if mod == 'mod':
     pro = hlp[1]+'MOD</sub>'
   if pro == "false":
     pro = "" 
   if pro == "false" and mod == "mod":
     pro = hlp[1]+'MOD</sub>'
   if id == '1':
     pro = hlp[1]+'CREATOR</sub>'
 
#level:    
   lvls = int(usr_info.find('"level"'))+8
   lvle = int( usr_info.find(',"xp"'))
   lvl =  usr_info[lvls:lvle]
   
   if int(lvl) < 10:
    lvl = '0'+str(lvl)

#followers:   
   flws = int(usr_info.find('"followers"'))+12
   flwe = int( usr_info.find(',"following"'))
   flw =  usr_info[flws:flwe]
   
   if int(flw) < 10:
    flw = '0'+str(flw)
   if int(flw) == 0:
    flw = '0'

#following:    
   flwis = int(usr_info.find('"following"'))+12
   flwie = int( usr_info.find(',"isFollowing"'))
   flwi =  usr_info[flwis:flwie] 
   
   if int(flwi) < 10:
    flwi = '0'+str(flwi)
   if int(flwi) == 0:
    flwi = '0'

#country (iso):    
   cnts = int(usr_info.find('"countryCode"'))+15
   cnte = int( usr_info.find(',"isPro"'))-1
   cnt =  usr_info[cnts:cnte]
   cn = cnt.strip('\'"')
#country name:
   cntr = pytz.country_names[cn]

#user bio:   
   bios = int(usr_info.find('"bio"'))+7
   bioe = int( usr_info.find(',"connectedAccounts"'))-1
   bio =  usr_info[bios:bioe]
   nl = bio.find('\\n')

   nl_1 = bio[nl:(nl+2)]
   
   if nl_1 == "\\n":
    bio=bio.replace(nl_1,'''
     ''')

#my id:
   if '"bio":null' in usr_info:
    bio = ''
    
   if id == hlp[2]:
     pro = hlp[1]+'HACKER</sub>'
     y = '&lt;HostError: unable to find link ☹&gt;'
     flw = flw+'<sub style="color:yellow"> (Follow me 🥰)</sub>'
     hlp[4] = 'Instagram: https://www.instagram.com/Ferdous9709'
     url = 'https://c.tenor.com/DXL84KB6lscAAAAj/confetti-cute.gif'
     
#OUTPUT:

#marquee:    
   print('<marquee><b>Welcome to <font color="yellow">SOLOLEARN ID HACKER</font>. Input any Sololearn id link & see the magic! DON\'T BE AFRAID, This is not a real hacker programme.  It only takes user information from web source and it is 100% safe!  - <font color="orange">Made by MD. Ferdous Ibne Abu Bakar</font>'+hlp[1]+'HACKER</sub></b></marquee>')
   
#user details:
   print('''<body style="background-color:#1a4fa27e;"><span style="color: green; font-size: 25px; font-weight: bold;">Successfully Hacked ↓↓↓</span><h4>User Name: '''+str(x[132:s])+''''''+str(pro)+'''

User ID: '''+str(id)+'''

Total XP: '''+str(xp)+'''

Level: '''+str(lvl)+'''

Followers: '''+str(flw)+'''

Follwing: '''+str(flwi)+'''

Bio: '''+str(bio)+'''

Country: '''+str(cntr))
   
   print(hlp[3]+str(y)+'''</h5>''')
   print (hlp[4]+'HACKER</sub></h4>')
   request.urlretrieve(url, 'image.png')
   
#invalid input or error:  
  elif not 'sololearn.com/' in i:
   print('<h2 style="color:red;>'+str(url)+' - is an invalid link! You can only input your or other\'s valid Sololearn Profile link</h2>')


except AttributeError:
 print('<h2 style="color:red; align="center";>'+str(url)+'  -  is an invalid link!</h2>')
 
except ValueError:
  print('<h2 style="color:red; align="center";>'+str(i)+' - is an invalid link! Or this ID is Banned!</h2>')

except NameError:
 print('''<h2><font color="red">Faild to hack :(</font></h2><h3>Need help? input "help" or SUBMIT without any input and RUN▶</h2>*You can only input your or other\'s valid Sololearn Profile link.
 ''')
 
#no avater:
except __import__('urllib').error.URLError:
    print('<p style="color:grey">No Avatar!</p>')
        
os.system("touch file.png")
