# Kubernetes Troubleshooting Automation Platform

Automates detection and resolution of common Kubernetes issues including pod failures, image pull errors, and node taints. Integrates with Prometheus and Grafana for monitoring.

## Features
- Detect failed pods and image pull errors
- Resolve node taints automatically
- Prometheus alert integration
- Grafana dashboard for visualization
- RBAC-aware CLI interface

## Setup
```bash
pip install -r requirements.txt
python cli/main.py
