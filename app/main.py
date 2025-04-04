from data_cleaner import DataCleaner
from data_aggregator import DataAggregator
from data_visualizer import DataVisualizer

def main():
    cleaner = DataCleaner(
        proficiency_path="data/proficiency.json",
        skills_path="data/skills.json",
        data_path="data/data.json"
    )
    cleaner.process()

    aggregator = DataAggregator(cleaner.clean_data)
    aggregator.calculate_skill_aggregations()
    aggregator.save_to_csv("output/skill_aggregations.csv")

    data_viz = DataVisualizer(aggregator.aggregated_results)
    data_viz.plot_skill_count()
    data_viz.plot_mean_score()
    data_viz.plot_min_max_score()

if __name__ == "__main__":
    main()