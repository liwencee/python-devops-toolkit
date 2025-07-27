import subprocess
from modules.notifier import send_slack_alert

def deploy_docker(container_name, image):
    try:
        subprocess.run(["docker", "run", "-d", "--name", container_name, image], check=True)
        print(f"Container {container_name} deployed.")
    except subprocess.CalledProcessError:
        print(f"Failed to deploy container {container_name}.")
        send_slack_alert(f"Failed to deploy container {container_name}")
