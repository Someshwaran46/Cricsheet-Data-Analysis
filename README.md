# Cricsheet-Data-Analysis
Automates Cricsheet JSON scraping using Selenium, structures data in MySQL with separate tables for Test, ODI, IPL, and T20 matches, runs SQL queries for player and team analysis, and visualizes insights with a dynamic Power BI dashboard.

### **Folder:** `1. Web Scrapping`  
  - Contains scripts to automate downloading JSON files from Cricsheet using **Selenium**.  

#### **Files:**  
- **`Web_Scrapping.py`** – Downloads all available JSON files from Cricsheet and stores them in the **"Web_Scrapping Downloads"** folder.  
- **`Specific_JSON.py`** – Downloads specific JSON files from Cricsheet and stores them in the **"Specific JSON"** folder.
 

### **Folder:** `2. Dataframe conversion and SQL insertion`  
  - Contains scripts to convert JSON files into Pandas DataFrames and store them in SQL tables under the **cricket** database.  

#### **Files:**  
- **`ipl.py`** – Processes IPL JSON data and inserts it into the `ipl` table.  
- **`odis.py`** – Processes ODI JSON data and inserts it into the `odis` table.  
- **`t20s.py`** – Processes T20 JSON data and inserts it into the `t20s` table.  
- **`tests.py`** – Processes Test match JSON data and inserts it into the `tests` table.

### **Folder:** `3. Data Visualization`  
  - Contains scripts for visualizing cricket data using SQL queries and Python libraries.  

#### **File:**  
- **`Data Visualization.ipynb`** – Executes 20 SQL queries and visualizes the results using **Matplotlib** and **Seaborn**.

### **Folder:** `4. Power BI Dashboard`  
  - Contains the Power BI dashboard for visualizing cricket match insights.  

#### **File:**  
- **`cricsheet.pbix`** – Power BI dashboard displaying key insights from various matches.
