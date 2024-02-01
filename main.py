from student import Student
objStudent=Student()

def Menu():
        print('Choose menu : \n\t1. Add Student\n\t2. Remove Student\n\t3. Update Student\n\t4. See all Students\n\t5. Batch-wise Topper List\n\t6. Exit\n\t7. Search Student')
        try:
            print()
            menu=int(input('Enter menu  : '))
            if menu==1:
                name=input('Enter your name : ')
                course=input('Enter your course name : ')
                assessment=int(input('How many assessments (Tests) did you solved out of 5 ? : '))
                assignment=int(input('How many assignment (Practice Sets) did you solved out of 10 ? : '))
                
                # compare assessments
                if assessment>=0 and assessment<=5:
                    new_assessment=assessment
                else:
                    print('We have only 5 assessments...')
                
                # compare assignments
                if assignment>=0 and assignment<=10:
                    new_assignment=assignment
                else:
                    print('We have only 10 assignment...')
                
                # insert data into table 
                objStudent.AddStudent(name,course,new_assessment,new_assignment)  
                 
            elif menu==2:
                Id=int(input('Enter Id of Record you want to Delete : '))
                objStudent.RemoveStudent(Id)
                
            elif menu==3:
                Id=int(input('Enter Id of Record you want to Update : '))
                objStudent.UpdateStudent(Id)
                
            elif menu==4:
                objStudent.ShowAllStudent()
                
            elif menu==5:
                objStudent.Batch_Wise_Topper()
                
            elif menu==6:
                print('Program ending...')
                
            elif menu==7:
                name=input('Enter name : ')
                objStudent.Search_Student(name)
                
            else:
                print('Menu does not exist.')
                
        except Exception:
            print('Please enter valid menu...')
      
      
      
      
# calling menus       
Menu()



