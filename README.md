<div align="center"> 
	<img alt="Food trucks' application" src="./frontend/public/assets/banner1.png" />
</div>
<div align="center">    
    <h1 > Food trucks' application </h1>
</div>

<p align="center">
 <a href="#-About-this-project">About this project</a> •
 <a href="#-Technologies">Technologies</a> •
 <a href="#-Useful-CLI-commands">CLI commands</a> •
 <a href="#-Documentation">Documentation</a> •
 <a href="#-How-to-run-this-project">How to run</a> •
 <a href="#-Author">Author</a> • 
</p>

<div align="center">    
    <img alt="Food trucks' application" src="./frontend/public/assets/banner2.png" />
</div>

# Content

## 💻 About this project

🚀 This project has implemented both backend and frontend. The implemented logic relies mainly over two models, Locations and Applicants or Trucks models.
Each location can have several trucks. Therefore, at the frontend, an interface to filter trucks by locations is implemented.

## 🛠 Technologies

### 🧭 Backend: 
The backend is implemented using Rest Django. Therefore, it is written in Python.
In the Figure below, you can see the Swagger documentation. Note that from the point of view of backend, the trucks are considered as applicants.

![Swagger](./frontend/public/assets/documentation/backend1.png)

### 🎨 Frontend:
The frontend is implemented using React and Typescript.
One of the amazing results that you can find with this application is shown in the Figure below.
![Main](./frontend/public/assets/documentation/frontend1.png)

In addition, if one day you get lost in my application, Bonnie always will help you to go back on the right track.

![NotFound](./frontend/public/assets/documentation/frontend2.png)

## ⚙️ Useful CLI commands

```bash
python manage.py fake_location <size_batch>
```

where the parameter `size_batch` represents the number of random locations that will be inserted into the database.

```bash
python manage.py fake_trucks <size_batch>
```

this parameter works similarly to the previous command. However, the user must consider a size_batch value at least 10 times the size_batch of the Location model. Thus, the probability of each location having several trucks is higher.


```bash
python manage.py fake_populate <size_batch>
```

this command populates the Locations and Applicants models by considering a size_batch relation of 1 to 10.

## 📝 Documentation

The backend has CRUD endpoints for each model. Futhermore, an amazing service to upload data from a CSV file is implemented. For more details, please go to Swagger documentation in the following link:

```
http://localhost:5050/api/docs/
```

## How to run this app 


## 🦸 Author

<a href="https://www.linkedin.com/in/alvaro-javier-ortega-951241174/">
 <img style="border-radius: 50%;" src="https://shorturl.at/moLO9" width="100px;" alt="M."/>
 <br />
 <sub><b>Alvaro Ortega</b></sub></a> <a href="https://www.linkedin.com/in/alvaro-javier-ortega-951241174/" >🚀</a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-AlvaroOrtega-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ne%C3%ADlton-seguins-bb8786a6/)](https://www.linkedin.com/in/alvaro-javier-ortega-951241174//)
[![Gmail Badge](https://img.shields.io/badge/-alvarojavierortega.com@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:alvarojavierortega.com@gmail.com)](alvarojavierortega.com@gmail.com)


