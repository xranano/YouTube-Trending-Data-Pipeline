# 🌍 YouTube Trending Data Pipeline

This project builds an end-to-end data engineering pipeline using the YouTube Data API to extract, clean, store, and analyze trending video data across multiple countries.

## ✅ Project Scope

### 1. YouTube API Integration
- Set up OAuth 2.0 access to YouTube Data API v3.
- Successfully tested and authenticated API requests.

### 2. Data Extraction
- Pulled trending video metadata for the following countries:
  - United States (US)
  - Georgia (GE)
  - Sweden (SE)
- Data includes: title, publish date, view count, like count, comment count, and more.

### 3. Data Cleaning and Normalization
- Handled missing values and standardized data types using pandas.
- Normalized datetime fields and cast numerical fields to appropriate types.
- Stored intermediate cleaned `.csv` files for each country.

### 4. Database Integration
- Designed and implemented a PostgreSQL schema with a `videos` table.
- Loaded cleaned datasets into the database using psycopg2.
- Ensured consistent formatting for future queries and analytics.

### 5. Exploratory Data Analysis
- Executed SQL and pandas-based queries to analyze:
  - Average views per country
  - Most common trending categories
  - Distribution of likes, comments, and views

### 6. Clustering (Unsupervised Learning)
- Performed KMeans clustering to group trending videos based on:
  - Views, likes, comments, publish hour, and country
- Visualized clusters using seaborn's `pairplot`
- Scaled features using `StandardScaler` for optimal clustering performance

## 🧰 Tech Stack

- Python (pandas, requests, sklearn, matplotlib, seaborn)
- PostgreSQL
- YouTube Data API v3
- SQL
- PyCharm

