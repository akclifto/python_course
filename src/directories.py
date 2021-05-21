from pathlib import Path

# Will take path from abs or relative
# Windows: abs path 
# C:/Windows/System32/.../myfilePathEnd
# MacOS/Linux: abs path
# user/local/bin/.../myfilePathEnd

# relative paths: using the packages/school_package as working example.

path = Path("src/packages/school_package")
print(path.exists())

# make a directory called email at the end of relative path

# path = Path("src/packages/school_package/email")
# print(path.mkdir()) 
# remove a directory
# print(path.rmdir()) 

# iterate all files in a directory path: '*' means select everything
path = Path()
# print(path.glob("*.py"))
for file in path.glob("*"):
    print(file)
