---
layout: post
title: "[typescript] Azure Kubernetes Service를 사용하여 컨테이너 기반 애플리케이션을 배포하는 방법은 무엇인가요?"
description: " "
date: 2023-12-15
tags: [typescript]
comments: true
share: true
---

# Deploying Containerized Application with Azure Kubernetes Service (AKS)

Azure Kubernetes Service (AKS) allows you to deploy, manage, and scale containerized applications using Kubernetes. Follow these steps to deploy a containerized application to AKS.

## Prerequisites

Before you begin, make sure you have the following:

1. An Azure account with the necessary permissions to create an AKS cluster.
2. Azure CLI installed on your local machine.
3. Docker installed on your local machine to build and push the container image.

## Step 1: Create an AKS Cluster

Use Azure CLI to create an AKS cluster. Replace `<resource-group>` and `<cluster-name>` with your preferred values.

```bash
az group create --name <resource-group> --location <location>
az aks create --resource-group <resource-group> --name <cluster-name> --node-count 2 --enable-addons monitoring --generate-ssh-keys
```

## Step 2: Connect to the AKS Cluster

Once the cluster is created, run the following command to configure `kubectl` to connect to the AKS cluster.

```bash
az aks get-credentials --resource-group <resource-group> --name <cluster-name>
```

## Step 3: Build and Push the Container Image

Navigate to your application's directory and build the Docker image.

```bash
docker build -t <image-name> .
```

Then, push the image to Azure Container Registry (ACR).

## Step 4: Deploy the Application to AKS

Create a Kubernetes deployment and a service to expose the application.

```bash
kubectl create deployment <deployment-name> --image=<image-name>
kubectl expose deployment <deployment-name> --type=LoadBalancer --port=80
```

## Step 5: Access the Application

Retrieve the public IP address of the Load Balancer to access the deployed application.

```bash
kubectl get service <deployment-name>
```

That's it! Your containerized application is now deployed and running on Azure Kubernetes Service.

## Conclusion

In this guide, we went through the process of deploying a containerized application to Azure Kubernetes Service using Azure CLI and Kubernetes commands. AKS provides a scalable and managed Kubernetes service, making it an ideal choice for running containerized workloads in the cloud.

For more advanced management and customization options, refer to the [official Azure Kubernetes Service documentation](https://docs.microsoft.com/en-us/azure/aks/).