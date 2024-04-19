Learning AWS Boto3 - AWS SDK for Python

Installation

```
$ conda create -n aws-boto3 -c conda-forge boto3
```

Jupyter Lab

```
$ conda create -n jupyterlab -c conda-forge jupyterlab

$ conda activate jupyterlab

$ mkdir -p $HOME/jupyterlab/notebooks

$ jupyter lab --notebook-dir $HOME/jupyterlab --preferred-dir $HOME/jupyterlab/notebooks
```

Configuration

```
$ aws configure

$ aws configure --profile boto3
```

API Calls

* Client (Low level API)
* Resources (High level API)
* Paginators
* Waiters