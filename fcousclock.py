import time

# 设置专注时间间隔
focus_time = 10

# 获取当前时间
current_time = time.strftime("%Y-%m-%d %H:%M:%S")

# 在屏幕上输出当前时间
print("现在的时间是：", current_time)

while True:
    # 等待1秒
    time.sleep(1)

    # 获取当前时间
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # 在屏幕上输出当前时间
    print("现在的时间是：", current_time)

    # 如果当前时间与上一次时间相差了focus_time秒，则记录当前时间
    if current_time != prev_time:
        prev_time = current_time
