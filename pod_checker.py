from kubernetes import client, config

def check_failed_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        if pod.status.phase == "Failed":
            print(f"Failed pod: {pod.metadata.name} in {pod.metadata.namespace}")
