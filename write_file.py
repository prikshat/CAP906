content="Hello this data is written in file after execution"  #write contents which you want to write in the file
file=open('file_write.txt','w')
# w used to write in file
file.write(content)
print("Written in file")