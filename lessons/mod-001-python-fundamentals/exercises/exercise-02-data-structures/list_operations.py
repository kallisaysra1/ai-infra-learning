# list_operations.py

# Sample dataset: image file paths for training
training_images = [
    "img_0001.jpg",
    "img_0002.jpg",
    "img_0003.jpg",
    "img_0004.jpg",
    "img_0005.jpg"
]

# Print dataset information
print(f"Total training images: {len(training_images)}")
print(f"First image: {training_images[0]}")
print(f"Last image: {training_images[-1]}")

# Add new images
training_images.append("img_0006.jpg")
training_images.extend(["img_0007.jpg", "img_0008.jpg"])
print(f"After adding: {len(training_images)} images")

# Insert image at specific position
training_images.insert(0, "img_0000.jpg")
print(f"First image now: {training_images[0]}")

# Remove images
removed = training_images.pop()  # Remove last
print(f"Removed: {removed}")

training_images.remove("img_0000.jpg")  # Remove by value
print(f"Final count: {len(training_images)}")

# Check if image exists
if "img_0003.jpg" in training_images:
    index = training_images.index("img_0003.jpg")
    print(f"Found img_0003.jpg at index {index}")

# Slice operations (get batches)
batch_size = 3
batch_1 = training_images[0:batch_size]
batch_2 = training_images[batch_size:batch_size*2]
print(f"Batch 1: {batch_1}")
print(f"Batch 2: {batch_2}")

# Reverse and sort
training_images_sorted = sorted(training_images)
print(f"Sorted: {training_images_sorted}")

training_images_reversed = list(reversed(training_images))
print(f"Reversed: {training_images_reversed}")

# Additional Tasks from Exercise
print("\n--- Additional Tasks ---")
# 1. Add 10 more images
extra_images = [f"img_{i:04d}.jpg" for i in range(9, 19)]
training_images.extend(extra_images)
print(f"Added 10 more images. Total now: {len(training_images)}")

# 2. Create batches of size 4
batch_size_4 = 4
batches_4 = [training_images[i:i+batch_size_4] for i in range(0, len(training_images), batch_size_4)]
print("Batches of size 4:")
for i, b in enumerate(batches_4):
    print(f"  Batch {i+1}: {b}")

# 3. Find all images with "000" in their name
images_with_000 = [img for img in training_images if "000" in img]
print(f"Images with '000' in name: {images_with_000}")
