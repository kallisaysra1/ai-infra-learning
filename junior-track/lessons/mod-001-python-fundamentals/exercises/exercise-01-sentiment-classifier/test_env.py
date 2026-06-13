import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read and print environment variables
model_name = os.getenv("MODEL_NAME")
batch_size = os.getenv("BATCH_SIZE")
device = os.getenv("DEVICE")

print(f"Model: {model_name}")
print(f"Batch Size: {batch_size}")
print(f"Device: {device}")

# Type conversion
batch_size_int = int(os.getenv("BATCH_SIZE", "32"))
print(f"Batch size as integer: {batch_size_int}")
