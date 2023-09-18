
str1 = " Python"
str2 = " Java"

    # process->01

print(str1) # Python
print(str2) # Java

    # process->02

print("language one:",str1) # language one:  Python
print("language two:",str2) # language two:  Java

    # process->03

print(str1,"and",str2)          #  Python and  Java
print(str1 + "and"+ str2)       #  Pythonand Java
print(str1 + " and " + str2)    # Python and  Java

    # process->04

print("language one is:{} adn language two is:{}".format(str1,str2))
    # By difult {0} and {1}

print("language one is:{0} adn language two is:{1}".format(str1,str2))
    # language one is: Python adn language two is: Java

print("language one is:{1} adn language two is:{0}".format(str1,str2))
    # language one is: Java adn language two is: Python

    # process->05

print(f"language one is:{str1} and language two is:{str2}") # hear f mean format
    # language one is: Python and language two is: Java

    # process->06

print("language one is: %s and language two is: %s."%(str1,str2))

num = 15.34562789
print("%.f" %num) # 15
print("%.4f" %num) # 15.3456