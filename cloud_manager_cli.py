import argparse
from modules.aws_manager import list_instances, manage_instance
from modules.docker_manager import deploy_docker
from modules.inventory_gen import generate_inventory

def main():
    parser = argparse.ArgumentParser(description="Cloud Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")

    manage_parser = subparsers.add_parser("ec2")
    manage_parser.add_argument("action", choices=["start", "stop"])
    manage_parser.add_argument("--tag-key")
    manage_parser.add_argument("--tag-value")

    docker_parser = subparsers.add_parser("docker")
    docker_parser.add_argument("--name", required=True)
    docker_parser.add_argument("--image", required=True)

    inv_parser = subparsers.add_parser("inventory")
    inv_parser.add_argument("--hosts", nargs="+", required=True)
    inv_parser.add_argument("--path", default="inventory.yaml")

    args = parser.parse_args()

    if args.command == "list":
        list_instances()
    elif args.command == "ec2":
        manage_instance(args.action, args.tag_key, args.tag_value)
    elif args.command == "docker":
        deploy_docker(args.name, args.image)
    elif args.command == "inventory":
        generate_inventory(args.hosts, args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
# cloud_manager_cli.py
# This script serves as the command-line interface for managing cloud resources.