#function
def validate(password):
    speccount=0
    numcount=0
    for i in password:
        if i in spec:   
            speccount+=1
        if i in nums:
            numcount+=1
            
    if(len(password)>7 and speccount>=2 and numcount>=2):
        return "Strong"
    else:
        return "Weak"
        
#input        
password=str(input())

#constants
spec=('&','#','@','$','*','!','%')
nums=('1','2','3','4','5','6','7','8','9','0')

#result
print(validate(password))

