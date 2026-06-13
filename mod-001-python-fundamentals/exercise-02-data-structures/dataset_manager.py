# dataset_manager.py

from typing import Dict, List, Set, Tuple
from collections import defaultdict
import random

class MLDatasetManager:
    """Comprehensive dataset manager using all data structures"""

    def __init__(self):
        # Dictionary: sample_id -> sample data
        self.samples: Dict[int, Dict] = {}

        # Sets: track dataset splits
        self.train_ids: Set[int] = set()
        self.val_ids: Set[int] = set()
        self.test_ids: Set[int] = set()

        # List: maintain order for class labels
        self.class_names: List[str] = []

        # Dictionary: class -> list of sample IDs
        self.class_to_samples: Dict[str, List[int]] = defaultdict(list)

    def add_sample(self, sample_id: int, filepath: str,
                   class_label: str, metadata: Dict = None):
        """Add a sample to the dataset"""
        if sample_id in self.samples:
            raise ValueError(f"Sample {sample_id} already exists")

        self.samples[sample_id] = {
            'filepath': filepath,
            'class': class_label,
            'metadata': metadata or {}
        }

        # Update class tracking
        if class_label not in self.class_names:
            self.class_names.append(class_label)

        self.class_to_samples[class_label].append(sample_id)

    def split_dataset(self, train_ratio: float = 0.7,
                     val_ratio: float = 0.15, seed: int = 42):
        """Split dataset into train/val/test"""
        random.seed(seed)

        all_ids = list(self.samples.keys())
        random.shuffle(all_ids)

        n = len(all_ids)
        train_end = int(n * train_ratio)
        val_end = train_end + int(n * val_ratio)

        self.train_ids = set(all_ids[:train_end])
        self.val_ids = set(all_ids[train_end:val_end])
        self.test_ids = set(all_ids[val_end:])

    def validate_splits(self) -> Tuple[bool, List[str]]:
        """Validate dataset splits have no overlap"""
        issues = []

        # Check overlaps
        train_val = self.train_ids & self.val_ids
        if train_val:
            issues.append(f"Train-Val overlap: {len(train_val)} samples")

        train_test = self.train_ids & self.test_ids
        if train_test:
            issues.append(f"Train-Test overlap: {len(train_test)} samples")

        val_test = self.val_ids & self.test_ids
        if val_test:
            issues.append(f"Val-Test overlap: {len(val_test)} samples")

        # Check all samples assigned
        all_split_ids = self.train_ids | self.val_ids | self.test_ids
        if len(all_split_ids) != len(self.samples):
            issues.append("Not all samples assigned to splits")

        return len(issues) == 0, issues

    def get_class_distribution(self, split: str = 'train') -> Dict[str, int]:
        """Get class distribution for a split"""
        if split == 'train':
            split_ids = self.train_ids
        elif split == 'val':
            split_ids = self.val_ids
        elif split == 'test':
            split_ids = self.test_ids
        else:
            raise ValueError("Split must be 'train', 'val', or 'test'")

        distribution = {}
        for class_name in self.class_names:
            class_samples = set(self.class_to_samples[class_name])
            count = len(class_samples & split_ids)
            distribution[class_name] = count

        return distribution

    def get_summary(self) -> Dict:
        """Get dataset summary statistics"""
        return {
            'total_samples': len(self.samples),
            'num_classes': len(self.class_names),
            'classes': self.class_names,
            'train_samples': len(self.train_ids),
            'val_samples': len(self.val_ids),
            'test_samples': len(self.test_ids),
            'class_distribution': {
                cls: len(samples)
                for cls, samples in self.class_to_samples.items()
            }
        }

# Example usage
manager = MLDatasetManager()

# Add samples
samples_data = [
    (1, "/data/cat_001.jpg", "cat"),
    (2, "/data/dog_001.jpg", "dog"),
    (3, "/data/cat_002.jpg", "cat"),
    (4, "/data/bird_001.jpg", "bird"),
    (5, "/data/dog_002.jpg", "dog"),
    (6, "/data/cat_003.jpg", "cat"),
    (7, "/data/bird_002.jpg", "bird"),
    (8, "/data/dog_003.jpg", "dog"),
    (9, "/data/cat_004.jpg", "cat"),
    (10, "/data/bird_003.jpg", "bird"),
]

for sample_id, filepath, class_label in samples_data:
    manager.add_sample(sample_id, filepath, class_label)

# Split dataset
manager.split_dataset(train_ratio=0.6, val_ratio=0.2, seed=42)

# Validate
is_valid, issues = manager.validate_splits()
print(f"Splits valid: {is_valid}")
if issues:
    for issue in issues:
        print(f"  - {issue}")

# Get summary
summary = manager.get_summary()
print(f"\nDataset Summary:")
for key, value in summary.items():
    print(f"  {key}: {value}")

# Check distributions
print("\nClass Distribution per Split:")
for split in ['train', 'val', 'test']:
    dist = manager.get_class_distribution(split)
    print(f"  {split}: {dist}")
