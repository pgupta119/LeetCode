import sys

# Check for errors
if len(sys.argv) < 2:
    # print("Too few arguments")
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     # print('Too many arguments')
#     sys.exit("Too many arguments")
# else:
# Print name tags


# slices
for arg in sys.argv[1:]:
    print("Hello", "My name is", arg)
