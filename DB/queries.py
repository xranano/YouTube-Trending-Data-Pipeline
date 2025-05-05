avg_views_by_country="""select country, ROUND(AVG(view_count)) as avg_views from videos group by country order by avg_views desc;"""

hourly_upload_trends="""select extract(hour from published_at) as upload_hour, round(avg(view_count)) as avg_views
from videos
group by upload_hour
order by upload_hour;"""

eng_ratio="""SELECT 
    country,
    ROUND(AVG((like_count + comment_count)) / avg(view_count), 3) AS avg_eng
FROM 
    videos 
where view_count > 0
GROUP BY 
    country
order by avg_eng desc;"""


