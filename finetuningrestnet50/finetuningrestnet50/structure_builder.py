import os

# Define the full structure
structure = {
    "image_classifier": [
        "main.py",
        "config.py",
        "data_loader.py",
        "train.py",
        "evaluate.py",
        "utils.py",
        "requirements.txt",
        "app.py",
        "saved_model/",
        "dataset/train/class1/",
        "dataset/train/class2/",
        "dataset/val/class1/",
        "dataset/val/class2/"
    ]
}

def create_structure(structure):
    for folder, items in structure.items():
        os.makedirs(folder, exist_ok=True)
        for item in items:
            path = os.path.join(folder, item)
            if item.endswith("/"):
                os.makedirs(path, exist_ok=True)
            else:
                # Create a Python file with a basic placeholder
                with open(path, "w") as f:
                    f.write(f"# {item} - auto-generated\n")

if __name__ == "__main__":
    create_structure(structure)
    print("✅ Full image classification project structure created.")
