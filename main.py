from etl.fetch_trending import fetch_trending
from analysis.trending_analysis import trending_analysis
from DB.insert_data import insert_data
from DB.run_queries import run_query
from DB.queries import avg_views_by_country, hourly_upload_trends,eng_ratio

def main():
    countries = ["IN"]

    for country in countries:
        print(f"Fetching {country}'s data...")
        fetch_trending(country)

        print(f"Analysing and cleaning {country}'s data...")
        cleaned_data = trending_analysis(country)

        print(f"Saving {country}'s data...")
        insert_data(cleaned_data, country)

        print(f"Processing complete for {country}")

#     run queries
    print("Average views by country")
    run_query(avg_views_by_country)

    print("Hourly upload trends")
    run_query(hourly_upload_trends)

    print("Engagement Ratio")
    run_query(eng_ratio)

if __name__ == "__main__":
    main()