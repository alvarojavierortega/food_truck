# Food trucks' application

This project has implemented both backend and frontend. The implemented logic relies mainly over two models, Locations and Applicants or Trucks models.
Each location can have several trucks. Therefore, at the frontend, an interface to filter trucks by locations is implemented.

## Technologies

### Backend: 
The backend is implemented in Rest Django. Therefore, it is written in Python.

### Frontend:
The frontend is implemented using React and Typescript.

## Useful CLI commands

```
python manage.py fake_location <size_batch>
```

where the parameter `size_batch` represents the number of random locations that will be inserted into the database.

```
python manage.py fake_trucks <size_batch>
```

this parameter works similarly to the previous command. However, the user must consider a size_batch value at least 10 times the size_batch of the Location model. Thus, the probability of each location having several trucks is higher.


```
python manage.py fake_populate <size_batch>
```

this command populates the Locations and Applicants models by considering a size_batch relation of 1 to 10.

## Documentation

The backend has CRUD endpoints for each model. For more details, please go to the following link:

```
http://localhost:5050/api/docs/
```

## How to run this app 

