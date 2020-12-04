fname = input("Input the Filename = ")

subname= fname[-2:]

if subname == "py":
    ext = "python"
else:
    ext = "none"
print("the extension of file is = ", ext)
