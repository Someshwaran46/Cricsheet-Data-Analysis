# 🏏 Cricsheet Data Analysis Project

**A full-stack cricket analytics pipeline** that scrapes match data from [Cricsheet](https://cricsheet.org/), stores it in MySQL, performs insightful SQL analyses, and visualizes results using Python and Power BI — empowering data-driven decisions for cricket fans, analysts, and developers.

---

## 📂 Folder Overview

### 📁 `1. Web Scraping`  
Automates the collection of match data from Cricsheet using **Selenium**.

#### 🔹 Files:
- **`Web_Scrapping.py`**  
  Downloads **all** available JSON files and saves them in the `Web_Scrapping Downloads/` folder.
  
- **`Specific_JSON.py`**  
  Allows downloading of **specific match JSONs** and stores them in the `Specific JSON/` folder.

---

### 📁 `2. DataFrame Conversion & SQL Insertion`  
Processes raw JSON into structured data and inserts it into **MySQL** under the `cricket` database.

#### 🔹 Files:
- **`ipl.py`** – Converts IPL data and stores it in the `ipl` table.  
- **`odis.py`** – Converts ODI data and stores it in the `odis` table.  
- **`t20s.py`** – Converts T20 data and stores it in the `t20s` table.  
- **`tests.py`** – Converts Test match data and stores it in the `tests` table.

---

### 📁 `3. Data Visualization`  
Brings cricket data to life using SQL + Python.

#### 🔹 File:
- **`Data Visualization.ipynb`**  
  Runs 10 analytical SQL queries and visualizes them using **Matplotlib** and **Seaborn** (e.g., top batsmen, win ratios, economy rates).

---

### 📁 `4. Power BI Dashboard`  
Interactive dashboard to explore patterns, performances, and match dynamics across formats.

#### 🔹 File:
- **`cricsheet.pbix`**  
  A dynamic **Power BI dashboard** packed with visuals like bar charts, heatmaps, and trend lines for intuitive cricket insights.

---

## ✅ Key Features
- 🔄 **Automated Scraping** of JSON data with Selenium  
- 🗃️ **Structured Storage** in MySQL across Test, ODI, IPL, and T20 formats  
- 📊 **20+ SQL Queries** for player/team analytics  
- 📈 **Rich Visualizations** with Matplotlib, Seaborn, and Power BI  

---

## 🔧 How to Run the Project Locally

Follow these steps to clone and execute the Cricsheet Data Analysis pipeline on your machine.

---

### 📥 1. Clone the Repository

```bash
git clone https://github.com/Someshwaran46/Cricsheet-Data-Analysis.git
cd Cricsheet-Data-Analysis
```

---

### 🧪 2. (Optional) Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

---

### 📦 3. Install Required Dependencies

```bash
# If requirements.txt is available
pip install -r requirements.txt

# Otherwise, install manually
pip install selenium pandas mysql-connector-python matplotlib seaborn
```

---

### 🛢️ 4. Set Up MySQL Database

1. Ensure MySQL is installed and running on your system.
2. Create a database named `cricket`.
3. Update database credentials (username/password) in the `.py` scripts if needed (default is usually `root`/`root`).

---

### 🚀 5. Execute the Project Scripts

#### 🔹 Step 1: Web Scraping

```bash
# To download all match JSONs
python 1. Web Scrapping/Web_Scrapping.py

# Or download specific match JSONs
python 1. Web Scrapping/Specific_JSON.py
```

#### 🔹 Step 2: JSON to MySQL Insertion

```bash
python 2. Dataframe conversion and SQL insertion/ipl.py
python 2. Dataframe conversion and SQL insertion/odis.py
python 2. Dataframe conversion and SQL insertion/t20s.py
python 2. Dataframe conversion and SQL insertion/tests.py
```

#### 🔹 Step 3: Data Visualization with SQL + Python

```bash
# Open the notebook in Jupyter or VSCode
jupyter notebook "3. Data Visualization/Data Visualization.ipynb"
```

#### 🔹 Step 4: Open Power BI Dashboard

- Launch `4. Power BI Dashboard/cricsheet.pbix` using Power BI Desktop.

---

## 📬 Feedback

- Feel free to open issues or submit pull requests! Improvements, and suggestions are always welcome 🙌
- For clarifications drop an email to somesh4602@gmail.com

---
