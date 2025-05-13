#45*5=555 , 56+9=77 , 56/4=6
print("enter first number")
int1=int(input())
print("enter second number")
int2=int(input())
print("enter operator")
i=input()
if i=='+' and int1 !=56 and int1 !=9 and int2 != 56 and int2 != 9:
    print(int1+int2)
elif i=='-':
    print(int1-int2)
elif i=='*' and int1 != 45 and int1 != 5 and int2 != 45 and int2 != 5:
    print(int1*int2)
elif i=='/' and int1 !=56 and int2 != 4:
    print(int1 / int2)
elif i=='+' and (int1 ==56 or int1== 9) and (int2 == 56 or int2== 9):
    print(77)
elif i=='*' and (int1 == 45 or int1 == 5) and (int2 == 45 or int2 == 5):
    print(555)
elif i=='/' and int1 ==56 and int2 == 4:
    print(6)
print("Thank you")
