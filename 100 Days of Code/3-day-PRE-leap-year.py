# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def CheckLeap(year):  
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year")

CheckLeap(year)
