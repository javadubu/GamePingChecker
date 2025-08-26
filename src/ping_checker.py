import json
import subprocess
import platform
from datetime import datetime
import os

def ping(host, count=4):
    param = "-n" if platform.system().lower()=="windows" else "-c"
    command = ["ping", param, str(count), host]
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except Exception as e:
        return str(e)

def check_servers(server_file):
    with open(server_file, "r") as f:
        data = json.load(f)

    results = []
    print(f"\n🎮 Checking {data['name']} servers...\n")

    for server in data["servers"]:
        response = ping(server["ip"])
        results.append({
            "region": server["region"],
            "ip": server["ip"],
            "response": response
        })
        print(f"[{server['region']}] {server['ip']}\n{response}\n")

    return results

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    results = check_servers("servers/fifa.json")
    with open("results/logs.csv", "a") as log:
        for r in results:
            log.write(f"{datetime.now()},{r['region']},{r['ip']}\n")