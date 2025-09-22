from kubernetes import client, config

def resolve_node_taints():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    for node in nodes.items:
        taints = node.spec.taints or []
        if taints:
            print(f"Node {node.metadata.name} has taints: {taints}")
            node.spec.taints = []
            v1.patch_node(node.metadata.name, node)
