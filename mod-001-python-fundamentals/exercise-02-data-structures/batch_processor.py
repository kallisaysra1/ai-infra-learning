# batch_processor.py

import random
from typing import List, Tuple, Dict
from collections import defaultdict

class DataBatchProcessor:
    """Process data in batches for ML training"""

    def __init__(self, data: List, batch_size: int, shuffle: bool = True):
        self.data = data.copy()
        self.batch_size = batch_size
        self.shuffle = shuffle

    def get_batches(self, drop_last: bool = False) -> List[List]:
        """Generate batches from data"""
        working_data = self.data.copy()
        if self.shuffle:
            random.shuffle(working_data)

        batches = []
        for i in range(0, len(working_data), self.batch_size):
            batch = working_data[i:i + self.batch_size]
            # Handle drop_last
            if drop_last and len(batch) < self.batch_size:
                continue
            batches.append(batch)

        return batches

    def get_batch_indices(self, drop_last: bool = False) -> List[List[int]]:
        """Return indices of batches instead of actual data"""
        indices = list(range(len(self.data)))
        if self.shuffle:
            random.shuffle(indices)

        batches_indices = []
        for i in range(0, len(indices), self.batch_size):
            batch = indices[i:i + self.batch_size]
            if drop_last and len(batch) < self.batch_size:
                continue
            batches_indices.append(batch)

        return batches_indices

    def get_batch_statistics(self) -> dict:
        """Calculate batch statistics"""
        num_batches = (len(self.data) + self.batch_size - 1) // self.batch_size
        last_batch_size = len(self.data) % self.batch_size or self.batch_size

        return {
            "total_samples": len(self.data),
            "batch_size": self.batch_size,
            "num_batches": num_batches,
            "last_batch_size": last_batch_size
        }

    def get_stratified_batches(self, labels: List[str]) -> List[List]:
        """Generate batches ensuring balanced class labels (Stratified Batching)"""
        # Group data indices by label
        label_to_indices = defaultdict(list)
        for idx, label in enumerate(labels):
            label_to_indices[label].append(self.data[idx])

        # Shuffle each class group if required
        if self.shuffle:
            for label in label_to_indices:
                random.shuffle(label_to_indices[label])

        # Distribute items into batches round-robin or proportionally
        batches = []
        unique_labels = list(label_to_indices.keys())
        
        # Simple proportional draw: draw evenly from each class
        while any(len(label_to_indices[lbl]) > 0 for lbl in unique_labels):
            batch = []
            while len(batch) < self.batch_size:
                added = False
                for label in unique_labels:
                    if len(label_to_indices[label]) > 0 and len(batch) < self.batch_size:
                        batch.append(label_to_indices[label].pop(0))
                        added = True
                if not added:
                    break  # All exhausted
            if batch:
                batches.append(batch)
        return batches

    def get_padded_batches(self, pad_val: int = 0) -> List[List]:
        """Generate batches and pad the last one if incomplete"""
        batches = self.get_batches(drop_last=False)
        if not batches:
            return batches
            
        last_batch = batches[-1]
        if len(last_batch) < self.batch_size:
            padding_needed = self.batch_size - len(last_batch)
            last_batch.extend([pad_val] * padding_needed)
            
        return batches

    def circular_batch_generator(self):
        """Infinite generator yielding batches continuously (circular)"""
        working_data = self.data.copy()
        index = 0
        while True:
            if index == 0 and self.shuffle:
                random.shuffle(working_data)
                
            batch = []
            for _ in range(self.batch_size):
                batch.append(working_data[index])
                index = (index + 1) % len(working_data)
                
            yield batch

# Example usage
sample_ids = list(range(1, 101))  # 100 samples

processor = DataBatchProcessor(sample_ids, batch_size=16, shuffle=False)
batches = processor.get_batches()

print(f"Generated {len(batches)} batches")
print(f"First batch: {batches[0]}")
print(f"Last batch size: {len(batches[-1])}")

stats = processor.get_batch_statistics()
print(f"Statistics: {stats}")

# Testing extensions
print("\n--- Testing Extensions ---")

# 1. Drop last incomplete batch
batches_drop = processor.get_batches(drop_last=True)
print(f"With drop_last=True, num batches: {len(batches_drop)}")

# 2. Batch indices
batch_indices = processor.get_batch_indices()
print(f"First batch indices: {batch_indices[0]}")

# 3. Padded batch
processor_padded = DataBatchProcessor(list(range(1, 10)), batch_size=4, shuffle=False)
print(f"Padded batches: {processor_padded.get_padded_batches(pad_val=-1)}")

# 4. Stratified batching
labels = ["cat", "dog"] * 50  # 100 labels, alternating
strat_processor = DataBatchProcessor(list(range(1, 101)), batch_size=6, shuffle=False)
strat_batches = strat_processor.get_stratified_batches(labels)
print(f"Stratified batch 1 (balanced draw): {strat_batches[0]}")

# 5. Circular generator test
gen = processor.circular_batch_generator()
print(f"Gen Batch 1: {next(gen)}")
print(f"Gen Batch 2: {next(gen)}")
print(f"Gen Batch 3: {next(gen)}")
