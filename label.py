import pandas as pd 
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
    valid: bool = False 

    while not valid: 
        x = input("Please enter the timestep (candle size) for which you'd like to label... \n 5 -> 5 minute 15 -> 15 minute 30 -> 30 minute")



def add_label_data():

    
    start = get_validate_timestamp("Please enter the timestamp for which you'd like to start from")


    data_length: int =  len(df["timestamp"])
    
    entry_exit_list: list = [] 
    count: int = 0

    print("Starting timestamp --> ", df["timestamp"][0])
    while(len(entry_exit_list) != data_length):
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
    df = pd.read_csv("../../data/candles/ETHUSDT-30m.csv")
    add_label_data(df)
    df.to_csv("ETHUSDT-30mEE", index=False)
