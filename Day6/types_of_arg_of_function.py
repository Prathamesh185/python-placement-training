# interview question 2
# how many types of arg we can pass in the function
# There are 4 types of arg we can pass in the function
# i) Positional arg
# ii) Key-word arg
# iii) Default arg 
# iv) Variable No. of arg / Variable length of arg

# i) Positional arg
# def add(a,b):
#     return a+b

# result = add(3,5)
# print(result)


# def personalInfo(fname, lname):
#     print("First Name:",fname)
#     print("Last Name:", lname)

# personalInfo("prashant", "jha")


# ii) Key-word arg
# def profile(fname, lname):
#     print("First Name:",fname)
#     print("Last Name:", lname)

# profile(fname="prashant",lname="jha")

'''
    Difference between positional arg and key-word arg
    positional arg = parameters must be passed in same order
    key-word arg = parameters must be passed in any order, but keys must match
'''

# iii) Default arg
# def cityName(city="Bangalore"):
#     print("City Name=",city)

# cityName("Nagpur")
# cityName("Delhi")
# cityName()


# iv) Variable number of arg
def city(*name):
    print(name)
    
city("Delhi","Nagpur","Mumbai","pune","Bangalore")