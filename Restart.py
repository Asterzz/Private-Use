import os
import time
 
 
def get_pid(itme):
    pids = os.popen("pgrep -f {}".format(itme))
    pids = pids.read()
    print(item, "PID IS:", pids, type(pids))
    return pids
 
 
def kill_item(item):
    result = os.popen("pkill -f {}".format(item))
    print("killed --------", result.read())
    return result.read()
 
 
def start_item(item, start_commond):
    result = os.popen(start_commond)
    print("starting-------{}".format(str(result.read())))
    time.sleep(10)
    if get_pid(item):
        print("{} started".format(item))
 
 
def start(item, start_command):
    print("status: {}".format(get_pid(item)))
    if get_pid(item):  
        print("already start, start killing------------")
        kill_item(item)
        print("kill succeed--------------")
        time.sleep(10)
        start_item(item, start_command)
        print("restart succeed-----------------")
    else:  
        start_item(item, start_command)
 
 
if __name__ == '__main__':
    item = "manage_qa_tools"  
    start_command = "nohup python3 app.py >app.log 2>&1 &"  
    start(item, start_command)
