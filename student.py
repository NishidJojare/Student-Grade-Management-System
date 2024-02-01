# creating student class
class Student:
    def __init__(self):
        self.table={'Python-Django':{},'Data Science':{},'Data Analytics':{}}
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 
            
            # getting records with course
            mycursor.execute("SELECT * FROM tblStudent")
            data=mycursor.fetchall()
            
            for rows in data:
                score=rows[3]*10+rows[4]*10
                self.table[rows[2]][rows[1]]=score
            
             
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
            
            
        except Exception:
            print(f"Something went wrong")
        
        
        python_students=len(self.table['Python-Django'])
        da_students=len(self.table['Data Analytics'])
        ds_students=len(self.table['Data Science'])
        
        
        def topper(key):
            
            sorted_dict = self.table[key]
            names = []
            max_score = max(sorted_dict.values())
            
            for k,v in sorted_dict.items():
                if sorted_dict[k] == max_score:
                    names.append(k)
                    
            return names,max_score 
            
        python_toppers,python_scores=topper('Python-Django')
        da_toppers,da_scores=topper('Data Analytics')
        ds_toppers,ds_scores=topper('Data Science')
        
        
        print(f'''
        ____________________________________________________________________________________
        |                                                                                  |
        |            **********   Student Grade Management System   ***********            |
        |                                                                                  |
        |                                                                                  |
        |------------------------  Total no of students : {python_students+da_students+ds_students} ------------------------------|  
        |__________________________________________________________________________________|
        |                                                                                  |
        |          Total courses : {len(self.table.keys())} (Python-Django/Data Science/Data Analytics)           | 
        |__________________________________________________________________________________|
        |                                                                                  |
        |     	       ______________________________________________________              | 
        |     	       |    Students enrolled in Python-Django : {python_students}          |              |
        |     	       |                                                    |              | 
        |     	       |    Students enrolled in Data Analytics : {da_students}         |              |
        |     	       |                                                    |              |
        |     	       |    Students enrolled in Data Science :  {ds_students}          |              |
        |     	       |____________________________________________________|              |
        |     ________________________________________________________________________     |
        |     |                                                                      |     |
        |     | Batch-wise toppers : Python-Django - {', '.join(python_toppers)} (Score : {python_scores})     |     |
        |     |                      Data Analytics - {', '.join(da_toppers)} (Score : {da_scores})    |     |
        |     |                      Data Science  - {', '.join(ds_toppers)} (Score : {ds_scores})      |     |
        |     |______________________________________________________________________|     |
        |                                                                                  |
        |__________________________________________________________________________________|         
            ''')
        
        
   
    def AddStudent(self,name,course,assessment,assignment):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 

            # executing the sql command to insert values in a table
            mycursor.execute("INSERT INTO tblStudent(stud_name,course,assessment,assignment) VALUES (%s,%s,%s,%s)", (name,course,assessment,assignment))
            
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
             
            
        except Exception:
            print(f"Something went wrong")
      
    def RemoveStudent(self,Id):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 

            # executing the sql command to show record before deletion
            mycursor.execute("SELECT * FROM tblStudent WHERE Id=%s", (Id,))
            record=mycursor.fetchone()
            print()
            print('------------------------------------------------------------------------')
            print(f'Id : {record[0]}\nName : {record[1]}\nCourse : {record[2]}\nAssessments Solved : {record[3]}\nAssignments Solved : {record[4]}\nTotal Score : {record[3]*10+record[4]*10}')
            print('------------------------------------------------------------------------')
            
            ch=input('Do you want to Delete this record ? Y/N : ')
            try:
                if ch.lower()=='y':
                    # Executing the delete query using execute method
                    mycursor.execute("DELETE FROM tblStudent WHERE Id=%s",(Id,))
                    print('Deleted Successfully...')
                else:
                    print('Record has kept as it was...')
            except:
                print('Something went wrong...')
            
                
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
             
            
        except Exception:
            print(f"Something went wrong")
            
      
    def UpdateStudent(self,Id):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 

            # executing the sql command to show record before deletion
            mycursor.execute("SELECT * FROM tblStudent WHERE Id=%s", (Id,))
            record=mycursor.fetchone()
            print()
            print('------------------------------------------------------------------------')
            print(f'Id : {record[0]}\nName : {record[1]}\nCourse : {record[2]}\nAssessments Solved : {record[3]}\nAssignments Solved : {record[4]}\nTotal Score : {record[3]*10+record[4]*10}')
            print('------------------------------------------------------------------------')
            
            print()
            name=input('Enter your name : ')
            print(f'Course : {record[2]}')
            assessment=int(input('How many assessments (Tests) did you solved out of 5 ? : '))
            assignment=int(input('How many assignment (Practice Sets) did you solved out of 10 ? : '))
                
            if name:
                new_name=name 
                
            if assessment:
                new_assessment=assessment 
                
            if assignment:
                new_assignment=assignment 
            
            try:
                mycursor.execute("UPDATE tblStudent SET stud_name=%s,assessment=%s,assignment=%s WHERE Id=%s",(new_name,new_assessment,new_assignment,Id))
            except:
                print()
                print('Something went wrong...')
            else:
                print()
                print('Updated Successfully..')
            
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
             
            
        except Exception:
            print(f"Something went wrong")
          
    def ShowAllStudent(self):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 
            
            # excecuting select query and displaying records in ascending order
            mycursor.execute("SELECT * FROM tblStudent") 
            
            # excecuting select query and displaying records in descending order
            # mycursor.execute("SELECT * FROM tblStudent ORDER BY Id DESC") 
            
            # fetching all records
            data=mycursor.fetchall()
            
            for row in data:
                print('-----------------------------------------------------------------------------\n')
                print(f'Id : {row[0]}\nName : {row[1]}\nCourse : {row[2]}\nTotal solved Assessments : {row[3]}\nTotal solved Assignments : {row[4]}\nTotal Marks out of 150 : {row[3]*10+row[4]*10}')
                print()
                
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
            
            
        except Exception:
            print(f"Something went wrong")
            
            
            
            
    def Search_Student(self,name):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb") 

            # Get the cursor object 
            mycursor = mydb.cursor() 
            
            # excecuting select query and displaying records in ascending order
            mycursor.execute("SELECT * FROM tblStudent WHERE stud_name=%s",(name,)) 
            
            # fetching all records
            data=mycursor.fetchall()
            
            for row in data:
                print('-----------------------------------------------------------------------------\n')
                print(f'Id : {row[0]}\nName : {row[1]}\nCourse : {row[2]}\nTotal solved Assessments : {row[3]}\nTotal solved Assignments : {row[4]}\nTotal Marks out of 150 : {row[3]*10+row[4]*10}')
                print()
                
            # commit the changes
            mydb.commit()
            # close cursor
            mycursor.close()
            # close DB connection 
            mydb.close() 
            
            
        except Exception:
            print(f"Something went wrong")
        
        
        
            
    def Batch_Wise_Topper(self):
        print()
        
        for key, _ in self.table.items():
            sorted_dict = self.table[key]
            names = []
            if len(sorted_dict.values()) == 0:
                break
            max_score = max(sorted_dict.values())
            
            for k,v in sorted_dict.items():
                if sorted_dict[k] == max_score:
                    names.append(k)
                    
            names_str = ', '.join(names)        
            print('---------------------------------------------------------------------')
            print(f'Batch : {key}\nName : {names_str}\nScore : {max_score}')


  

