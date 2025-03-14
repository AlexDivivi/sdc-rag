# SDC - Hands on GenAI - RAG

## Setup

### Local DEV Setup

`Install conda`. conda is a programm to manage environments on your local machine. After that: 

```sh
cd ${env}
conda env create --file environment.yml
source activate ${env}
```

Copy the `.env-form` file and rename it to `.env`. Fill the environment secrets in the new file. The `.env` file will be ignored by git.

### Updating requirements

Requirements are held in the `requirements.txt` file and can be updated by simply updating the local environment and freezing the requirements.

```sh
cd ${env}
conda env update --file environment.yml
source activate ${env}
pip freeze > requirements.txt
```

The `requirements.txt` file is used by the docker build process to setup the corresponding container environment.

## Start

```sh
docker compose up
```