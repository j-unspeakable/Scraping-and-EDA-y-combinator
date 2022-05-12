## **CONTENTS**
1. [Description](#desc) 
2. [Web Scraping](#scrape)
3. [Data Wrangling and Exploratory Data Analysis](#eda)
4. [Summary](#summ)

<a name="desc"></a>
## **1. DESCRIPTION**
The aim of this project is to demonstrate an end-to-end data engineering workflow involving data extraction or collection, wrangling, cleaning, and exploratory data analysis. (Akin to an ETL process). The activities carried out in this regard are listed as follows:
- Data Extraction (Web Scraping) 
- Exploratory Data Analysis (EDA)


<a name="scrape"></a>
## **2. WEB SCRAPING** (`ycombinator_scraper.ipynb` / `ycombinator_scraper.py`)
Scraping a website using beautifulsoup and selenium frameworks and converting the scraped data into a readable csv document.
Details about the data scraped from the website is in the notebook.

- ### INFORMATION TO BE SCRAPED
The image below indicates the information to be scraped from the website: https://www.ycombinator.com/companies

<img width="" alt="Screenshot 2022-04-03 at 7 29 58 PM" src="https://user-images.githubusercontent.com/55639062/161443204-ae7fc423-f1d3-4512-bb56-7bef85f3691e.png">

Details on how the scraping was carried out is clearly documented in the notebook. 
Highlights of the data that was scraped for each company are:

- Company name,
- Company tag,
- Short description,
- Founded,
- Location,
- Country,
- Team size,
- Website,
- Active founders,
- Social media link(s) of the company,
- Founders name and social media link(s),
- Description.


<a name="eda"></a>
## **3. DATA WRANGLING AND EXPLORATORY DATA ANALYSIS (EDA)(`ycombinator_eda.ipynb`)**
- ### **FEATURE ENGINEERING**
A feature that depicts the number of founders in each company was engineered and used in both univariate and bivariate analysis. 


- ### **ALL CHARTS FOR UNIVARIATE AND BIVARIATE ANALYSIS**
    ### **For univariate analysis:**

    - **Most represented country:** From the figure below, the most represented country home to the most companies is the USA with an overwhelming count of 654 out oof a total of 1000 companies. It is followed by India, Canada, UK ....etc.
    ![output1](https://user-images.githubusercontent.com/92790663/168176456-c2e14b7e-3b8d-4644-9e3c-e5c1bd7206c1.png)


    - **Year companies were founded:** From the figure below, most of the companies recorded were founded in the year 2021.
    ![output2](https://user-images.githubusercontent.com/92790663/168176457-3c984e9f-445d-4a6d-aef7-9019ab153aec.png)

    - **Team size:** From the figure below, most Team_size falls within the range of 2-10 and a right-skewed plot is noticed in that regard.
    ![output3](https://user-images.githubusercontent.com/92790663/168176459-67f7c959-3ea3-4b73-b0d0-20c2aa13a2fb.png)

    - **Number of founders:** From the figure below, 546 companies out of a 1000 had just 2 founders, followed by 214 companies with 1 founder and 191 companies with 3 founders.
    ![output4](https://user-images.githubusercontent.com/92790663/168176449-dbec7bc3-8b4e-4081-a46b-0467fb4209e0.png)

    ### **For bivariate analysis:**

    - **Relationship between Country and Year_founded**
    ![output5](https://user-images.githubusercontent.com/92790663/168176452-8974f3ea-6451-45f8-b881-759dfee7c742.png)

    - **Relationship between Country and Team_size**
    ![output6](https://user-images.githubusercontent.com/92790663/168176453-b6e268ad-01fc-4e5e-b9c4-dda5701d774c.png)

    - **Relationship between Country and Number of Founders**
    ![output7](https://user-images.githubusercontent.com/92790663/168176454-52c4202c-4822-4059-b454-677b61880931.png)

<a name="summ"></a>
## **4. SUMMARY**
From the univariate and bivariate analysis, some inferences were drawn. Some of the notable ones are:
- The most represented country in the observations is the USA with a total of 654 out of 1000 observations.
- Most of the companies in the observations was founded in the year 2021.
- Most of the team sizes in the observations falls within the range of 2-10 and a right-skewed image is noticed in that regard.
- 546 companies out of a 1000 had just 2 founders, followed by 214 companies with 1 founder and 191 companies with 3 founders. 
- There is no notable relationship between Country - Founded, Country - Team_size, and Country - Number_of_founders.