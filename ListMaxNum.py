def find_max_element(list):
    if len(list) == 0:
        return 0
    else:
        MaxInList= max(list)
        return MaxInList

li= [] 
maxnum= find_max_element(li)
print("Largest in ",li,"is", maxnum)
