# Infrastructure Automation & Cost Optimization Tool

## Overview

This project automates provisioning Azure infrastructure and fetches cost data using Python and Terraform.

## Setup

### 1. Provision infrastructure with Terraform:

\\\ash
cd infra
terraform init
terraform apply
\\\

### 2. Run cost reporting script:

- Set environment variable:

\\\ash
export AZURE_SUBSCRIPTION_ID=\"your-subscription-id\"
\\\

- Install dependencies & run:

\\\ash
cd cost-reporter
pip install -r requirements.txt
python cost_report.py
\\\

## Azure DevOps Pipeline

This repo includes a pipeline YAML to automate running the cost reporting script on push to \main\.
