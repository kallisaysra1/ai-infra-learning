# tuple_operations.py

# Model metadata (immutable)
model_metadata = ("ResNet50", "1.0.0", "2024-10-18", 0.92)
model_name, version, date, accuracy = model_metadata  # Unpacking

print(f"Model: {model_name}")
print(f"Version: {version}")
print(f"Released: {date}")
print(f"Accuracy: {accuracy}")

# Tuple of tuples: training history
training_history = (
    (1, 0.85, 0.45),   # (epoch, accuracy, loss)
    (2, 0.88, 0.32),
    (3, 0.91, 0.25),
    (4, 0.92, 0.20),
    (5, 0.93, 0.18)
)

print("\nTraining History:")
for epoch, acc, loss in training_history:
    print(f"Epoch {epoch}: Accuracy={acc:.2f}, Loss={loss:.2f}")

# Find best epoch
best_epoch = max(training_history, key=lambda x: x[1])
print(f"Best epoch: {best_epoch[0]} with accuracy {best_epoch[1]}")

# Named tuples for better readability
from collections import namedtuple

ModelConfig = namedtuple('ModelConfig',
                        ['name', 'layers', 'params', 'memory_mb'])

resnet_config = ModelConfig('ResNet50', 50, 25_500_000, 98)
vgg_config = ModelConfig('VGG16', 16, 138_000_000, 528)

print(f"\n{resnet_config.name}: {resnet_config.params:,} parameters")
print(f"{vgg_config.name}: {vgg_config.params:,} parameters")

# Compare memory
if resnet_config.memory_mb < vgg_config.memory_mb:
    print(f"{resnet_config.name} is more memory efficient")

# Tuple as dictionary key (immutable)
model_performance = {
    ('ResNet50', 'ImageNet'): 0.92,
    ('VGG16', 'ImageNet'): 0.88,
    ('ResNet50', 'CIFAR10'): 0.95,
}

key = ('ResNet50', 'ImageNet')
accuracy = model_performance[key]
print(f"\n{key[0]} on {key[1]}: {accuracy}")

# Return multiple values from function
def train_model(epochs: int) -> tuple:
    """Simulate training, return multiple metrics"""
    final_accuracy = 0.92
    final_loss = 0.15
    training_time = 3600  # seconds
    num_params = 25_500_000

    return final_accuracy, final_loss, training_time, num_params

# Unpack return values
acc, loss, time, params = train_model(50)
print(f"\nTraining complete:")
print(f"  Accuracy: {acc}")
print(f"  Loss: {loss}")
print(f"  Time: {time}s")
print(f"  Parameters: {params:,}")
