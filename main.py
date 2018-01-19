import os
import os.path
#from pathlib import Path

def save(nama1, Nyawa1, Atk1, Def1):	#save function
	file = open(nama1 + ".sav","w") 	#bukak file
 
	file.write(Nyawa1)		#save nyawa
	file.write("\n")		
	file.write(Atk1)			#save atk
	file.write("\n")
	file.write(Def1)			#save def
	
 
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
		file = open(nama+".sav","r")
		data_file=str(file.readlines(1))
		file.close()

		list(data_file)
		#print(data_file)

		Nyawa = int(data_file[2])
		Atk = int(data_file[9])
		Def = int(data_file[16])
		
		print("Load Successfull")

	if os.path.isfile(nama+".sav") == False:	#cek save file takde
		save(str(nama), str(Nyawa), str(Atk), str(Def))	#buat file baru
		print("New save file created")


	print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def) )

	#training place
	while True:

		CMD = input("Command: ")	#input command

		if CMD == 1:				#training attack
			Nyawa = Nyawa + 1
			label = " "

		if CMD == 2:				#training attack
			Atk = Atk + 1
			label = " "

		if CMD == 3:				#training defence
			Def = Def + 1
			label = " "

		if 	CMD == 4:
			save(str(nama), str(Nyawa), str(Atk), str(Def))
			label = "Saved!"

		if CMD == 5:
			break

		os.system('clear')			#clear scrn
		print(label)
		print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def) ) #show stats



if __name__ == "__main__":
	main()