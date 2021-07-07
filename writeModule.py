import csv
# data = []


def append_lines(file_name=None, read_data=[]):
    data = []
    index = 0

    if (file_name):
        while True:
            if (file_name[-4:] != ".csv"):
                print("Filename not valid. Try again.")
                file_name = input("> ")
            break

        with open(file_name, newline='') as read:
            reader = csv.reader(read, delimiter=',')  # , quotechar='|')
            for row in reader:
                index += 1
                print(row)  # TODO FJERNE
                data.append(row)
                if (row == "exit" or row == "quit"):
                    break
        lines = 0

        with open("testFileWrite.csv", newline='') as file:
            reader = csv.reader(file)
            lines = len(list(reader))

        with open("testFileWrite.csv", "a", newline='') as write:
            writer = csv.writer(write)
            for i, row in enumerate(data):
                row.insert(0, i + 1 + lines)
                writer.writerow(row)
            print(len(data))
            print(data)

    elif (len(read_data) != 0):
        #data = [] #read_data
        lines = 0

        with open("testFileWrite.csv", newline='') as file:
            reader = csv.reader(file)
            lines = len(list(reader))

        with open("testFileWrite.csv", "a", newline='') as write:
            while True:
                print("Data format:")
                print("seq,name/first,name/last,age,street,city,state,latitude,longitude,ccnumber")
                print("Type 'exit' or 'quit' when done")
                innput = input("New data: ")
                if (innput == "exit" or innput == "quit"):
                    break
                print(data, "54")
                data.append(innput)
            writer = csv.writer(write)
            for i, row in enumerate(data):
                row.insert(0, i + 1 + lines)
                writer.writerow(row)
            print(len(data), "60")
            print(data, "61")
