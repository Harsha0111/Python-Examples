import time

user_input_mins = int(input("How many minutes you want set the count down?: "))
user_input_sec = int(input("How many seconds you want set the count down?: "))
seconds = user_input_mins * 60 + user_input_sec


def count_down(seconds):
    start_time = 0

    while start_time < seconds:
        time.sleep(1)
        start_time += 1

        time_left = seconds - start_time
        mins_left = time_left // 60
        secs_left = time_left % 60

        print(f"Your count down ends in {mins_left}mins:{secs_left}sec")


count_down(seconds)
