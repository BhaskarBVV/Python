all_types=[2.5,'a','1','hello',2,3,'3',1.2]
il=[]
sl=[]
fl=[] 
for i in all_types:
    try:
        if i>='a' or i<='a':
            sl.append(i)
    except:
        try:
            if int(i)==i:
                il.append(i) 
            else:
                fl.append(i)
                
        except:
            print("Unknown data types")

print("Integers :", il)
print("Floating :", fl)
print("String   :", sl)
