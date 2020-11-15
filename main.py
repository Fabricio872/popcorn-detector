import time as time_lib

import numpy as np
import sounddevice as sd

duration = 50  # in seconds
warmup_time = 2  # in seconds
max_pop_time = 3  # in seconds time
pop_threshold = 15  # in volume units
min_pop_time = 512  # in milliseconds
pop_times = []


def pop_time():
    return time_lib.time() - pop_times[-1]


def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if (int(volume_norm) > pop_threshold):
        if (pop_times):
            # print("%f pops/second" % (round(1 / pop_time(), 2)), end='\r', flush=True)
            print(len(pop_times), end='\r', flush=True)

        pop_times.append(time_lib.time())
        time_lib.sleep(min_pop_time / 1000)


def main():
    stream = sd.InputStream(callback=audio_callback)
    with stream:
        sd.sleep(duration * 1000)
    print('\n', len(pop_times), 'total popcorns')


if __name__ == '__main__':
    main()
