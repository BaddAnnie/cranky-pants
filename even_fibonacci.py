#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

numbers = [0,1]
sum = 0

while numbers[1] < 4000000:
    if numbers[1] % 2 == 0:
        sum = sum + numbers[1]
    numbers = [numbers[1],numbers[0] + numbers[1]]    

print(sum)
    
