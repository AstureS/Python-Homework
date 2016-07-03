import sys , math #Добавление используемых модулей

try: 
	infilename = sys.argv [1] #Читаем со второй позиции имя файла со входными данными 
	outfilename = sys.argv [2] #Читаем с третьей позиции имя файла куда будем записывать результирующие данные
except:
	print("Usage:", sys.argv[0], "infile  outfile") #Если отсутствует какой либо файл, то выводим ошибку 
	sys.exit (1) #и завершаем выполнение программы 

ifile = open(infilename , "r") #Открываем файл с входными данными  на чтение 
ofile = open(outfilename , "w") #Открываем файл для результатов на запись 

def  myfunc(y): #Метод который считает значение функции в точке 
	if y  >= 0.0: #Если у не меньше 0
		return y**5* math.exp(-y) #то возвращаем у в 5 степени умноженное на е в степени -у		
	else:
		return  0.0 #иначе 0

for  line in ifile: #Для каждой строки из файла с входящими данными 
	pair = line.split () #Разбиваем строку по пробелу 
	x = float(pair [0]) #Присваиваем переменной х значение первого столбца файла 
	y = float(pair [1]) #-//- у значение второго столбца 
	fy = myfunc(y) #считаем значение функции в точке у
	ofile.write("%g %12.5g\n" % (x,fy)) #записываем в файл форматированный вывод
ifile.close() # закрытие доступа к файлам
ofile.close() # закрытие доступа к файлам

