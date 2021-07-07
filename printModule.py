import csv


def print_line(column=None):
    run = True
    while run:
        #name/first,name/last,age,street,city,state,latitude,longitude,ccnumber
        if (column):
            if (column == "firstname"):

        else:
            print_line_str = input("print line: ")
            try:
                print_line_int = int(print_line_str)
            except ValueError:
                if (print_line_str == "exit" or print_line_str == "quit"):
                    run = False
                    break
                print('You must write an integer like so: "1234" without quotes')
                continue

            with open('datasett.csv', newline='') as datasett:
                reader = csv.reader(datasett, delimiter=',', quotechar='|')
                for i, row in enumerate(reader):
                    # print(', '.join(row))
                    if (i == print_line_int):
                        print(row)
                        if (row == "exit" or row == "quit"):
                            run = False
                            break
