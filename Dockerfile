FROM ubuntu:20.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

WORKDIR $HOME

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get --allow-releaseinfo-change update && \ 
# need to remove the line about in the future, added to get around a bug from apt-get update
# https://stackoverflow.com/questions/68802802/repository-http-security-debian-org-debian-security-buster-updates-inrelease
    apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
		vim wget bzip2 ca-certificates libglib2.0-0 \
		libxext6 libsm6 libxrender1 libgl1 libglu1-mesa\
		curl libxerces-c-dev p7zip-full \
		llvm-6.0 llvm-6.0-tools freeglut3 freeglut3-dev \
		gcc g++ cmake make zlib1g-dev pkg-config libexpat-dev \ 
        awscli rsync git software-properties-common gcc-8 \
		python3.7 python3.7-dev python3.7-distutils

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7

# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

COPY setup.py build/setup.py
COPY requirements.txt build/requirements.txt
RUN cd build && pip install . && cd ../
COPY app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
