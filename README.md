
Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

Start Airflow on your local machine by running 'astro dev start'.

This command will spin up five Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- DAG Processor: The Airflow component responsible for parsing DAGs
- API Server: The Airflow component responsible for serving the Airflow UI and API
- Triggerer: The Airflow component responsible for triggering deferred tasks

When all five containers are ready the command will open the browser to the Airflow UI at http://localhost:8080/. You should also be able to access your Postgres Database at 'localhost:5432/postgres' with username 'postgres' and password 'postgres'.

Note: If you already have either of the above ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://www.astronomer.io/docs/astro/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.

Set up and Run an Airflow Project
=================================

- To set up a new Airflow project with the Astro CLI, make a new folder, and then use the command astro dev init to generate a new project.
- The Astro CLI will generate a project with a standard project directory. This includes:
    - The dags directory: Contains Python files corresponding to data pipelines, including examples such as example_dag_advanced and example_dag_basic.
    - The include directory: Used for storing files like SQL queries, bash scripts, or Python functions needed in data pipelines to keep them clean and organized.
    - The plugins directory: Allows for the customization of the Airflow instance by adding new operators or modifying the UI.
    - The tests directory: Contains files for running tests on data pipelines, utilizing tools like the pytest library.
    - The .dockerignore file: Describes files and folders to exclude from the Docker image during the build.
    - The .env file: Used for configuring Airflow instances via environment variables.
    - The .gitignore file: Specifies files and folders to ignore when pushing the project to a git repository, useful for excluding sensitive information like credentials.
    - The airflow_settings.yaml file: Stores configurations such as connections and variables to prevent loss when recreating the local development environment.
    - The Dockerfile: Used for building the Docker image to run Airflow, with specifications for the Astro runtime Docker image and the corresponding Airflow version.
    - The packages.txt file: Lists additional operating system packages to install in the Airflow environment.
    - The README file: Provides instructions and information about the project.
    - The requirements.txt file: Specifies additional Python packages to install, along with their versions, to extend the functionality of the Airflow environment.
- The Astro CLI can be used to run an Airflow project. To start an Airflow project with the Astro CLI, use the command astro dev start. To restart the project, use astro dev restart, and to stop the project, use the command astro dev stop.
- To get Airflow to work with VSCode and provide benefits like correct syntax highlighting and autocompletion, the VSCode instance must be run inside of the docker container using the Dev Containers extension.


DBT
========


Airflow Variables
key = insurance_claims_dag_settings
value = {
    "gcs_source_data_bucket":"[YOUR GCP PROJECT ID]-bucket", 
    "dev_bronze_dataset":"ic_dev_bronze",
    "dev_silver_dataset":"ic_dev_silver",
    "dev_gold_dataset":"ic_dev_gold"
}

data quality check
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT id) AS unique_id,
    SUM(CASE WHEN id IS NULL THEN 1 ELSE 0 END) AS null_ids
FROM table;    

astro dev start
astro dev restart
astro dev stop

Ensure data platform is connected (DBT)
dbt compile              | dbtf compile
dbt run                  | dbtf run
dbt clean                | dbtf clean
dbt run --full-refresh   | dbtf run --full-refresh  

dbtf test -s claims_payment
dbtf run-operation generate_model_yaml --args '{"model_names": ["claims_payment"]}'
dbtf run-operation generate_base_model --args '{"source_name": "ic_bronze", "table_name": "claims_reserves" }'

install.ps1: Run 'dbt --help' to get started
Usage: dbt.exe [OPTIONS] <COMMAND>

  init           Initialize a new dbt project
  deps           Install package dependencies
  parse          Parse models
  list           List selected nodes
  ls             List selected nodes (alias for list)
  compile        Compile models
  run            Run models
  run-operation  Run the named macro with any supplied arguments
  test           Test models
  seed           Seed models
  snapshot       Run snapshot models
  show           Show a preview of the selected nodes
  build          Build seeds, models and tests
  clean          Remove target directories
  source         Run sources subcommands
  clone          Create clones of selected nodes
  system         dbt installation configuration
  man            Create reference documentation
  debug          Profile connection debugging
  retry          Retry failed nodes from the previous run
  pull                  Pull and materialize input data from remote warehouse
  sl             Semantic Layer commands
  help           Print this message or the help of the given subcommand(s)

Use `dbt <COMMAND> --help` to learn more about the options for each command.                 