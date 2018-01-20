import os
import os.path
# from pathlib import Path

def save(nama1, Nyawa1, Atk1, Def1):	# save function
	file = open(nama1 + ".sav", "w") 	# bukak file

	Nyawa1 = '%03d' % int(Nyawa1)	# bagi dia jadi 3 digit
	Atk1 = '%03d' % int(Atk1)
	Def1 = '%03d' % int(Def1)

	file.write(Nyawa1)		# save nyawa
	# file.write("\n")
	file.write(Atk1)			# save atk
	# file.write("\n")
	file.write(Def1)			# save def
	
	file.close()

def lawan(Nyawa2nd, Def2nd, Atk1ft):	# algorithm bila berlawan

	Damage = Atk1ft - Def2nd
	Nyawa2nd = Nyawa2nd - Damage

	return Nyawa2nd


def tmpt_lawan():									# medan perlawanan
	
	Nyawa_bin1=0
	Nyawa_bin1=0
	binatang1 = raw_input("Binatang 1: ")			#pilih binatang
	binatang2 = raw_input("Binatang 2: ")			#pilih binatang 2

	if os.path.isfile(binatang1+".sav") is True:		# cek save file
		# load item here !!!!!
		file = open(binatang1+".sav", "r")
		data_file=str(file.readlines(1))
		file.close()

		list(data_file)				# break kan string jd character
		print(data_file)

		# pilih character dan tambah string string nombor
		Nyawa_bin1 = str(data_file[2])+str(data_file[3])+str(data_file[4])
		Atk_bin1 = str(data_file[5])+str(data_file[6])+str(data_file[7])
		Def_bin1 = str(data_file[8])+str(data_file[9])+str(data_file[10])

		#print(Nyawa_bin1)
		#print(Atk_bin1)
		#print(Def_bin1)

	if os.path.isfile(binatang2+".sav") is True:		# cek save file
		# load item here !!!!!
		file = open(binatang2+".sav", "r")
		data_file=str(file.readlines(1))
		file.close()

		list(data_file)				# break kan string jd character
		print(data_file)

		# pilih character dan tambah string string nombor
		Nyawa_bin2 = str(data_file[2])+str(data_file[3])+str(data_file[4])
		Atk_bin2 = str(data_file[5])+str(data_file[6])+str(data_file[7])
		Def_bin2 = str(data_file[8])+str(data_file[9])+str(data_file[10])

	if os.path.isfile(binatang1+".sav") is False:	# cek save file takde
		print("Name 1 don't exist")
		finish = True
		os.system("exit")
		#main()

	if os.path.isfile(binatang2+".sav") is False:	# cek save file takde
		print("Name 2 don't exist")
		finish = True
		os.system("exit")
		#main()

	finish = False

	while finish is False :

		if Nyawa_bin1 <= 0 :
			finish = True
			print("==============")
			print("Binatang 2 WIN")
			print("==============")
			break

		if Nyawa_bin2 <= 0 :
			finish = True
			print("==============")
			print("Binatang 1 WIN")
			print("==============")
			break

		test=raw_input("pause")

		#print("binatang 1 stat: ")
		#print(str(Nyawa_bin1), str(Atk_bin1), str(Def_bin1))
		#print("binatang 2 stat: ")
		#print(str(Nyawa_bin2), str(Atk_bin2), str(Def_bin2))


		print("Binatang 1 serang Binatang 2 !!")
		satuVSdua = lawan(int(Nyawa_bin2), int(Def_bin2), int(Atk_bin1))
		Nyawa_bin2 = satuVSdua
		print("Nyawa binatang 2: " + str(satuVSdua))


		#print("binatang 1 stat: ")
		#print(str(Nyawa_bin1), str(Atk_bin1), str(Def_bin1))
		#print("binatang 2 stat: ")
		#print(str(Nyawa_bin2), str(Atk_bin2), str(Def_bin2))


		print("Binatang 2 serang Binatang 1 !!")
		duaVSsatu = lawan(int(Nyawa_bin1), int(Def_bin1), int(Atk_bin2))
		Nyawa_bin1 = duaVSsatu
		print("Nyawa binatang 1: " + str(duaVSsatu))


		#print("binatang 1 stat: ")
		#print(str(Nyawa_bin1), str(Atk_bin1), str(Def_bin1))
		#print("binatang 2 stat: ")
		#print(str(Nyawa_bin2), str(Atk_bin2), str(Def_bin2))





	test=raw_input("pause")




def main():
	
	# initial value
	Nyawa = 0	# initial setting nyawa
	Atk = 0		# initial setting attack
	Def = 0		# initial setting defence
	label = " "


	# key in nama dan cek save file
	nama = raw_input("nama: ")

	if os.path.isfile(nama+".sav") is True:		# cek save file
		# load item here !!!!!
		file = open(nama+".sav", "r")
		data_file=str(file.readlines(1))
		file.close()

		list(data_file)				# break kan string jd character
		print(data_file)

		# pilih character dan tambah string string nombor
		Nyawa = str(data_file[2])+str(data_file[3])+str(data_file[4])
		Atk = str(data_file[5])+str(data_file[6])+str(data_file[7])
		Def = str(data_file[8])+str(data_file[9])+str(data_file[10])
		
		print("Load Successfull")

	if os.path.isfile(nama+".sav") is False:	# cek save file takde
		save(str(nama), str(Nyawa), str(Atk), str(Def))	# buat file baru
		print("New save file created")


	print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def))

	# training place
	while True:

		CMD = input("Command: ")	# input command

		if CMD == 1:				# training attack
			Nyawa = int(Nyawa) + 1
			label = " "

		if CMD == 2:				# training attack
			Atk = int(Atk) + 1
			label = " "

		if CMD == 3:				# training defence
			Def = int(Def) + 1
			label = " "

		if 	CMD == 4:
			save(str(nama), str(Nyawa), str(Atk), str(Def))
			label = "Saved!"

		if CMD == 5:				# tutup
			break

		if CMD == 6:				# tutup
			tmpt_lawan()

		os.system('clear')			# clear scrn
		print(label)

		# show stats
		print("Nyawa " + str(Nyawa) + " Atk " + str(Atk) + " Def " + str(Def)) 



if __name__ == "__main__":
	main()
	#lawan()
	#tmpt_lawan()