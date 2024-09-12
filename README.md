# Python Devcontainer

[![YouTube Explainer](https://img.youtube.com/vi/rVHTSrQdX_g/0.jpg)](https://www.youtube.com/watch?v=rVHTSrQdX_g)

This project contains the following features:

* [Dev Container](https://containers.dev/)
  * [Base Image](https://github.com/devcontainers/images/tree/main/src/python)
  * [VS Code Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
* [Node.js](https://nodejs.org/en) and [Express](https://expressjs.com/) backend
* [Vue 3](https://vuejs.org/) frontend
* [MySQL](https://hub.docker.com/_/mysql) and [phpMyAdmin](https://hub.docker.com/_/phpmyadmin) service containers

## Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [VS Code](https://code.visualstudio.com/)
  * [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  * [Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

## Step 1 - Define the Dev Container

1. Create a new project folder and open it in VS Code
2. Use the command palette to add dev container files to the project ([Documentation](https://code.visualstudio.com/docs/devcontainers/create-dev-container))

## Step 2 - Load the Dev Container

1. In VS Code, use the command palette to reopen the folder in a dev container. The first time this action is performed, it may take several minutes to download base images and build the container. This will be much faster in the future.

## Step 3 - Create the Python project and Unit Tests

See the video and repository for a sample project.

## Step 4 - Commit to GitHub

Commit this code to a GitHub repository. From there, a GitHub Codespace can be built for developing in the cloud, and it can also be used as a basis for a repository in GitHub Codespaces. 