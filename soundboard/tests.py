from sounddevice import play
from soundfile import read
import time


if __name__ == '__main__':

    track = 'Re_ii-Ebisu.wav'

    data, fs = read(track, dtype='float32')
    play(data, fs)

    time.sleep(10)
    print("End")
