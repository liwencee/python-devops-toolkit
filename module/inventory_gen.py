import yaml

def generate_inventory(hosts, path="inventory.yaml"):
    data = {"all": {"hosts": hosts}}
    with open(path, "w") as f:
        yaml.dump(data, f)
    print(f"Inventory file saved to {path}")
