from DB.database import connect_to_db

def insert_data(data, country):
    conn = connect_to_db()
    if not conn:
        print("Connection unsuccessful")
        return

    cursor = conn.cursor()
    insert_query = """
    INSERT INTO public.videos(
	title, published_at, channel_title, view_count, like_count, comment_count, country)
	VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    for _, video in data.iterrows():
        cursor.execute(insert_query, (
            video['title'],
            video['published_at'],
            video['channel_title'],
            video['view_count'],
            video['like_count'],
            video['comment_count'],
            country
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data inserted successfully")
