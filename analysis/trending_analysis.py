import pandas as pd

def trending_analysis(country):

    df = pd.read_csv(f'./data/trending_{country}.csv')

    df['published_at'] = pd.to_datetime(df['published_at'])
    df['view_count'] = df['view_count'].fillna(0).astype(int)
    df['comment_count'] = df['comment_count'].fillna(0).astype(int)
    df['like_count'] = df['like_count'].fillna(0).astype(int)

    df = df[['title', 'published_at', 'channel_title', 'view_count', 'comment_count', 'like_count']]
    # print(df.sort_values("view_count", ascending=False).head(10))
    df.to_csv(f"data/trending_{country}_cleaned.csv", index=False)

    return df;
