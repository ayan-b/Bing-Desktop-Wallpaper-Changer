from sys import stdout
import time


def human_readable_size(number_bytes):
    for x in ['bytes', 'KB', 'MB']:
        if number_bytes < 1024.0:
            return "%3.2f %s" % (number_bytes, x)
        number_bytes /= 1024.0


def print_download_status(block_count, block_size, total_size):
    global start_time
    total_sz = total_size
    total_size = human_readable_size(total_size)
    written_size = human_readable_size(min(block_count * block_size, total_sz))
    if block_count == 0:
        start_time = time.time()
        return
    percent = int(block_count * block_size * 100 / total_sz)
    duration = time.time() - start_time
    if duration == 0:
        duration = 1
    speed = human_readable_size((block_count*block_size)/duration)
    # Adding space padding at the end to ensure we overwrite the whole line
    stdout.write("\r%s of %s | %d percent | %0.2fs passed | %s/s " % (
        written_size, total_size, min(100, percent), duration, speed))
    stdout.write("|%s%s|  " % ('#'*int(percent/2), ' '*(50-int(percent/2))))
    stdout.flush()
