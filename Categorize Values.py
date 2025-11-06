#Mixed type list adalah list yang berisi berbagai tipe data
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"] 

#Gunakan loop untuk menampilkan jenis data dari setiap item dalam list
for item in myMixedTypeList:
    print("{} adalah tipe data {}".format(item, type(item)))