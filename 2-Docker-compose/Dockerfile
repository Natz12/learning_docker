# FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime
ARG MINICONDA_VERSION=latest
FROM continuumio/miniconda3:$MINICONDA_VERSION

RUN apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y 

RUN apt-get install wget -y

RUN  conda update conda \
    && conda clean --all --yes

USER $USER

WORKDIR /maindir

# Copy conda env
COPY env.yml .

# Create environment
RUN conda env create -f env.yml

# Make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile

# Make non-activate conda commands available
ENV PATH=$CONDA_DIR/envs/test_env/bin:$PATH

# Copy Python scripts
COPY example_time.py .
COPY example_time2.py .


# Create container entry point (Where it will start every time we run teh container)
# ENTRYPOINT /bin/bash --login -c "conda activate test_env && python3 example_time.py"

# Another option is to use conda run but its use is discourage as it is still in development.
# ENTRYPOINT [ "conda", "run", "--no-capture-output", "-n", "test_env", "python3", "example_time.py"]


