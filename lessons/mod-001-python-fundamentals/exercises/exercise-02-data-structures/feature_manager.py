# feature_manager.py

from typing import Dict, List, Any
import json

class FeatureManager:
    """Manage ML features and their metadata"""

    def __init__(self):
        self.features: Dict[str, Dict[str, Any]] = {}
        # Version tracking: name -> list of metadata snapshots
        self.versions: Dict[str, List[Dict[str, Any]]] = {}
        # Correlation matrix: (feat_a, feat_b) -> float correlation
        self.correlations: Dict[tuple, float] = {}

    def add_feature(self, name: str, dtype: str,
                   importance: float = 0.0, description: str = "",
                   validation_rules: dict = None):
        """Add a feature with metadata and validation rules"""
        metadata = {
            "dtype": dtype,
            "importance": importance,
            "description": description,
            "used_count": 0,
            "version": 1,
            "validation_rules": validation_rules or {}
        }
        self.features[name] = metadata
        self.versions[name] = [metadata.copy()]

    def get_feature(self, name: str) -> Dict[str, Any]:
        """Get feature metadata"""
        return self.features.get(name, {})

    def update_importance(self, name: str, importance: float):
        """Update feature importance and increment version"""
        if name in self.features:
            self.features[name]["importance"] = importance
            self.features[name]["version"] += 1
            # Add to history
            self.versions[name].append(self.features[name].copy())

    def increment_usage(self, name: str):
        """Track feature usage"""
        if name in self.features:
            self.features[name]["used_count"] += 1

    def get_top_features(self, n: int = 5) -> List[tuple]:
        """Get top N features by importance"""
        sorted_features = sorted(
            self.features.items(),
            key=lambda x: x[1]["importance"],
            reverse=True
        )
        return sorted_features[:n]

    def filter_by_dtype(self, dtype: str) -> Dict[str, Dict]:
        """Get all features of specific data type"""
        return {
            name: meta for name, meta in self.features.items()
            if meta["dtype"] == dtype
        }

    def validate_feature_value(self, name: str, value: Any) -> bool:
        """Validate a value against feature rules"""
        if name not in self.features:
            return False
        rules = self.features[name].get("validation_rules", {})
        
        # Check type
        dtype = self.features[name]["dtype"]
        if dtype == "int" and not isinstance(value, int):
            return False
        if dtype == "float" and not isinstance(value, (int, float)):
            return False
        if dtype == "str" and not isinstance(value, str):
            return False
        if dtype == "bool" and not isinstance(value, bool):
            return False
            
        # Check rules
        if "min" in rules and value < rules["min"]:
            return False
        if "max" in rules and value > rules["max"]:
            return False
        if "allowed" in rules and value not in rules["allowed"]:
            return False
            
        return True

    def set_correlation(self, feat_a: str, feat_b: str, val: float):
        """Set correlation between two features"""
        key = tuple(sorted([feat_a, feat_b]))
        self.correlations[key] = val

    def get_highly_correlated_pairs(self, threshold: float = 0.8) -> List[tuple]:
        """Find highly correlated feature pairs"""
        return [pair for pair, val in self.correlations.items() if abs(val) >= threshold]

    def export_config(self, filepath: str):
        """Export features to JSON"""
        with open(filepath, 'w') as f:
            json.dump(self.features, f, indent=2)

    def import_config(self, filepath: str):
        """Import features from JSON"""
        with open(filepath, 'r') as f:
            self.features = json.load(f)

# Example usage
manager = FeatureManager()

# Add features
manager.add_feature("age", "int", 0.85, "User age in years", {"min": 0, "max": 120})
manager.add_feature("income", "float", 0.92, "Annual income", {"min": 0.0})
manager.add_feature("location", "str", 0.65, "City name", {"allowed": ["NYC", "SF", "LA"]})
manager.add_feature("clicks", "int", 0.78, "Number of clicks")

# Update importance (creates version 2)
manager.update_importance("age", 0.88)
print(f"Age version: {manager.get_feature('age')['version']}")
print(f"Age version history: {len(manager.versions['age'])}")

# Validation
print(f"Valid age 25: {manager.validate_feature_value('age', 25)}")
print(f"Valid age 150: {manager.validate_feature_value('age', 150)}")
print(f"Valid location NYC: {manager.validate_feature_value('location', 'NYC')}")
print(f"Valid location Chicago: {manager.validate_feature_value('location', 'Chicago')}")

# Correlation
manager.set_correlation("income", "clicks", 0.85)
manager.set_correlation("age", "clicks", 0.30)
print(f"Highly correlated pairs (>0.8): {manager.get_highly_correlated_pairs(0.8)}")
