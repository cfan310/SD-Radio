# installed pyrtlsdr w/ pip

# Realtek RTL2832U

import numpy as np

arr1 = np.array([2, 4, 6, 8, 10])

result = np.square(arr1)

print(result)

# IP address using np.raise to a power of num of items in the array

# first give a subnet
# then iterate through subnet
# if first three are 169, print APIPA
# if first octet is 10, 172 or 192, assign it to a subnetwork
# automatic SDR subnetting based on given frequencies and locations

ipaddress1 = np.array([])