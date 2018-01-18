import os
import os.path
#from pathlib import Path

def save(nama1, Nyawa1, Atk1, Def1):	#save function
	file = open(nama1 + ".sav","w") 	#bukak file
 
	file.write(Nyawa1 + "\n")		#save nyawa
	file.write(Atk1 + "\n")			#save atk
	file.write(Def1 + "\n")			#save def
	
 
	file.close()

def main():
	
	#initial value
	Nyawa = 0	#initial setting nyawa
	Atk = 0		#initial setting attack
	Def = 0		#initial setting defence


	#key in nama dan cek save file
	nama = raw_input("nama: ")

	if os.path.isfile(nama+".sav") == True:		#cek save file
		#load item here !!!!!
		print("Load Successfull")

	if os.path.isfile(nama+".sav") == False:	#cek save file takde
		save(str(nama), str(Nyawa), str(Atk), str(Def))	#buat file baru
		print("New save file created")


	#training place
	while True:

		CMD = input("Command: ")	#input command

		if CMD == 1:				#training attack
			Nyawa = Nyawa + 1

		if CMD == 2:				#training attack
			Atk = Atk + 1

		if CMD == 3:				#training defence
			Def = Def + 1

		if 	CMD == 4:
			save(str(nama), str(Nyawa), str(Atk), str(Def))

		os.system('clear')			#clear scrn
		print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def) ) #show stats



if __name__ == "__main__":
	main()