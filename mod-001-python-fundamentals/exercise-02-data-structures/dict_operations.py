# dict_operations.py

# Model configuration
model_config = {
    "name": "ResNet50",
    "version": "1.0.0",
    "input_shape": (224, 224, 3),
    "num_classes": 1000,
    "pretrained": True,
    "freeze_layers": 10
}

# Access values
print(f"Model: {model_config['name']}")
print(f"Version: {model_config['version']}")

# Safe access with get()
optimizer = model_config.get("optimizer", "adam")  # Default to adam
print(f"Optimizer: {optimizer}")

# Update config
model_config["learning_rate"] = 0.001
model_config.update({
    "optimizer": "adam",
    "weight_decay": 0.0001
})

print(f"Updated config: {model_config}")

# Check key existence
if "dropout" not in model_config:
    model_config["dropout"] = 0.5
    print("Added dropout configuration")

# Iterate over config
print("\nConfiguration summary:")
for key, value in model_config.items():
    print(f"  {key}: {value}")

# Get all keys and values
config_keys = list(model_config.keys())
config_values = list(model_config.values())
print(f"\nConfig keys: {config_keys}")

# Remove keys
removed_value = model_config.pop("freeze_layers", None)
print(f"Removed freeze_layers: {removed_value}")

# Clear specific keys
temp_config = model_config.copy()
temp_config.clear()
print(f"Cleared config: {temp_config}")
print(f"Original still intact: {len(model_config)} keys")
