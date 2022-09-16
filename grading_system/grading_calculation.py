print('enter marks')
marks = int(input())

if marks>=0 and marks<=33:
    print ('grade F')

elif marks>=34 and marks<=39:
    print ('grade D')

elif marks>=40 and marks<=49:
    print ('grade C')

elif marks>=50 and marks<=59:
    print ('grade B')

elif marks>=60 and marks<=69:
    print ('grade -A')

elif marks>=70 and marks<=79:
    print ('grade A')

elif marks>=80 and marks<=100:
    print ('grade A+')

else:
    print('invalid')
