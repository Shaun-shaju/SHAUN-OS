import time
import os
import sys

print(""" 
 _    _  ____  __    ___  _____  __  __  ____    ____  _____    ___  _   _    __    __  __  _  _    _____  ___ 
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)  (_  _)(  _  )  / __)( )_( )  /__\  (  )(  )( \( )  (  _  )/ __)
 )    (  )__)  )(__( (__  )(_)(  )    (  )__)     )(   )(_)(   \__ \ ) _ (  /(__)\  )(__)(  )  (    )(_)( \__ 
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)   (__) (_____)  (___/(_) (_)(__)(__)(______)(_)\_)  (_____)(___/""")                                                                                 
print("""
-> Open Terminal -- Type terminal
-> Ping Website -- Type ping
-> Trace IP Address -- Type tracert
-> Open Web Browser -- Type browser
-> Open Calculator -- Type calculator
-> Open Clock -- Type time
-> About Shaun -- Type shaun (click q to come out and then y to confirm.)
-> About Shaun OS -- Type "Shaun OS--version"

Note:-
    The any app you open will not turn off but rather the entire operation stops...
""")
action = input("What do you want to do: ")

if action == "terminal":
    print("Type cls to shutdown")
    os.system('python3 terminal.py')
elif action == "ping":
    ping = input("Which website to Ping: ")
    os.system('ping '+ ping)
    time.sleep(0.2)
    os.system('python3 home.py')
elif action == "tracert":
    tracert = input("Which ipaddress to trace: ")
    os.system('traceroute '+ tracert)
    time.sleep(2)
    os.system('python3 home.py')
elif action == "browser":
    os.system('python3 webbrowser.py')
elif action == "calculator":
    os.system('python3 calculator.py')
elif action == "shaun":
    os.system('w3m about_shaun.html')
    os.system('python3 home.py')
elif action == "shutdown" or "cls":
    timer = 0
    loading = "Initializing Shutdown Sequence: [------------------]"
    backtrack = '\b'*len(loading)

    while timer < 20:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","#",1)
        time.sleep(0.5)
        timer += 1
    time.sleep(1)
    sys.stdout.write(backtrack)
    time.sleep(0.3)
    exit()
