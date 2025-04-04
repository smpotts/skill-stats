# Data Cleaner 
This project is designed to process, validate, and clean raw JSON data from multiple sources. The data is then aggregated and stored in a structured format for further analysis or use.

## File structure
`app/data_cleaner.py`: The `DataCleaner` class and contains methods for processing and cleaning the raw data.  
`app/data_aggregator.py`: The `DataAggregator` class contains methods for aggregating the cleansed data.
`app/data_visualizer.py`: The `DataVisualizer` class contains methods for visualizing the data after aggregations.
`data/`: Directory containing raw JSON data files (e.g., proficiency.json, skills.json, data.json).  
`output/`: Directory containing the aggregated data post-cleansing.

## Running the app
To run the project, run the `main.py` file.