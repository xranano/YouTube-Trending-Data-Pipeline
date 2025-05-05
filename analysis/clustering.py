from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from DB.run_queries import run_query
import pandas as pd
import seaborn as sns

df = run_query("select *, extract(hour from published_at) as published_hour from videos;")
df['published_at'] = pd.to_datetime(df['published_at'])
df['published_hour'] = df['published_hour'];

df = pd.get_dummies(df, columns=['country'])

features = df[['view_count', 'published_hour', 'like_count', 'comment_count'] + [col for col in df.columns if col.startswith('country_')]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_features)

sns.pairplot(df[['view_count', 'like_count', 'comment_count', 'cluster']], hue='cluster')
plt.show()

cluster_profiles = df.groupby("cluster")[["view_count", "like_count", "comment_count"]].mean()
print(cluster_profiles)


melted = df.melt(id_vars=["cluster"],
                 value_vars=["view_count", "like_count", "comment_count"],
                 var_name="Metric", value_name="Value")

plt.figure(figsize=(12, 6))
sns.boxplot(x="Metric", y="Value", hue="cluster", data=melted)
plt.yscale("log")
plt.title("Distribution of Features per Cluster")
plt.show()

