student={1015:{"rollno:":1,"name":"Kamran","Marks":[93,95,94]},
         1016:{"rollno:":2,"name":"Hassan","Marks":[90,90,90]},
         1017:{"rollno:":3,"name":"Irqan","Marks":[90,90,92]}
        }


for k,v in student.items():
    #print(k,v)
    print(v["name"],v["Marks"])