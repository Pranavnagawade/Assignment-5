'''
Q1.Write a Python class to implement pow(x, n)
Explanation:
Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
You must implement it using Class
'''

user_input1=int(input("Enter the number :"))
user_input2=int(input("Enter nth power of number :"))
class Pow:
    def power(self,x,n):
        if x==0 and n==0:
            return 0
        else:
            multi=1
            for i in range(n):
                multi=multi*x
            return multi
pow=Pow()
result=pow.power(user_input1,user_input2)
print("Power of number is :",result)