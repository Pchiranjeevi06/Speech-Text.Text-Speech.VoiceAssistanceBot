import re
reg_ex = re.search('launch (.*)', "launch whatsapp".lower())
if reg_ex:   
    appname = reg_ex.group(1)
    print(appname)
    print(appname=="whatsapp")
       