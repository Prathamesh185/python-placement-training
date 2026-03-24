#rstrip

programming = input("Enter your programming Name:")
p_name = programming.strip()
if p_name == 'Python':
    print(p_name)
elif p_name == 'Java':
    print(p_name)
elif p_name == "Cpp":
    print(p_name)
else:
    print("Wrong programming name")