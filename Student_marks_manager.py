
student = {}

print("---STUDENT MARKS MANAGER PROGRAM--- \n Type 'y' to start...")
while True:
     number = "y"
     check = input()
     if number == check:
        print("\n Starting programm...")
        break
            
     else:
         print("Invalid Output")
         

    
while True:
    print('\n-----Student manager app------')
    print('1. Add Student')
    print('2. View student list')
    print('3. View marks')
    print('4. Print Data on File')
    print('5. Format File Data')
    print('6. Exit')
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        print("\n -----Student Enroll Panel-----")
        name = input("Enter student name:")
        marks = int(input("Enter student marks:"))
        student[name] = marks
        print(f'{name} successfully added!')
        
    elif choice == "2":
        if not student:
            print("No Student found!")
        else:   
            print("\n ------Marks Viewer------")
            for name, marks in student.items():
                result = "Passed" if marks >= 40 else "Failed"
                print(name,":",marks,"---",result)
                 
                 
    elif choice == "3":  
        name = input("Enter Student's name:")
        if name in student:
               marks = student[name]
               print(f"{name}'s marks is:" ,marks)
               if marks < 40:
                   print("Failed")
                   
               else:
                    print("Passed")
        else:
             print("Student not found!")
             
    elif choice == "4":
         if not student:
                  print("No student found in db!")
         else:
             with open("/storage/emulated/0/My_Python /Project/student.txt","w") as file:  # replace as file path here:   open("_here_","w")
                 if not file:
                    print('File Error')
               
                 else:  
                    file.write("------Student's Data-----")
                    for name,marks in student.items():
                        writer = file.write
                        writer.writerow([name,marks])
                        file.close()  
                        print("\n ...All Data printed Successfully!" )
         
    elif choice == "5":
        file = open("/storage/emulated/0/My_Python /Project/student.txt","w")   # replace as file path here:   open("_here_","w")
        pass    
        print("All Data formatted successfully!")
              
    elif choice == "6":
        print("Exiting...")
        exit
        
    else:
         print("choice not found!")
         
 