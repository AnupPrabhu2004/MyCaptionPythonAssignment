import math as M
Radius=float(input("please enter the radius of circle:"))
area_of_circle=M.pi*Radius*Radius
print("The area of the given circle is:",area_of_circle)
def get_file_extension(filename):
    parts = filename.split(".")
    
    if len(parts) > 1 and parts[0] != "" and parts[-1] != "":
        return parts[-1]
    else:
        return ""

# Accept a filename from the user
filename = input("Enter a filename: ")

# Get the extension of the filename
extension = get_file_extension(filename)

if extension:
    print("The extension of the file is:", extension)
else:
    print("No extension found.")
