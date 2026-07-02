# file=open("sample.txt",'w')
# string="""hi
# hello
# how are you"""
# file.write(string)
# file.close()
# print("sample.txt file created and content also added")

### readimg content from file
# with open("sample.txt",'r') as file:
#     data = file.read()
#     print(data[:5])
#     print("data:",data)
# print("data readed successfully")


# with open("output.txt",'r') as file:
#     line =file.readline()
#     lines = file.readlines()
#     print("Line:",line)
#     print("Lines:",lines)
# print("Program completed")

# file=open("output.txt",'w')
# string="""1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10"""
# file.write(string)
# file.close()
# print("output.txt file created and content also added")

n=int(input())
with open("output.txt",'w') as file:
    for i in range(1,n+1):
        file.write(str(i)+"\n")