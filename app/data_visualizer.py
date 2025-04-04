import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, aggregated_data):
        self.aggregated_data = aggregated_data
        sns.set_style("whitegrid")

    def plot_skill_count(self):
        plt.figure(figsize=(10, 5))
        sns.barplot(data=self.aggregated_data, x="skill", y="count", palette="Blues_r", hue="skill", legend=False)
        plt.title("Count of Records per Skill")
        plt.show()

    def plot_mean_score(self):
        # print(self.aggregated_data)
        plt.figure(figsize=(10, 5))
        sns.barplot(data=self.aggregated_data, x="skill", y="mean_score", palette="Blues_r", hue="skill", legend=False)
        plt.title("Mean Score per Skill")
        plt.show()

    def plot_min_max_score(self):
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=self.aggregated_data, x="skill", y="min_score", marker="o", label="Min Score", color="red")
        sns.lineplot(data=self.aggregated_data, x="skill", y="max_score", marker="o", label="Max Score", color="green")
        plt.title("Min and Max Scores per Skill")
        plt.legend()
        plt.show()

    def plot_count_vs_mean(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=self.aggregated_data, x="count", y="mean_score", hue="skill", palette="tab10", s=100)

        plt.title("Skill Score Distribution")
        plt.xlabel("Number of Records (Count)")
        plt.ylabel("Mean Score")
        plt.show()
