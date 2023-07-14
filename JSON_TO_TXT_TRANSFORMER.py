import json

def open_file():
    try:
        path = input("Enter path of JSON file: ")
        file = open(path)
        data = json.load(file)
        file.close()
        return data['values']
    except:
        print("Error when loading file")

def write_file(values):
    name = input("Enter name of org: ")
    writer = open(f"{name}.txt", "w")

    for i in range(len(values)):
        if i == len(values) - 1:
            writer.write(values[i]['value'])
        else:
            writer.write(values[i]['value'] + "\n")

    writer.close()

    print("**********Completed**********")


def main():
    values = open_file()

    write_file(values)

main()
