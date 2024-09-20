import psutil

# CPU
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_percent(interval=1))
# print(psutil.cpu_times().system)
# print(psutil.cpu_stats())
# print(psutil.cpu_freq())

# RAM
print(psutil.virtual_memory())
print(psutil.swap_memory())

# HDD
print(psutil.disk_usage('/'))
print(psutil.disk_partitions())