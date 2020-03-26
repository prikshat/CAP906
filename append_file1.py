#append used to add your new text in your existing file
file=open('file_write.txt','a')
file.write("this add in file after existing contents");
file.close()
print("Append executed")