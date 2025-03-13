# Topics:
## Project Set-up:
1. Create a conda.yaml file using the command:
```conda env export > conda.yaml```

    Example: 
    ```
    name: mlflow project demo
    channels:
        - defaults
    dependencies:
        - python=3.12.3
        - pip
        - pip:
            - mlflow==1.23.1
    ```
2. To run the project, use this code in the terminal:
    - ```mlflow run .``` or
    - ```mlflow run . --no-conda``` or
    - ```mlflow run github_repo_link``` or
    - ```mlflow run github_repo_link -P param1=3 --no-conda```.