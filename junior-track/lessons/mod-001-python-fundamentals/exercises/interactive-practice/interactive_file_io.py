# interactive_file_io.py

# TASK 1: Read 'server_logs.txt' line-by-line and print each line to the screen.
with open("server_logs.txt", "r") as file:
    for line in file:
        print(line.strip())

# TASK 2: Filter error logs and write them to a new file.
with open("server_logs.txt", "r") as infile, open("errors_report.txt", "w") as outfile:
    for line in infile:
        if "ERROR" in line:
            outfile.write(line)
