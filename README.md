# ETL ~ Workshop-1 ~ Python Data Engineer Workshop <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="Nombre de la Imagen" width="30px"/>

Presented by Samuel Escalante Gutierrez - [@SamuelEscalante](https://github.com/SamuelEscalante)

# Welcome

This project involves receiving a CSV file with data from candidates who participated in selection processes (this data was generated randomly). The main objective was to perform analysis and manipulations on this data to obtain relevant information and finally make a data visualizations.

### Tools used

- **Python** <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px">
- **Jupyter Notebooks** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- **PostgreSQL** <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- **Power BI** <img src="https://1000logos.net/wp-content/uploads/2022/08/Microsoft-Power-BI-Logo.png" alt="PowerBI" width="30px" height="21px">
- **SQLAlchemy** <img src="https://quintagroup.com/cms/python/images/sqlalchemy-logo.png/@@images/eca35254-a2db-47a8-850b-2678f7f8bc09.png" alt="SQLalchemy" width="50px" height="21px">

### About the data

This dataset have 50k rows of data about candidates. The columns names and their respective datatype before data transformation are:

- First Name : Object

- Last Name : Object

- Email : Object

- Country : Object

- Application Date : Object

- Yoe (Years Of Experience) : Integer 

- Seniority : Object

- Technology : Object

- Code Challenge Score : Integer

- Technical Interview : Integer

### Repository Organizacion

- **data:** This folder contains all the csv files 'Canidadates.csv', 'SuccessfulApplicants.csv' and 'countries-contienent.csv'
- **db_operations:** This folder is the first one you should run in the first instance, it is generally responsible for putting the raw data into the 'Candidates' table.
- **notebooks:** This folder contains the exploratory data analysis and contains the notebook responsible for uploading the transformed data to the 'SuccessfulAplicants' table.
- **src:** This folder contains the code responsible for connecting to our database, as well as the models of the tables that we already mentioned.

##Requirements
1. Install Python : [Python Downloads](https://www.python.org/downloads/)
2. Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)
3. Install Power BI : [Install Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494) 

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
(add the file to the root of the project)

`PGDIALECT` <- This variable specifies the dialect of PostgreSQL to be used in the connection.  
`PGUSER` <- Defines the username to be used for authenticating against the PostgreSQL database.  
`PGPASSWD` <- This variable stores the password associated with the PostgreSQL user for authentication.  
`PGHOST` <- Indicates the address of the PostgreSQL database server that the application will connect to.  
`PGPORT` <-  Specifies the port on which the PostgreSQL database server is listening.  
`PGDB` <- Defines the name of the database that the application will connect to.  
`WORK_DIR` <- Sets the working directory for the application, indicating the base path for performing operations and managing files.

## Run this project

1. Clone the project
```bash
  git clone https://github.com/SamuelEscalante/Workshop-01-ETL.git
```

2. Go to the project directory
```bash
  cd Workshop-1-ETL
```

3. Create virtual environment for Python
```bash
  python -m venv venv
```

4. Install libreries
```bash
  pip install -r requirements.txt
```

5. Create a database in PostgreSQL

6. Explore the project, you shoul start by folder **db_operations** :
   - _database_setup:_  this notebook focused on database connection, table creation, and data insertion
   - _transform_data:_ provides methods for processing and transforming data from a CSV file.
  
7. Continue executing folder **notebooks** :
   - _eda_: In this notebook, we will dive into a comprehensive exploration of the dataset
   - _data_processing_: This Notebook demonstrates the data processing workflow using the `TransformData` class from the `transform_data.py` module and load final data into 'SuccessfulApplicants' table.
  
8. Go to Power Bi :  
8.1 Open a new dashboard
![image](https://github.com/SamuelEscalante/Workshop-01-ETL/assets/111151068/56e0c10a-4819-4e1e-ad28-d47ad4381ec2)

8.2 Look for 'Database PostgreSQL' :  
![image](https://github.com/SamuelEscalante/Workshop-01-ETL/assets/111151068/581e84ff-0cb4-4240-a998-217c8b9607c4)

8.3 Insert your information and accept :  
![image](https://github.com/SamuelEscalante/Workshop-01-ETL/assets/111151068/da2e0d78-ecdc-4068-a97b-c470911c4a18)
  
8.4 Select the tables and load the data :  
![image](https://github.com/SamuelEscalante/Workshop-01-ETL/assets/111151068/da5f7f55-ec3f-40d7-b51e-85b5a7a9c7b6)


The data is now synchronized with power bi! You can do your own dashboard.  
See my dashboard [here](Dashboard-Workshop-01.pdf) 

## Farewell and Thanks

Thank you for visiting our repository! We hope you find this project useful. If it has been helpful or you simply liked it, consider giving the repository a star! 🌟

We would love to hear your feedback, suggestions, or contributions.

Thanks for your support! 👋

