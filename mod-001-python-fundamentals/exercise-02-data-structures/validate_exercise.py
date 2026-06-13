# validate_exercise.py

def test_list_operations():
    """Test list comprehensions"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test filtering
    evens = [n for n in numbers if n % 2 == 0]
    assert evens == [2, 4, 6, 8, 10], "Even filter failed"

    # Test transformation
    squared = [n**2 for n in numbers]
    assert squared[0] == 1 and squared[-1] == 100, "Squaring failed"

    print("✓ List operations tests passed")

def test_dict_operations():
    """Test dictionary operations"""
    metrics = {"acc": 0.92, "loss": 0.15, "f1": 0.89}

    # Test filtering
    high_metrics = {k: v for k, v in metrics.items() if v > 0.20}
    assert "loss" not in high_metrics, "Dict filtering failed"

    # Test get with default
    lr = metrics.get("learning_rate", 0.001)
    assert lr == 0.001, "Dict get with default failed"

    print("✓ Dict operations tests passed")

def test_set_operations():
    """Test set operations"""
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # Test intersection
    overlap = set_a & set_b
    assert overlap == {4, 5}, "Set intersection failed"

    # Test union
    combined = set_a | set_b
    assert len(combined) == 8, "Set union failed"

    # Test difference
    only_a = set_a - set_b
    assert only_a == {1, 2, 3}, "Set difference failed"

    print("✓ Set operations tests passed")

def test_tuple_operations():
    """Test tuple immutability and usage"""
    config = ("model", "v1", 0.92)

    # Test unpacking
    name, version, acc = config
    assert name == "model", "Tuple unpacking failed"

    # Test immutability
    try:
        config[0] = "new_model"
        assert False, "Tuple should be immutable"
    except TypeError:
        pass  # Expected

    print("✓ Tuple operations tests passed")

if __name__ == "__main__":
    test_list_operations()
    test_dict_operations()
    test_set_operations()
    test_tuple_operations()
    print("\n✓ All validation tests passed!")
