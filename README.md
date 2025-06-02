# Infra Automation & Cost Optimization Tool
## Overview
This project provides an automated infrastructure deployment and cost optimization solution for cloud resources. It helps automate provisioning, monitor resource usage, and generate cost reports to optimize spending.
## Features
- Infrastructure as Code (IaC) based deployments using Terraform
- Automated cost reporting and analysis
- Integration with cloud provider APIs to track resource utilization
- Alerting for cost overruns and optimization opportunities
- Scalable and modular design for easy extension
## Folder Structure
```
infra-automation-cost-tool/
├── infra/                  # Terraform configuration files for infrastructure deployment
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── cost-reporter/          # Scripts and modules for cost tracking and reporting
│   ├── cost_report.py
│   ├── requirements.txt
│   └── utils.py
├── azure-pipelines/        # Azure DevOps pipeline YAML files
│   └── ci.yml
├── README.md               # This documentation file
```
## Prerequisites
- Terraform >= 1.0
- Python 3.x with required packages (see `cost-reporter/requirements.txt`)
- Azure CLI configured with appropriate permissions
- Access to billing APIs for cost data
## Usage
### Deploy Infrastructure
```bash
cd infra
terraform init
terraform apply
```
### Generate Cost Report
```bash
cd cost-reporter
pip install -r requirements.txt
python cost_report.py
```
### CI/CD Pipeline
The Azure DevOps pipeline defined in `azure-pipelines/ci.yml` automates infrastructure deployment and cost report generation.

terraform apply

