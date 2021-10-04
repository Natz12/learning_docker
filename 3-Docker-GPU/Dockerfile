FROM nvidia/cuda:10.2-base
# CMD nvidia-smi
# FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime
# ARG MINICONDA_VERSION=latest
# FROM continuumio/miniconda3:$MINICONDA_VERSION

RUN apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y 
    #vim-tiny vim-athena build-essential

RUN apt-get install wget -y

USER $USER

# ---------- Minconda installation and config ----------

# Install miniconda
ENV MINICONDA_VERSION latest
ENV CONDA_DIR $HOME/miniconda3
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-$MINICONDA_VERSION-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# Make non-activate conda commands available
ENV PATH=$CONDA_DIR/bin:$PATH

# Make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
# Make conda activate command available from /bin/bash --interative shells
RUN conda init bash

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

# Start bash with conda env
RUN echo "conda activate test_env" >> ~/.bashrc
ENV PATH /opt/conda/envs/test_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $test_env

# Copy Python scripts
COPY example_time_gpu.py .
COPY example_time_gpu2.py .


# Create container entry point (Where it will start every time we run teh container)
# ENTRYPOINT /bin/bash --login -c "conda activate test_env && python3 example_time.py"

# Another option is to use conda run but its use is discourage as it is still in development.
# ENTRYPOINT [ "conda", "run", "--no-capture-output", "-n", "test_env", "python3", "example_time.py"]


