
def main():
    print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    print("Average = " + str(calc_average(temp_list)))
    print("Min , Max = " + str(find_min_max(temp_list)))
    sorted_temp = sort_temperature(temp_list)
    print("Median = " + str(calc_median_temperature(sorted_temp)))
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    number = input('Enter the number:')
    number_list = number.split(",")
    temp = []
    for num in number_list:
        temp.append(round(float(num), 1))
    return temp

def calc_average(temp):
    total_sum = sum(temp)
    total_number = len(temp)
    average = total_sum/total_number
    return average

def find_min_max(temp):
    maximum = max(temp)
    minimum = min(temp)
    min_max = [minimum, maximum]
    return min_max

def sort_temperature(temp):
    sorted_temp = sorted(temp)
    print(sorted_temp)
    return sorted_temp
def calc_median_temperature(sorted_temp):
    middle = int(len(sorted_temp)/2)

    if ((len(sorted_temp) % 2) == 0):
        median = (sorted_temp[middle] + sorted_temp[middle-1]) / 2
    else:
        median = sorted_temp[middle]
    return median

if __name__ == "__main__":
    main()