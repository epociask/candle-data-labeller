import pandas as pd 
import datetime
# 1-> buy
# 0-> sell
# -1-> hold

def get_validate_timestamp(message: str):
    val = "2020-" + input(f"{message}: ") + ":00"
    
    if len(val) != 19 or "2020" not in val or val.count("-") != 2 or val.count(":") != 2 or val[10] != " ":
        print("--Invalid format... please try again --")
        return get_validate_timestamp(message)


    return val 

def get_time_step():
    while True: 
        x = input("Please enter the timestep (candle size) for which you'd like to label... \n 5 -> 5 minute 15 -> 15 minute 30 -> 30 minute")
        
        if x in ['15', '5', '30']:
            return x 

def generate_time_list(timestamp: str, step: int):
    
    l = []
    val = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()

    while val <= now: 
        temp = val + datetime.timedelta(minutes = int(step))
        l.append(datetime.datetime.strftime(temp, "%Y-%m-%d %H:%M:%S"))
        val = temp 

    return l 

def add_label_data():

    
    start = get_validate_timestamp("Please enter the timestamp for which you'd like to start from")

    step = get_time_step()

    time_list: list = generate_time_list(start, step) 

    print(time_list)

    entry_exit_list: list = [] 
    count: int = 0

    while(len(entry_exit_list) != len(time_list)):
        buy_enter = get_validate_timestamp("Please enter entry timestamp for buy range")
        buy_exit = get_validate_timestamp("Please enter exit timestamp for buy range")
        sell_enter = get_validate_timestamp("Please enter entry timestamp for sell range")
        sell_exit = get_validate_timestamp("Please enter exit timestamp for sell range")
        
        print(f"Buy enter: {buy_enter} \nBuy Exit: {buy_exit} \nSell Enter: {sell_enter} Sell Exit: {sell_exit}")
        
        if input("Are you happy with your selection?? If not please enter `n` or `no`").strip().lower() in ['n', 'no']:
            continue 

        while(df["timestamp"][count] <= buy_enter):
            print("buy enter ", df["timestamp"][count])
            entry_exit_list[count] = -1
            count+=1 

        while(df["timestamp"][count] <= buy_exit):
            print("buy exit ", df["timestamp"][count])
            entry_exit_list[count] = 1
            count+=1

        while(df['timestamp'][count] <= sell_enter):
            print("sell enter ", df["timestamp"][count])
            entry_exit_list[count] = -1
            count+=1

        while(df['timestamp'][count] <= sell_exit):
            print("sell exit ", df["timestamp"][count])
            entry_exit_list[count] = 0 
            count+=1

    return df 


if __name__ == '__main__':
    add_label_data()
