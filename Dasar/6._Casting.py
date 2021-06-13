# casting atau merubah tipe data suatu nilai

# tipe data darin inputan user berupa str

# data STR
print("=======STR=========")
Data_str = input("Masukkan Nilai : ")
print("Nilai :",Data_str,"\n- Type :",type(Data_str))

Data_Int = int(Data_str)
Data_Float = float(Data_str)
Data_Bool = bool(int(Data_str))
print("Nilai :",Data_Int,"\n- Type :",type(Data_Int))
print("Nilai :",Data_Float,"\n- Type :",type(Data_Float))
print("Nilai :",Data_Bool,"\n- Type :",type(Data_Bool))


# data INT
print("=======INT==========")
Data_Int = int(input("Masukkan Nilai : "))
print("Nilai :",Data_Int,"\n- Type :",type(Data_Int))

Data_str = str(Data_Int)
Data_Float = float(Data_Int)
Data_Bool = bool(Data_Int)
print("Nilai :",Data_str,"\n- Type :",type(Data_str))
print("Nilai :",Data_Float,"\n- Type :",type(Data_Float))
print("Nilai :",Data_Bool,"\n- Type :",type(Data_Bool))


# data Float
print("=======Float==========")
Data_Float = float(input("Masukkan Nilai : "))
print("Nilai :",Data_Float,"\n- Type :",type(Data_Float))

Data_str = str(Data_Float)
Data_Int = int(Data_Float)
Data_Bool = bool(Data_Float)
print("Nilai :",Data_str,"\n- Type :",type(Data_str))
print("Nilai :",Data_Int,"\n- Type :",type(Data_Int))
print("Nilai :",Data_Bool,"\n- Type :",type(Data_Bool))


# data Booleam
print("=======bool==========")
Data_bool = 1
print("Nilai :",Data_bool,"\n- Type :",type(Data_bool))

Data_str = str(Data_Bool)
Data_Int = int(Data_Bool)
Data_Float = float(Data_Bool)
print("Nilai :",Data_str,"\n- Type :",type(Data_str))
print("Nilai :",Data_Int,"\n- Type :",type(Data_Int))
print("Nilai :",Data_Float,"\n- Type :",type(Data_Float))