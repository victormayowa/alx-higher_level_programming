#!/usr/bin/python3
''' get desired statistics from file '''


import sys
''' import system module '''


def print_stats(total_size, status_counts):
    """
    Prints the statistics for the given file size and status code counts.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing status code counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

# Initialize variables


line_count = 0
total_size = 0
status_counts = {}

try:
    # Process input line by line
    for line in sys.stdin:
        # Split the line by spaces
        parts = line.split(" ")
        if len(parts) >= 7:
            # Extract the status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])
            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            # Increment line count
            line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats(total_size, status_counts)
