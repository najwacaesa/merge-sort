import os 
os.system('cls') 
 
def mergeSort(l): 
    if len(l)>1: 
 
        tengah=len(l)//2 
        kiri = l[:tengah] 
        kanan= l[tengah:] 
 
        mergeSort(kiri) 
        mergeSort(kanan) 
 
     
 
        a=b=c=0 
 
        while a<len(kiri) and b<len(kanan): 
            if kiri[a]<kanan[b]: 
                l[c]=kiri[a] 
                a+=1 
            else: 
                l[c]=kanan[b] 
                b+=1 
            c+=1 
 
        while a<len(kiri): 
            l[c]=kiri[a] 
            a+=1 
            c+=1 
 
        while b<len(kanan): 
            l[c]=kanan[b] 
            b+=1 
            c+=1 
    return l
    
 
def ubah(list1): 
    result=[] 
    for array in list1: 
        if isinstance(array,list): 
            for i in array: 
                if isinstance(i,list): 
                    for a in i : 
                        result.append(int(a)) 
                elif isinstance(i, int): 
                    result.append(i) 
        else: 
            result.append(array) 
    return result 
     

arr =[12, 1, [22, 3, [8, 14]], 2, 6, [11], 90] 
print("Sebelum sorting=",arr) 
    
pr = ubah(arr) 
print("proses =", pr) 
hal = mergeSort(pr) 
print("Setelah sorting =", hal)