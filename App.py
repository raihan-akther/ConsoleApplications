



import os
choice=''
while choice not in ['Yes','No']:
    choice=input('Do you want to file read or write? say yes or no: ')

    if choice.lower()=='yes':
        u=''
        while u not in [1,2]:

                u=input('if you want file read -press 1 or if you want file write-press 2: ')

                if u=='1':
                        for root, dirs, files in os.walk(r"C:\Users\rhlen\Desktop\New folder\New folder (2)\peopleData"):
                            file = input('Filename: ')
                            extension = input('Extension: ')
                            filename = ('{0}.{1}'.format(file, extension))

                            if filename in files:
                                file = open('{0}'.format(filename), "r")
                                a=file.read()
                                print(a)
                                file.close
                            else:
                                print('file not found')
                                print (os.path.join(root, name))
                            break


                if u=='2':
                    name=input('Name: ')
                    age=input('Age: ')
                    gender=input('Gender: ')
                    work=input('Work: ')
                    file= input('Filename: ')
                    extension=input('Extension: ')
                    filename=('{0}.{1}'.format(file,extension))
                    file=open('{0}'.format(filename),"w")
                    a=file.write(' name= {0} \n age={1} \n gender={2} \n work={3}'.format(name,age,gender,work))
                    print(a)
                    file.close


    if choice=='no':
            print('sorry')
    break
