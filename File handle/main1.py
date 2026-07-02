import csv
# with open("test.csv",'w',newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(['name','contact'])
#     writer.writerows([['greeshma','9392375701'],["sai",9440414666]])


with open("test.csv",'r',newline="") as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)