import os
import os.path
#from pathlib import Path

def save(nama1, Nyawa1, Atk1, Def1):	#save function
	file = open(nama1 + ".sav","w") 	#bukak file
 	
	Nyawa1 = '%03d' % int(Nyawa1)	#bagi dia jadi 3 digit
	Atk1 = '%03d' % int(Atk1)
	Def1 = '%03d' % int(Def1)

	file.write(Nyawa1)		#save nyawa
	#file.write("\n")		
	file.write(Atk1)			#save atk
	#file.write("\n")
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

		list(data_file)				#break kan string jd character
		print(data_file)

		Nyawa = str(data_file[2])+str(data_file[3])+str(data_file[4])	#pilih character ke empat
		Atk = str(data_file[5])+str(data_file[6])+str(data_file[7])
		Def = str(data_file[8])+str(data_file[9])+str(data_file[10])
		
		print("Load Successfull")

	if os.path.isfile(nama+".sav") == False:	#cek save file takde
		save(str(nama), str(Nyawa), str(Atk), str(Def))	#buat file baru
		print("New save file created")


	print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def) )

	#training place
	while True:

		CMD = input("Command: ")	#input command

		if CMD == 1:				#training attack
			Nyawa = int(Nyawa) + 1
			label = " "

		if CMD == 2:				#training attack
			Atk = int(Atk) + 1
			label = " "

		if CMD == 3:				#training defence
			Def = int(Def) + 1
			label = " "

		if 	CMD == 4:
			save(str(nama), str(Nyawa), str(Atk), str(Def))
			label = "Saved!"

		if CMD == 5:				#tutup
			break

		os.system('clear')			#clear scrn
		print(label)
		print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def) ) #show stats



if __name__ == "__main__":
	main()