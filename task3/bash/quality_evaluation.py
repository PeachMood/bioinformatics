# Get the filename from the command line argument
import sys
filename = sys.argv[1]

# Get the first line with "mapped" and extract the percent value
with open(filename) as f:
    for line in f:
        if "mapped" in line and not "primary" in line:
            percent_str = line.split("(")[1].split("%")[0]
            percent_val = float(percent_str)
            break

# Check if the percent value is higher than 90%
if percent_val > 90:
    print("OK")
else:
    print("BAD")
