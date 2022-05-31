def swapFileData(Name):
    print("swaping file" + Name + "with data_b")
    data_a = open("sample1.txt" , "w+")
    data_b = open("sample2.txt" , "w+")

    data_a.write(data_b)
    data_b.write(data_a)

swapFileData()

    
