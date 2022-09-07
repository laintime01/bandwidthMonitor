import time
import psutil
# psutil = process and system utilities


def monitor_bandwidth():
    last_data_recv = psutil.net_io_counters().bytes_recv
    last_data_sent = psutil.net_io_counters().bytes_sent
    last_total = last_data_recv + last_data_sent

    while True:
        data_recv = psutil.net_io_counters().bytes_recv
        data_sent = psutil.net_io_counters().bytes_sent
        total = data_sent + data_recv

        new_data_recv = data_recv - last_data_recv
        new_data_sent = data_sent - last_data_sent
        new_total = total - last_total

        mb_recv = new_data_recv / 1024 / 1024
        mb_sent = new_data_sent / 1024 / 1024
        mb_total = new_total / 1024 / 1024

        print(f"{mb_recv:.2f} MB received, {mb_sent:.2f} MB sent, {mb_total:.2f} MB total")

        last_data_sent = data_sent
        last_data_recv = data_recv
        last_total = total

        time.sleep(1)


if __name__ == '__main__':
    monitor_bandwidth()




