import pandas as pd

class DataAggregator:
    def __init__(self, clean_data):
        # even if we don’t modify it, keeping a reference allows for re-aggregation if needed
        self.clean_data = clean_data
        self.aggregated_results = None  
    
    def calculate_skill_aggregations(self):
        df = pd.DataFrame(self.clean_data)

        # need to use .agg() to compute multiple aggregations within the groupby
        self.aggregated_results = df.groupby('skill').agg(
            count=("score", "size"),  # count rows per skill
            min_score=("score", "min"),  # min score per skill
            mean_score=("score", "mean"),  # mean score per skill
            max_score=("score", "max"),  # max score per skill
        ).reset_index()

    def save_to_csv(self, output_file_path):
        self.aggregated_results.to_csv(output_file_path)

