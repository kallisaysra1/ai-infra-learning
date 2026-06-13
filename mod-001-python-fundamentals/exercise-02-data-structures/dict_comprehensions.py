# dict_comprehensions.py

# Create metric dictionary from lists
metric_names = ["accuracy", "precision", "recall", "f1_score"]
metric_values = [0.92, 0.89, 0.94, 0.91]

metrics = {name: value for name, value in zip(metric_names, metric_values)}
print(f"Metrics: {metrics}")

# Filter metrics above threshold
high_metrics = {k: v for k, v in metrics.items() if v > 0.90}
print(f"High metrics (>0.90): {high_metrics}")

# Transform values
metrics_percentage = {k: f"{v*100:.1f}%" for k, v in metrics.items()}
print(f"Metrics as %: {metrics_percentage}")

# Nested dictionary: experiment results
experiments = {
    "exp_001": {
        "model": "resnet50",
        "accuracy": 0.92,
        "loss": 0.15,
        "epoch": 50,
        "status": "completed"
    },
    "exp_002": {
        "model": "vgg16",
        "accuracy": 0.88,
        "loss": 0.22,
        "epoch": 45,
        "status": "completed"
    },
    "exp_003": {
        "model": "mobilenet",
        "accuracy": 0.85,
        "loss": 0.28,
        "epoch": 30,
        "status": "failed"
    }
}

# Find best experiment by accuracy
completed_exps = {k: v for k, v in experiments.items()
                  if v["status"] == "completed"}
best_exp = max(completed_exps.items(), key=lambda x: x[1]["accuracy"])
print(f"Best experiment: {best_exp[0]} with accuracy {best_exp[1]['accuracy']}")

# Extract specific field from all experiments
accuracies = {exp_id: data["accuracy"]
              for exp_id, data in experiments.items()
              if data["status"] == "completed"}
print(f"All accuracies: {accuracies}")

# Group experiments by model
by_model = {}
for exp_id, data in experiments.items():
    model = data["model"]
    if model not in by_model:
        by_model[model] = []
    by_model[model].append(exp_id)

print(f"Experiments by model: {by_model}")

# Create summary statistics
summary = {
    "total_experiments": len(experiments),
    "completed": sum(1 for v in experiments.values() if v["status"] == "completed"),
    "failed": sum(1 for v in experiments.values() if v["status"] == "failed"),
    "avg_accuracy": sum(v["accuracy"] for v in experiments.values()
                       if v["status"] == "completed") / len(completed_exps)
}
print(f"Summary: {summary}")
