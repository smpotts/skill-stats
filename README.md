# Skill Stats 
This project is designed to process, validate, and clean raw JSON data from multiple sources. The data is then aggregated and stored in a structured format for further analysis or use.  It follows a structured pipeline:

- Data Processing – Cleans and validates raw data.
- Aggregation – Computes statistics like count, min, mean, and max scores per skill.
- Visualization – Generates insightful plots to understand skill trends.

## File Structure
`app/data_cleaner.py`: The `DataCleaner` class and contains methods for processing and cleaning the raw data.  
`app/data_aggregator.py`: The `DataAggregator` class contains methods for aggregating the cleansed data.
`app/data_visualizer.py`: The `DataVisualizer` class contains methods for visualizing the data after aggregations.
`data/`: Directory containing raw JSON data files (e.g., proficiency.json, skills.json, data.json).  
`output/`: Directory containing the aggregated data post-cleansing.

## How It Works 
To run the project, run the `main.py` file, which kicks off the following steps:

### 1. Data Processing (`data_processor.py`)
- Reads raw JSON files (proficiency.json, skills.json, data.json).
- Validates structure and ensures required fields exist.
- Cleans bad or inconsistent data (e.g., non-integer scores, missing skills).
- Stores cleaned data in class attributes.

### 2, Data Aggregation (`data_aggregator.py`)
Uses pandas to compute:
- Count of records per skill
- Minimum, maximum, and mean scores
- Stores aggregated results for visualization.

### 3. Data Visualization (`data_visualizer.py`)
Uses seaborn and matplotlib to generate:
- Bar charts (Mean score per skill)
- Line charts (Min, mean, max scores per skill)
- Scatter plots (Count vs. mean score trends)
