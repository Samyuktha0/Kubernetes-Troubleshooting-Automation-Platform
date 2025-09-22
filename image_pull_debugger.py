from kubernetes import client, config

def debug_image_pull_errors():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        for container_status in pod.status.container_statuses or []:
            if container_status.state.waiting and "ImagePullBackOff" in container_status.state.waiting.reason:
                print(f"Image pull error in pod {pod.metadata.name}: {container_status.state.waiting.message}")
