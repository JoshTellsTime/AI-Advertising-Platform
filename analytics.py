# analytics.py

import psycopg2
from database import Database

class Analytics:
    @staticmethod
    def track_ad_performance(ad_id):
        connection = Database.get_connection()
        cursor = connection.cursor()

        try:
            # Query to fetch ad performance data
            query = "SELECT * FROM ad_performance WHERE ad_id = %s"
            cursor.execute(query, (ad_id,))

            ad_performance_data = cursor.fetchall()

            # Return ad performance data
            return ad_performance_data

        except psycopg2.DatabaseError as error:
            print(f"Error: {error}")
            return None

        finally:
            # Close the cursor and connection
            cursor.close()
            Database.return_connection(connection)

    @staticmethod
    def report_ad_performance(ad_id):
        # Fetch ad performance data
        ad_performance_data = Analytics.track_ad_performance(ad_id)

        if ad_performance_data is not None:
            # Generate and print report
            print(f"Ad Performance Report for Ad ID: {ad_id}")
            for row in ad_performance_data:
                print(f"Date: {row[0]}, Impressions: {row[1]}, Clicks: {row[2]}, Conversions: {row[3]}")
        else:
            print("No data available for the given Ad ID.")