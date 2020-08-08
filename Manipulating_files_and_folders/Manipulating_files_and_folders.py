#create new file and update existing files

#create a file
#open a file
f = open("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file.txt","w")
#write to a file
f.write("Hey!!")
#write multiple lines
#create a list 
line_list = ["\nHello\n","How are You?\n","I'm fine.\n","Ok Bye!!"]
f.writelines(line_list)
#close 
f.close()



#update a file
fi= open("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file.txt","a")
fi.write("Take Care.")
fi.close()


#read data from a file
ff= open("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file.txt","r")
content=ff.read()
#append read data to the other file
fl = open("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file1.txt","a")
fl.write(content)
fl.close()
ff.close()


#Moving files or folders


import os
import shutil
#make new directory 
os.mkdir("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\")
#move file
shutil.move("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\file.txt")
#copy file
shutil.copy("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\file1.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\file1.txt")
#copy multiple files -- using loops
file_list = ["F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\z.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\zz.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\zzz.txt"]
for i in file_list:
	shutil.copy(i,"F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\")

#rename file and folder

os.rename("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\z.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\ISB\\za.txt")
#multiple files
re_files = ["F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\1st sem.txt","F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\2nd sem.txt"]
for i in re_files:
	j=i.split(" ")
	os.rename(i,j[0]+" "+j[1]+" Semester.txt") 

#deleting a file
os.remove("F:\\Education\\Alien Brains\\Manipulating_files_and_folders\\z.txt")