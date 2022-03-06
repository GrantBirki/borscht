import json
from jinja2 import Template
import sys

REPO_DIR = sys.argv[1]

def http_template():
    with open(f"{REPO_DIR}/config/templates/http_template.json") as f:
        config = f.read()
    return config

def base_template():
    with open(f"{REPO_DIR}/config/templates/base.json") as f:
        base = json.loads(f.read())
    return base

def domains():
    with open(f"{REPO_DIR}/config/domains.txt") as f:
        domains = f.read().splitlines()
    return domains

def write_config(base, monitors):
    with open(f"{REPO_DIR}/config/config.json", "w") as f:
        base["monitorList"] = monitors
        f.write(json.dumps(base))

def generate_http_monitors(domains):
    monitors = []
    template = Template(http_template())
    
    for domain in domains:
        monitor = template.render(domain=domain)
        monitors.append(json.loads(monitor))
    return monitors

def main():

    all_monitors = []

    http_monitors = generate_http_monitors(domains())

    all_monitors += http_monitors
    write_config(base_template(), all_monitors)

if __name__ == "__main__":
    main()
