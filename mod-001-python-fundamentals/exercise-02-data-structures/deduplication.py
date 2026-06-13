# deduplication.py

from typing import List, Set, Dict

def remove_duplicate_samples(sample_ids: List[int]) -> List[int]:
    """Remove duplicates while preserving order"""
    seen = set()
    unique_samples = []

    for sample_id in sample_ids:
        if sample_id not in seen:
            seen.add(sample_id)
            unique_samples.append(sample_id)

    return unique_samples

def find_duplicate_files(filepaths: List[str]) -> Dict[str, List[str]]:
    """Find duplicate files by basename"""
    from collections import defaultdict
    import os

    basename_map = defaultdict(list)

    for filepath in filepaths:
        basename = os.path.basename(filepath)
        basename_map[basename].append(filepath)

    # Return only duplicates
    duplicates = {k: v for k, v in basename_map.items() if len(v) > 1}
    return duplicates

def validate_unique_classes(dataset: List[tuple]) -> bool:
    """Validate that all class labels are unique per sample"""
    sample_ids = [item[0] for item in dataset]
    unique_ids = set(sample_ids)

    if len(sample_ids) != len(unique_ids):
        print(f"Warning: {len(sample_ids) - len(unique_ids)} duplicate sample IDs found")
        return False
    return True

# Example: dataset with duplicates
raw_dataset = [
    (1, "cat", "img1.jpg"),
    (2, "dog", "img2.jpg"),
    (3, "cat", "img3.jpg"),
    (1, "cat", "img1_copy.jpg"),  # Duplicate ID
    (4, "bird", "img4.jpg"),
    (2, "dog", "img2_v2.jpg"),    # Duplicate ID
]

print("Original dataset size:", len(raw_dataset))

# Extract unique IDs
sample_ids = [item[0] for item in raw_dataset]
unique_ids = list(set(sample_ids))
print(f"Unique sample IDs: {len(unique_ids)} (from {len(sample_ids)} total)")

# Remove duplicates preserving first occurrence
cleaned_ids = remove_duplicate_samples(sample_ids)
print(f"Cleaned IDs: {cleaned_ids}")

# Find duplicate entries
seen_ids = set()
duplicates = []
for item in raw_dataset:
    if item[0] in seen_ids:
        duplicates.append(item)
    seen_ids.add(item[0])

print(f"Duplicate entries: {duplicates}")

# Validate uniqueness
is_valid = validate_unique_classes(raw_dataset)
print(f"Dataset has unique IDs: {is_valid}")

# Example: find duplicate filenames
image_files = [
    "/data/train/img001.jpg",
    "/data/train/img002.jpg",
    "/data/val/img001.jpg",      # Same basename
    "/data/test/img002.jpg",     # Same basename
    "/data/train/img003.jpg"
]

duplicate_files = find_duplicate_files(image_files)
print(f"\nDuplicate filenames: {duplicate_files}")

# Set operations for class distribution
class_labels = ["cat", "dog", "cat", "bird", "dog", "cat", "fish", "dog"]
unique_classes = set(class_labels)
print(f"\nUnique classes: {unique_classes}")
print(f"Number of classes: {len(unique_classes)}")

# Count occurrences
from collections import Counter
class_counts = Counter(class_labels)
print(f"Class distribution: {dict(class_counts)}")
