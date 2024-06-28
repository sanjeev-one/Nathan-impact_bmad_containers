
# FACET2 Injector Simulation Docker Image

## Overview
This repository contains the necessary components to create a Docker image that encapsulates a Jupyter Notebook simulation environment for the FACET2 injector. Github actions automatically builds the container and updates the local copy on S3DF. The simulation utilizes both IMPACT and BMAD codes to model and analyze the injector's behavior. The juptyer notebooks are written by [Eric Cropp](https://github.com/ericcropp/Impact-T_Examples/blob/main/FACET-II_Impact_Bmad/Impact_Bmad.ipynb). Additionally, the repository includes a script to facilitate running the Docker container on the S3DF platform.

## Docker Image
The Docker image is designed to provide a ready-to-use simulation environment with pre-installed dependencies and configurations necessary for running IMPACT and BMAD simulations. The core of this environment is a Jupyter Notebook that guides users through the simulation process, from setting up initial conditions to visualizing the results.

### Components
- **Jupyter Notebook**: Contains the simulation workflow, including setup, execution, and analysis steps.
- **IMPACT**: A particle accelerator simulation tool used for the initial stages of the simulation.
- **BMAD**: A library for simulating charged particle beams and designing accelerators, used in the latter stages of the simulation.

## Running the Container on S3DF
Included in this repository is a script that simplifies the process of deploying and running the Docker container on the S3DF platform. This script handles copying the notebooks to a working directory on s3df and runs a local copy of the container on s3df.

### Usage
To run the Docker container on S3DF, execute the provided script with the necessary parameters. Instructions are on confluence ([here](https://confluence.slac.stanford.edu/x/HAGHGw))


## Forking repo to create custom container for S3DF:
### Step 1: Fork the Repository
1. Go to the repository on GitHub.
2. Click on "Use this template" in the top right corner.
3. Create your new repository from this template.

### Step 2: Edit the Dockerfile
1. In your new repository, navigate to the `Dockerfile`.
2. Locate the section where `conda` packages are installed:
    ```Dockerfile
    RUN /opt/conda/bin/conda install -y \
        jupyter \
        jupyterlab \
        scipy \
        numpy \
        matplotlib \
        pillow \
        pandas \
        conda-forge::xopt \
        conda-forge::distgen \
        h5py \
        pytao \
        conda-forge::openpmd-beamphysics && \
        /opt/conda/bin/conda clean -afy
    ```
3. Edit the list and similar parts to include or exclude packages as needed for your project.

### Step 3: Update Jupyter Notebooks
1. Navigate to the `./notebooks` directory.
2. Replace the existing notebooks with your own notebooks that are needed for your project.


### Step 5: Configure GitHub Actions Secrets
1. Go to the settings of your new GitHub repository.
2. Navigate to `Secrets` under the `Security` section.
3. Add the necessary secrets for your Docker container to be built and pushed to Docker Hub.
    - These secrets might include `DOCKER_HUB_ACCESS_TOKEN`, `DOCKER_HUB_USERNAME`, `SSH_PASSWORD` and any other necessary credentials (ssh username).

### Step 6: Adjust GitHub Actions Workflow
1. Ensure the path where the container is pulled to on S3DF (in the `pull_to_s3df.yml` GitHub Actions workflow) matches the path referenced in `ondemand.sh`.
2. Edit the `pull_to_s3df.yml` file as necessary to match your configuration.

### Step 7: Connect to S3DF and Start Jupyter Instance
1. Connect to the S3DF OnDemand portal.
2. Start a Jupyter instance using a custom Singularity (Apptainer) image.
3. Paste the `ondemand.sh` script into the box below the custom Apptainer image on the OnDemand portal.

# Support
For any issues or questions regarding the setup, execution, or other aspects of using this Docker image, please refer to the documentation provided [[here](https://confluence.slac.stanford.edu/x/HAGHGw)] or contact sanjeev@slac.stanford.edu.


