
# Set the environment variable for the Apptainer image path
export APPTAINER_IMAGE_PATH=/sdf/group/facet/sanjeev/containers/impact-bmad_latest.sif
export NOTEBOOK_ROOT=$HOME/impact_bmad_container_notebooks
mkdir -p $HOME/impact_bmad_container_notebooks

# Define the jupyter function to use Apptainer for executing Jupyter with necessary bindings and running mkdir and cp commands
function jupyter() {
apptainer exec -B /usr,/sdf,/fs,/sdf/scratch,/lscratch ${APPTAINER_IMAGE_PATH} bash -c "
        mkdir -p ${NOTEBOOK_ROOT} &&
        cp -rn /opt/notebooks/* ${NOTEBOOK_ROOT}/";
  	apptainer exec -B /usr,/sdf,/fs,/sdf/scratch,/lscratch ${APPTAINER_IMAGE_PATH}  jupyter $@;
}
