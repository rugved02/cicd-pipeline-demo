# CI/CD Pipeline with GitHub Actions & Docker

## Project summary

A local, cloud-free CI/CD example that demonstrates how to automatically test code, build a Docker image, publish it to a Docker registry, and deploy the image to a local runtime (Minikube or a local VM). This repository contains the source code, CI workflows, and artifacts needed to reproduce and verify a working pipeline.

## Objective

- Show a repeatable CI/CD process using GitHub Actions and Docker.
- Validate code via automated tests in CI.
- Produce and publish a Docker image from CI.
- Deploy and verify the published image locally.

## Tools used

- GitHub Actions (CI/CD workflow engine)
- Docker & Docker Hub (container build and registry)
- Docker Compose and/or Minikube (local runtime for deployment)
- Any test framework appropriate for the application (unit/integration tests)

## Prerequisites

- GitHub account and access to the repository
- Docker Hub account (to view the pushed image)
- Docker installed locally to run images or Docker Compose
- Minikube or a local VM (only if you want to run the image in Kubernetes locally)
