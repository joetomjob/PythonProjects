import selectionsort


def read_file(filename):
    with open(filename) as data:
        name_of_file = data.readline()
        dict_v = {}
        for item in data:
            parts = item.strip().split()
            dict_v[parts[0]] = parts[1:]
        return dict_v, name_of_file


def get_the_final_list(profit, count):
    sell = []
    r = 0
    total_profit = 0
    for i in range(len(profit)):
        if profit[i][2] < count - r:
            sell.append(profit[i])
            r = r + profit[i][2]
            total_profit += profit[i][1] * profit[i][2]
        else:
            sell.append([profit[i][0], profit[i][1], count - r, profit[i][3]])
            total_profit += profit[i][1] * (count - r)
            break
    return sell, total_profit


def main():
    hill_town_file = input("Enter the first fileName :")
    valley_dale_file = input("Enter the second fileName :")
    count = int(input("Enter the maximum amount of items that can be carried : "))

    dict_v, name_of_valley_dale_file = read_file(valley_dale_file)
    dict_h, name_of_hill_town_file = read_file(hill_town_file)

    profit_h = []
    profit_v = []

    for i in dict_h.keys():
        if int(dict_h[i][1]) > int(dict_v[i][1]):
            profit_h.append([i, int(dict_h[i][1]) - int(dict_v[i][1]), int(dict_v[i][0]), name_of_valley_dale_file.strip()])
        elif int(dict_h[i][1]) < int(dict_v[i][1]):
            profit_v.append([i, int(dict_v[i][1]) - int(dict_h[i][1]), int(dict_h[i][0]), name_of_hill_town_file.strip()])

    sort_object = selectionsort
    profit_h = sort_object.selection_sort(profit_h)
    profit_v = sort_object.selection_sort(profit_v)

    sell_h, tot_profit_h = get_the_final_list(profit_h, count)
    sell_v, tot_profit_v = get_the_final_list(profit_v, count)

    if tot_profit_h > tot_profit_v:
        income = 0
        print("Go to " + sell_h[0][3] + " and buy :")
        for i in range(len(sell_h)):
            print(str(sell_h[i][2]) + " " + sell_h[i][0] + " for a profit of " + str(sell_h[i][2] * sell_h[i][1]))
            income = income + sell_h[i][2] * sell_h[i][1]
        print("income is " + str(income))
    else:
        income = 0
        print("Go to " + sell_v[0][3] + " and buy :")
        for i in range(len(sell_v)):
            print(str(sell_v[i][2]) + " " + sell_v[i][0] + " for a profit of " + str(sell_v[i][2] * sell_v[i][1]))
            income = income + sell_v[i][2] * sell_v[i][1]
        print("income is " + str(income))


if __name__ == '__main__':
    main()
