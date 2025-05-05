import requests
import pandas as pd

API_KEY = 'AIzaSyB4IC8f3JtvzBFeRtOeW9qSne2M-Xnd9-w';
BASE_URL = 'https://www.googleapis.com/youtube/v3/videos'

def fetch_trending(country):
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": country,
        "maxResults": 50,
        "key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print('Error', response.json());
        exit()

    data = response.json();
    print(data['items'][0])

    videos = [];
    for item in data['items']:
        snippet = item['snippet']
        stats = item.get('statistics', {})

        video = {
            "video_id": item["id"],
            "title": snippet.get("title"),
            "published_at": snippet.get("publishedAt"),
            "channel_title": snippet.get("channelTitle"),
            "category_id": snippet.get("categoryId"),
            "tags": snippet.get("tags", []),
            "view_count": stats.get("viewCount"),
            "like_count": stats.get("likeCount"),
            "comment_count": stats.get("commentCount")
        }

        videos.append(video);

    df = pd.DataFrame(videos)

    df.to_csv(f"./data/trending_{country}.csv", index=False)
    # print(f'Done, Saved Trending {country} Stats!')

    return data;

