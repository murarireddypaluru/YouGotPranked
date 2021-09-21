
def switchData():
    file1 = "/Applications/blabber replacment/Pro - 98/sample1.txt"
    file2 = "/Applications/blabber replacment/Pro - 98/sample2.txt"
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read() 
    
    #if input == 1:
        with open(file1, 'w') as a:
            a.write(data_b)
    #if input == 2:
        with open(file2, 'w') as b:
            b.write(data_a)
switchData()