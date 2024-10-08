# reddit-project
This is a Data Engineering Project

# Reddit Data ETL Pipeline Project

For this project, I utilized Docker to set up and maintain an infrastructure consisting of **Apache Airflow**, **Celery**, **PostgreSQL**, and **Redis**. This containerized approach facilitated the orchestration of workflows and ensured a consistent environment for the various components involved in the ETL process.

## Project Goals

### Data Extraction:
- The primary objective is to pull data from the Reddit platform, specifically from a chosen subreddit, **dataengineering**.
- I employed the **PRAW (Python Reddit API Wrapper)** library, which allows for straightforward access to Reddit's API, enabling the extraction of relevant posts efficiently.

### Data Transformation:
- Once the data is extracted, it undergoes a transformation process to ensure it is in a usable format. This involves cleaning the data by:
  - Converting timestamps to a datetime format for better usability.
  - Ensuring that boolean fields are consistently represented.
  - Making other adjustments necessary for preparing the data for analysis or storage.

### Data Loading:
- The final step involves saving the transformed data into a CSV file.
- This CSV file is then uploaded to an **AWS S3** bucket for further analysis, storage, or archiving purposes.

## Components of the Project

### DAG Definition (dag.py):
- The Directed Acyclic Graph (DAG) is defined using **Apache Airflow**, which is responsible for managing the workflow of the ETL process.
- The DAG includes:
  - A task to extract data from Reddit, utilizing the `reddit_pipeline` function.
  - A task that uploads the generated CSV file to an **AWS S3** bucket.

### Reddit Data Extraction and Transformation (reddit_etl.py):
- `connect_reddit`: Establishes a connection to Reddit using the provided API credentials.
- `extract_posts`: Pulls the top posts from the specified subreddit based on time filters and a defined limit.
- `transform_data`: Cleans and transforms the extracted data to ensure it meets the required format and standards.
- `load_data_to_csv`: Saves the cleaned DataFrame as a CSV file to the specified output path.

### Pipeline Execution (reddit_pipeline.py):
- The `reddit_pipeline` function orchestrates the entire ETL process by:
  - Connecting to Reddit.
  - Extracting posts from the specified subreddit.
  - Transforming the data to the desired format.
  - Loading the transformed data into a CSV file for storage.

## Workflow Overview

### Extraction Task (extract):
- This task initiates the Reddit extraction process by calling the `reddit_pipeline`.
- It passes parameters such as the filename, subreddit, time filter, and limit to customize the data extraction.

### Upload Task (upload_s3):
- After the extraction and CSV file generation, this task uploads the file to an **AWS S3** bucket.
- The upload occurs only after successful data extraction, maintaining the integrity of the workflow.

### Execution Order:
- The tasks are linked together using `extract >> upload_s3`, ensuring the upload task follows the extraction task in execution order.

## Data Management and Analysis Workflow

### AWS Glue Job Creation:
- After uploading the extracted CSV file to the S3 bucket, I created an **AWS Glue** job.
- I used an **AWS Glue crawler** to create a database and tables from the data, which facilitated efficient data management and querying.

### Data Transformation and Manipulation:
- Within the Glue job, I combined the last three columns of the data to create a more insightful dataset.
- This transformed dataset was then saved back into **S3** for further use.

### Querying with Amazon Athena:
- I utilized **Amazon Athena** to query the transformed data stored in S3, allowing for quick data exploration and analysis.
- This step provided insights and a better understanding of the data extracted from Reddit.

### Integration with Amazon Redshift:
- The transformed data was connected to **Amazon Redshift**, enabling the execution of complex queries.
- I performed various analyses and visualizations on the data to uncover trends and insights relevant to the subreddit.

## Potential Uses of the Data
- **Data Analysis**: Analyzing trends in discussions related to data engineering, such as popular topics, user engagement, and more.
- **Machine Learning**: Using the extracted data to build models for sentiment analysis, topic modeling, or user behavior analysis.
- **Reporting**: Generating reports or dashboards for stakeholders interested in insights from the data engineering subreddit.

## Conclusion
Overall, this project aims to automate the process of collecting, transforming, and preparing Reddit data for analysis, leveraging modern data engineering tools and practices. By utilizing Docker, **AWS Glue**, **Athena**, and **Redshift**, I have created a robust ETL pipeline that not only extracts and processes data but also facilitates in-depth analysis and visualization. 

