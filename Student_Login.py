
#Give the some user login i'd
l1=101
l2=102
l3=103
l4=105

#take the input from user for varification
name = input ("Enter the Name: ")
Login_id = int(input ("Enter Login i'd "))
'''
Login_id = l1
Login_id = l2
Login_id = l3
Login_id = l4 
'''
#conditions

if ((Login_id == l1) or (Login_id == l2) or (Login_id == l3)or (Login_id == l4)) :
    print("_______________________________________________")
    print("")
    print("=>> Your name is ",name,"& Your login i'd is ",Login_id)
    print("_______________________________________________")
    print("    Press 1 for confirm or press 2 for exit")
    num1 = input()
#now perform your desired operation
    if num1 == "1":
        print("_______________________________________________")
        print ("    Note: Maximum marks = 100")
        print("_______________________________________________")
        print("    Enter the marks of subject1: ")
        s1 = int(input())
        print("    Enter the marks of subject2: ")
        s2 = int(input())
        print("    Enter the marks of subject3: ")
        s3 = int(input())
        print("    Enter the marks of subject4: ")
        s4 = int(input())
        print("    Enter the marks of subject5: ")
        s5 = int(input())
        print("    Press 2 for continue: ")
        var = input()
        total = s1 + s2 + s3 + s4 + s5
        per = total/5
        print("_______________________________________________")
        print("")
        print("    Hello",name)
        print("    Total  marks is: ",total)
        print("    Obtained Percentage: ",per,"%")
        print("_______________________________________________")
    else:
        print("    You chose to exit. Thank you!")
else:
    print("      Your Login i'd is incorrect.")

