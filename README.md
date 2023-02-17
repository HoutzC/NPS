<p align="center">
  <img src="https://user-images.githubusercontent.com/109249712/179049823-0ab72b6d-efc4-4e88-bdec-3ee159c12e11.jpeg">
 </p>

A fully automated ETL pipeline that requests data from the National Park Service (NPS) API, scrapes various data sources, transforms and cleans data, connects to PowerBI, and visualizes data to provide analytical insights into visitation and economic trends of national park resources over the past 20 years.

# Description
This project was developed based on my passion for parks and outdoor recreation. Once I stumbled across the large amount of public data the NPS had collected I saw an opportunity to further develop my skills and understanding of data engineering by applying a variety of tools and resources to see what could be done with the data.

As this is is an exhibition, the project was intentionally designed to be overly complex by incorporating a variety of tools and expertise that may not necessarily be required.

# On-Premises Architecture
 
<p align="center">
  <img src="https://user-images.githubusercontent.com/109249712/218531457-d255e7c8-7d67-4a57-9dea-72ddbdebfefd.PNG">
 </p>

1) Windows Task Scheduler is set to run Python Scripts on pre-determined schedule
2) Data collection:

    - Data is requested from the NPS API and saved as a .csv

      `Python script for connecting to NPS API` | [API](../../blob/main/SCRIPTS/API.py)
    
    - Economic Impact Reports are manually collected from the Department of the Interior, and tables are extracted and compiled

      `Python script for extracting, cleaning, and compiling economic impact report PDFs` | [ReadPDF](../../blob/main/SCRIPTS/READPDF.py)
    
    - Public Use Statistics Reports are manually collected from the National Park Service Visitor Usage Statistics Report, compiled, and saved to .csv

      `Python script for cleaning and compiling Public Use Statistics Report CSVs` | [Visits](../../blob/main/SCRIPTS/Visits.py)
      
      `Automated script that extracts data using Selenium Web Driver (*BETA*)` | [*Comming Soon]
 
    - Weather and Climate data is scraped from Wikipedia and saved as a .csv

      `Python script for scraping and cleaning tables from Wikipedia` | [WikiScraper](../../blob/main/SCRIPTS/WikiScraper.py)

3) .csv data is stored in a folder
4) Data is connected to PowerBi service via On-Premises Data Gateway (Personal Mode)
5) PowerBi Dashboard is connected to dataset
6) PowerBi Service is set to Refresh and Publish at pre-determined schedule
7) Finalized Powerbi report is published.

>Power BI limits datasets on shared capacity to eight daily refreshes, and 48 daily refreshes if the dataset it on a Premium Capacity. Task Scheduler has no daily limit for how many times you can run the python scrypts.


# AWS Cloud Architecture (*BETA*)
<p align="center">
  <img src="https://user-images.githubusercontent.com/109249712/179039638-e412d81b-7afe-4f8e-a192-fb0bb1bc7ac3.png">
 </p>

1) Data Collection:
    
    - Data is requested from the NPS API and saved as a .csv

      `Python script for connecting to NPS API` | [API](../../blob/main/SCRIPTS/API.py)
    
    - Economic Impact Reports are manually collected from the Department of the Interior, and tables are extracted and compiled

      `Python script for extracting, cleaning, and compiling economic impact report PDFs` | [ReadPDF](../../blob/main/SCRIPTS/READPDF.py)
    
    - Public Use Statistics Reports are manually collected from the National Park Service Visitor Usage Statistics Report, compiled, and saved to .csv

      `Python script for cleaning and compiling Public Use Statistics Report CSVs` | [Visits](../../blob/main/SCRIPTS/Visits.py)
 
    - Weather and Climate data is scraped from Wikipedia and saved as a .csv

      `Python script for scraping and cleaning tables from Wikipedia` | [WikiScraper](../../blob/main/SCRIPTS/WikiScraper.py)

3) Data is uploaded and stored in an S3 bucket
4) Redshift database is established and deployed
5) Redshift is connected to Powerbi
6) Finalized Powerbi report is published


# End Product
<p align="center">
  <img src="https://github.com/HoutzC/NPS-Discover/blob/main/gif.gif">
</p>

Interact with the final product [here](https://app.powerbi.com/view?r=eyJrIjoiNGM3NTRiYjUtYmEwYS00NmQzLTk0NDgtNTFhODA2MjRiZDc5IiwidCI6ImQ1Mzc5MjYzLWEzMTQtNGE0Ny04NTBlLWI1ODI4NTdjYTE0NCJ9)!

> The final product is an interactive BI report that visualizes 20 years of national park data to help understand the economic impact of resources managed by the National Park Service. Final Report is sourcing data from a static CSV file as the database was terminated upon project completion to minimize costs.


Key features of the dashboard:
- A UX designed to deliver key KPI's and visuals with a premium product experience
- Simple and intuitive navigation panels to quickly move through the tool
- Auto scaling map using spacial data uploaded to mapbox to generate park boundaries
- Dynamic badges, icons, and images based on user selected filters to quickly convey key information
- Dynamic web links to relevent resources based on user filter selections
- Dynamic smart text to quickly summarize data for easy digestion and messaging based on filters
- Toggle buttons to increase report functionality and alleviate congestion
- Help menu for simple new user support
- Excel data export (implemented but not active/available in the publish to web environment to lower project costs)


# Improvement Suggestions
- Implement a data/report refresh notification system using Amazon SNS
- Improve data prediciton capabilities using machine learning functions within AWS
- Use Amazon Textract to improve data quality and range by extracting text from documents
- Push all ETL to AWS to increase Powerbi efficiency at scale.

# Continued Reading & Resources 
[AWS Serverless Data Analytics Pipeline](https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/aws-serverless-data-analytics-pipeline.pdf#aws-serverless-data-analytics-pipeline)

[AWS Serverless Multi-Tier Architectures with Amazon API Gateway and AWS Lambda](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/serverless-multi-tier-architectures-api-gateway-lambda.pdf#welcome)

[Using Microsoft Power BI with the AWS Cloud](https://docs.aws.amazon.com/en_us/whitepapers/latest/using-power-bi-with-aws-cloud/using-power-bi-with-aws-cloud.pdf)

[What is an on-premises data gateway?](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem#install-the-on-premises-data-gateway)

[Task Scheduler for Developers](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)

[Data refresh in Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data)
