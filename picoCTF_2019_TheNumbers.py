
normal_array = [16,9,3,15,3,20,6,"{",20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,"}"]

dict_array = {1:"a",2:"b",3:"c",4:"d",5:"e",
              6:"f",7:"g",8:"h",9:"i",10:"j",
              11:"k",12:"l",13:"m",14:"n",15:"o",
              16:"p",17:"q",18:"r",19:"s",20:"t",
              21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

for i in range(len(normal_array)):

    if normal_array[i] in dict_array:
        print(dict_array[normal_array[i]])
    elif normal_array[i] == "{":
        print ("{")
    else:
        print ("}")