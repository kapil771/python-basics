Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nupdating the original set ... ")  
Months.update(["July","August","September","October"]);  
print("\nprinting the modified set ... ")   
print(Months)

Days1 = {"Monday","Tuesday","Wednesday","Thursday"}  
Days2 = {"Friday","Saturday","Sunday"}  
print(Days1|Days2)