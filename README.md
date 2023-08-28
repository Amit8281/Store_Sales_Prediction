# STORE SALES PREDICTION

## How To Start
### Creat Environment
```
conda create -p venv python==3.9 -y
```
### Activate Environment
```
conda activate venv/
```
### Install Requirements 
```
pip install -r requirements.txt
```

## Problem Statement
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and common patterns can be discovered..

## Goal:-
Developing a comprehensive solution for leveraging data warehousing in shopping malls and Big Marts is essential. First, we must establish robust data pipelines to ingest and store individual item sales data in the data warehouse.This data repository should be designed for efficient retrieval and analysis, considering both consumer demographics and product attributes.

Next, employing advanced data mining and machine learning techniques, we can extract valuable insights from this data store. This includes identifying anomalies that might indicate theft or data entry errors and discovering common patterns that offer invaluable information for demand forecasting and inventory management.

## Dataset:-
```
https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data
```
## Project Various Steps:-
### Data Ingestion
The cornerstone of our data-driven project was established through a systematic process of data acquisition and ingestion. Utilizing Kaggle, a reputable platform renowned for its high-quality datasets, we identified and acquired the crucial data required for our price prediction project. This dataset, integral to our goal of accurate price forecasting, was meticulously downloaded and securely stored within our local system infrastructure. Subsequently, we initiated the data ingestion phase, where the dataset seamlessly integrated into our project's data pipeline. This meticulous approach ensures that our project is built upon a solid foundation, setting the stage for robust and precise price prediction models and analysis.

### Data transformation
Steps performed in pre-processing are:
- • First read data from Artifact folder
- • Checking unnecessary columns
- • One column has product id which is unique for every product so I deleted that column.
- • Checked for null values
- • there are too many null values are present in two columns that’s why I deleted them
- • Performed one-hot encoder on categorical columns.
- • Perform Ordinal Encoder on Ordinal Columns.
- • Scaling is performed for needed information.
- • And, the info is prepared for passing to the machine learning formula

### Modelling
The pre-processed information is then envisioned and every one the specified insights are being drawn. though from the drawn insights, the info is at random unfold however still modelling is performed with completely different machine learning algorithms to form positive we tend to cowl all the chances. and eventually, Gradient Boosting performed well .

### Batch Prediction

In the pursuit of creating a comprehensive and efficient system, we have successfully executed batch prediction as a pivotal component of our project. Leveraging a meticulously designed data transformation pipeline, we have harnessed the power of our predictive model to generate accurate and timely batch predictions. This milestone signifies the culmination of our efforts in seamlessly processing and analyzing data, resulting in actionable insights that drive informed decision-making. As we prepare our Low-Level Design Document, this achievement underscores the significance of our data transformation pipeline and predictive model, which will be elaborately detailed to ensure clarity and scalability in our system architecture.

### Training And Prediction Pipeline

In our endeavor to create a robust and end-to-end data-driven solution, we have meticulously crafted both a training pipeline and a prediction pipeline. The training pipeline serves as the backbone for developing our predictive models, allowing us to iteratively train and fine-tune them with the highest precision possible. Meanwhile, the prediction pipeline enables us to seamlessly apply these trained models to new data, ensuring that our insights and forecasts remain consistently accurate and adaptable to real-world scenarios. This dual pipeline approach embodies our commitment to providing a comprehensive, data-driven solution that empowers decision-makers with the most reliable and up-to-date information. As we delve into the creation of our Low-Level Design Document, we will intricately detail these pipelines, showcasing their sophistication and efficiency in our system architecture.

### UI Integration

Both CSS and HTML files are being created and are being integrated with the created machine learning model. All the required files are then integrated to the app.py(For localhost), Application.py(For Streamlit) file and tested locally

## Project Link - 
```
https://storesalesprediction-2gn2t3crrjnnh8kptxtlhq.streamlit.app/
```

## Vedio Url - 
```
https://youtu.be/N4BAEqE9To4?si=eqMiwijfHjaZEQli
```

