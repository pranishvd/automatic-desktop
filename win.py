import os



# enter the directory name
dirs = str(input("Enter the dir name = ")) 
# enter the path name
the_path = str(input("Enter the path = "))

# the current path
print(f"The current Path is {os.getcwd()}")

print("for Changing the Path")
# for changing the path
os.chdir(the_path)
print(f" dir is changed {os.getcwd}")
# colleting all directory information to variables
alls = os.listdir()
# checking the duplicate or same directory name in current path
if dirs not in alls:
# creting the directory
    os.mkdir(dirs)
else:
    print(f"no need to create directory {dirs} is here current path,please change directory name")


remove_dir =input("Want to remove dir Y/N = ")
# checking all directory and helping to remove the directory
if remove_dir =='Y' or 'y':
    for i in alls:
        print(i)
        choice =input("remove above dir Y/N =")
        if choice ==('Y' or 'y'):
            os.rmdir(i)


print("Thanks for using")




