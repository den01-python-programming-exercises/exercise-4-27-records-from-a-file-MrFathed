import csv

def main():
    #write your code below this line
    file_name = input("Name of the file:")

    with open(file_name) as f:
        data = f.read().splitlines()

    for line in data:
        stuff = line.split(',')
        name = stuff[0]
        age = stuff[1]

        if age == '1':
            age = age + ' year'
        else:
            age = age + ' years'
        
        print("{}, age: {}".format(name, age))

if __name__ == '__main__':
    main()
