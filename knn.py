import csv
import math

datain = []

pointx = 3
pointy = 9
result_distance = []


def input_data():
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            datain.append(row)

def calculator_distance():
    for e in datain:
        distance = math.sqrt((pointx - int(e[0]))**2 + (pointy - int(e[1]))**2)
        result_distance.append((distance, e[2]))
    return result_distance.sort(key=lambda tup: tup[0])

def nearest_neighbor(K=None):
    nearest = result_distance[:K]
    positive = []
    negative = []
    for e in nearest:
        if e[1] == '-':
            negative.append(e)
        else:
            positive.append(e)
    return '-' if len(negative) > len(positive) else '+'

def main():
    input_data()
    calculator_distance()
    result = nearest_neighbor(5)
    print('Testing is class: ', result)


if __name__ == '__main__':
    main()
