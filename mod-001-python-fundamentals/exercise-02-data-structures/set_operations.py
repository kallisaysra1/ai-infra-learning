# set_operations.py

# Training and validation dataset IDs
train_ids = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
val_ids = {9, 10, 11, 12, 13}
test_ids = {13, 14, 15, 16, 17}

print(f"Training samples: {len(train_ids)}")
print(f"Validation samples: {len(val_ids)}")
print(f"Test samples: {len(test_ids)}")

# Find overlapping samples (data leakage check)
train_val_overlap = train_ids & val_ids  # Intersection
print(f"Train-Val overlap: {train_val_overlap}")

train_test_overlap = train_ids & test_ids
print(f"Train-Test overlap: {train_test_overlap}")

val_test_overlap = val_ids & test_ids
print(f"Val-Test overlap: {val_test_overlap}")

# Union: all unique samples
all_samples = train_ids | val_ids | test_ids
print(f"Total unique samples: {len(all_samples)}")
print(f"All sample IDs: {sorted(all_samples)}")

# Difference: samples only in training
train_only = train_ids - val_ids - test_ids
print(f"Samples only in training: {train_only}")

# Symmetric difference: samples in either but not both
train_val_exclusive = train_ids ^ val_ids
print(f"Exclusive to train or val: {train_val_exclusive}")

# Check if sets are disjoint (no overlap)
is_clean_split = train_ids.isdisjoint(test_ids)
print(f"Clean train-test split: {is_clean_split}")

# Add and remove samples
new_samples = {18, 19, 20}
test_ids_updated = test_ids | new_samples  # Union
print(f"Updated test set: {test_ids_updated}")

# Remove outliers
outliers = {5, 10}
train_cleaned = train_ids - outliers
print(f"Training after removing outliers: {train_cleaned}")

# Subset check
small_set = {1, 2, 3}
is_subset = small_set.issubset(train_ids)
print(f"Is {small_set} subset of training? {is_subset}")

is_superset = train_ids.issuperset(small_set)
print(f"Is training superset of {small_set}? {is_superset}")
