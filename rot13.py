dict_array = {
    "a":1,"b":2,"c":3,"d":4,"e":5,
    "f":6,"g":7,"h":8,"i":9,"j":10,
    "k":11,"l":12,"m":13,"n":14,"o":15,
    "p":16,"q":17,"r":18,"s":19,"t":20,
    "u":21,"v":22,"w":23,"x":24,"y":25,"z":26
    }

reverse_dict_array = {
    1:"a",2:"b",3:"c",4:"d",5:"f",
    6:"f",7:"g",8:"h",9:"i",10:"j",
    11:"k",12:"l",13:"m",14:"n",15:"o",
    16:"p",17:"q",18:"r",19:"s",20:"t",
    21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"
}

targets = ["c","v","p","b","p","g","s","{","g","u","v","f","_","v","f","_","p","e","l","c","g","b","!","}"]

for i in range(len(targets)):
    if targets[i] in dict_array:
        if dict_array[targets[i]]+13 > 26:
            print(reverse_dict_array[dict_array[targets[i]]+13-26])
        else:
            print(reverse_dict_array[dict_array[targets[i]]+13])
    else:
        print(targets[i])