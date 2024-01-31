# installed pyrtlsdr w/ pip

# Realtek RTL2832U

# RTL-SDR Blog V3 R860 RTL2832U 1PPM TCXO HF Bias Tee SMA Software Defined Radio

import numpy as np
from rtlsdr import RtlSdr


# numpy > numerical python (provide mathematical operations on arrays)

def main():
    sdr = RtlSdr()

    # device configuration
    sdr.sample_rate = 2.048e6   # set initially to 2,480,000
    sdr.center_freq = 1.043e8                      # 104,300,000 MHz for Q-104.3 classic rock radio in NYC
    sdr.frequency_correction = 60   #PPM            parts per million
    sdr.gain = 'auto'

    # frequency variation = 6,258,000,000 Hz

    # variation 6 GHz

    # read samples
    samples = sdr.read_samples(256*1024)

    print(samples)

# Cleanup
    sdr.close()

if __name__ == "__main__":
    main()








'''
arr1 = np.array([2, 4, 6, 8, 10])

result = np.square(arr1)

print(result)

# add numpy filter for imported array

arr = np.array([5, 10, 15, 20])

# test array

arr2 = np.array([128, 64, 32, 16, 8, 4, 2, 1])

result = np.square(arr2)

print(result)
'''
