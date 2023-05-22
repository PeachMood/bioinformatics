#!/usr/bin/env python3

# Get the filename from the command line argument
import sys
filename = sys.argv[1]

# Get the first line with "mapped" and extract the percent value
with open(filename) as f:
    for line in f:
        if "mapped" in line and "primary" in line:
            percent_str = line.split("(")[1].split("%")[0]
            percent_val = float(percent_str)
            break

# Check if the percent value is higher than 90%
print(f"Mapped percentage: {percent_val}")
if percent_val > 90:
    print("Result: OK")
else:
    print("Result: BAD")
