if __name__ == '__main__':
    temp_value = 0
    list = []


    with open('input.txt') as file:
        data = file.read().split("\n")

    for i in data:
        if i == "":
            temp_value = 0
        else:
            num = int(i)
            temp_value += num
        list.append(temp_value)

    list.sort(reverse = True)
    print(list[0])
    print(list[0]+list[1]+list[2])
    print(list)

