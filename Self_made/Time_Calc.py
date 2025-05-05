average_speed = int(input('Average speed: ')) # 1
distance = int(input('Total distance: ')) # 2


def calc_time():
    time = distance / average_speed
    print(f'your total time is {time} hr')
    
calc_time()