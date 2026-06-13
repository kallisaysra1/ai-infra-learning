# interactive_dicts.py

# Here is our dictionary of model configurations (Dictionaries use curly braces and key: value pairs)
config = {
    "model_name": "vLLM-Llama3",
    "batch_size": 32,
    "learning_rate": 0.001,
    "use_gpu": True
}

# TASK 3: Look up and print the value of the "batch_size" key.
print(config["batch_size"])

# TASK 4: Update the batch size to 64 and add a new configuration key.
config["batch_size"] = 64
print(config)
