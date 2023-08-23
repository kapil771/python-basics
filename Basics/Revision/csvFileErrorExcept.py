import csv

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    colors = []
    for row in readCSV:
        colors.append(row[2])

    try:
        color = input('What color you want?')

        if color in colors:
            print("'"+color+"' is in list")
        else:
            print("Color not found")
    except NameError as e:
        print(e)
