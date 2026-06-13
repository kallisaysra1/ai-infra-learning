# interactive_functions.py

# We define a function using 'def' and a name. 
# Inside the parentheses, we write the name of the input variable (parameter).
def count_active_servers(statuses):
    active_count = 0
    for status in statuses:
        if status == True:
            active_count = active_count + 1
    
    # 'return' sends the final value back to the program
    return active_count

# TASK 2: Use (call) our function!
cluster_b = [True, True, True, True, False, False]

result = count_active_servers(cluster_b)
print(result)
