import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load mock ARG annotation
df = pd.read_csv("input/mock_ARG_annotations.tsv", sep="\t")

# Group by resistance class
arg_summary = df.groupby("class")["gene"].count().reset_index()
arg_summary.columns = ["Resistance_Class", "Gene_Count"]

# Save summary table
os.makedirs("output", exist_ok=True)
arg_summary.to_csv("output/ARG_summary.csv", index=False)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(data=arg_summary, x="Resistance_Class", y="Gene_Count", palette="mako")
plt.title("ARG Distribution by Resistance Class")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/ARG_barplot.png")
plt.close()
