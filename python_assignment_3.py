import psutil
import time

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def get_cpu_threshold():
    cpu_count = psutil.cpu_count()
    cpu_threshold =5 * cpu_count 
    return cpu_threshold

while True:
    cpu_usage = get_cpu_usage()
    cpu_threshold = get_cpu_threshold()

    if cpu_usage > 30:
        print(f"Warning: CPU usage is above threshold! Current usage: {cpu_usage}%, Threshold: {cpu_threshold}%")
    else:
        print(f"CPU usage: {cpu_usage}%, Threshold: {cpu_threshold}%")

    time.sleep(5) 
    
