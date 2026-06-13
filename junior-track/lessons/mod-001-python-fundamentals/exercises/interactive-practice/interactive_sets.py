# interactive_sets.py

# Here are the IDs of our training and validation datasets (Sets use curly braces)
train_ids = {101, 102, 103, 104, 105}
val_ids = {104, 105, 106, 107}

# TASK 5: Find the duplicate IDs present in BOTH training and validation sets.
overlapping_ids = train_ids & val_ids
print(overlapping_ids)
