# TanX.fi Infrastucture Engineer Task

## Objectives

- Compute the total revenue generated by the online store for each month in the dataset.
- Compute the total revenue generated by each product in the dataset.
- Compute the total revenue generated by each customer in the
  dataset.
- Identify the top 10 customers by revenue generated.

### Folder structure

- Test Folder consists of Test File
- Task Folder consists of main file which is Tanx.py

### Instuction to run test and task folder

`Note: As no dataset was provided we generated our own using faker, so if you wish to change data to your own, just simply change the content of orders.csv, in respective folders`

#### Task File

- To Build image

```cmd
docker build -t python_task .
```

- To run the docker image that you created above

```cmd
docker run python_task
```

#### Test File

- To Build image

```cmd
docker build -t python_test .
```

- To run the docker image that you created above

```cmd
docker run python_test
```
