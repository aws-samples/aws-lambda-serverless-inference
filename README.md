# Pay as you go machine learning inference with AWS Lambda - Example SAM applications

This repo contains AWS SAM templates that deploy serverless applications. The applications illustrate how to perform inference with breast cancer XGBoost ML model, and Python packages mounted from EFS.

For full details on how this works:
- Read the Compute Blog post at: TODO

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in these examples.

```bash
.
├── README.MD                                       <-- This instructions file
├── 01-setup                                        <-- Creates VPC, subnets and EFS file system
│   └── create-efs-acess-point-cfn.yml              <-- CloudFormation template to creates VPC, subnets and EFS file system
│   └── create-efs-acess-point-ec2-cfn.yml          <-- CloudFormation template to creates VPC, subnets, EFS file system and EC2
├── 02-train-code                                   <-- Python code used to train breast cancel XGBoost Model
│   └── requirements.txt                            <-- Python packages needed for the training and inference
│   └── bc_xgboost_train.py                         <-- Python file used to train breast cancel XGBoost Model
├── 03-lambda-template                              <-- XGBoost inference function example to use VPC and EFS
│   └── xgboost_inference_function                  <-- Python dependencies and scripts
│   └── template.yaml                               <-- SAM template
```

## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3.7.9 installed](https://www.python.org/downloads/release/python-379/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. Clone the repo onto your local development machine using `git clone`.

## Setup

To create a VPC, subnets and EFS file system, use the `create-efs-acess-point-cfn.yml` example in the `setup` directory. To deploy this template, run in a terminal:

```
aws cloudformation create-stack --stack-name create-efs-acess-point --template-body file://./create-efs-acess-point-cfn.yml
```
Note that the `template-body` parameter must include the `file://` prefix when run locally.

## Deploying examples

1. From the command line, change directory into the application example required, then run:
```
sam build
sam deploy --guided
```
Follow the prompts in the deploy process to set the stack name, EFS mount path, access point ARN, AWS Region, VPC and subnet IDs.

You can find VPC settings, list of subnet IDs, and list of access point ARNs for your account by executing the following CLI command:
```
aws cloudformation describe-stacks --stack-name create-efs-acess-point --query "Stacks[0].Outputs"
```

## How it works

* The deployed Lambda functions are configured with your VPC and subnet settings.
* The Lambda functions mount the EFS file system you specify. The operations in the examples use EFS to complete their tasks.

## Questions?

Please contact [@e_sela](https://twitter.com/e_sela) or raise an issue on this repo.

==============================================

Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0