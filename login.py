import time
import os

print("twostep_authcommand.bui")
print("  ")
time.sleep(0.2)
username = input("Username: ")
passcode = input("Password: ")

if username =="shaun" or "Shaun":
    if passcode == "0611":
        print("""
  _______                                 _______                  __            __ 
 |   _   .----.----.-----.-----.-----.   |   _   .----.---.-.-----|  |_.-----.--|  |
 |.  1   |  __|  __|  -__|__ --|__ --|   |.  |___|   _|  _  |     |   _|  -__|  _  |
 |.  _   |____|____|_____|_____|_____|   |.  |   |__| |___._|__|__|____|_____|_____|
 |:  |   |                               |:  1   |                                  
 |::.|:. |                               |::.. . |                                  
 `--- ---'                               `-------'                                  
                                                                                    """)
        time.sleep(0.5)
        os.system('python3 home.py')
    else:
        print(""" 
  _________                          .__  __           __________                              .__     
 /   _____/ ____   ____  __ _________|__|/  |_ ___.__. \______   \_______   ____ _____    ____ |  |__  
 \_____  \_/ __ \_/ ___\|  |  \_  __ \  \   __<   |  |  |    |  _/\_  __ \_/ __ \\__  \ _/ ___\|  |  \ 
 /        \  ___/\  \___|  |  /|  | \/  ||  |  \___  |  |    |   \ |  | \/\  ___/ / __ \\  \___|   Y  |
/_______  /\___  >\___  >____/ |__|  |__||__|  / ____|  |______  / |__|    \___  >____  /\___  >___|  /
        \/     \/     \/                       \/              \/              \/     \/     \/     \/ """)                                                                                                               
