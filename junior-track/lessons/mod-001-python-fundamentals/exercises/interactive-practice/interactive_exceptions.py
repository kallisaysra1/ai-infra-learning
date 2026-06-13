# interactive_exceptions.py

# TASK 1: Try to open a file that does not exist, and handle the error gracefully!
try:
    with open("non_existent_logs.txt", "r") as file:
        pass
except FileNotFoundError:
    print("Warning: File does not exist!")

# TASK 2: Gracefully handle missing keys in a configuration dictionary.
server_config = {
    "host": "192.168.1.50",
    "use_ssl": True
}

try:
    port = server_config["port"]
except KeyError:
    print("Error: Config key 'port' is missing!")
