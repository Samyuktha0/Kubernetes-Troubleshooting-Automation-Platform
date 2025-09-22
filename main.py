from scripts.pod_checker import check_failed_pods
from scripts.node_taint_resolver import resolve_node_taints
from scripts.image_pull_debugger import debug_image_pull_errors

def main():
    print("Running Kubernetes Troubleshooter...")
    check_failed_pods()
    resolve_node_taints()
    debug_image_pull_errors()

if __name__ == "__main__":
    main()
