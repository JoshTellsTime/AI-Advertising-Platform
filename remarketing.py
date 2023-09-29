# remarketing.py

from database import Database
from api_integration import APIIntegration

class Remarketing:
    @staticmethod
    def track_user_interaction(user_id, interaction):
        connection = Database.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO user_interactions (user_id, interaction) VALUES (%s, %s)"
        cursor.execute(query, (user_id, interaction))

        connection.commit()
        cursor.close()
        Database.return_connection(connection)

    @staticmethod
    def generate_targeted_ads(user_id):
        connection = Database.get_connection()
        cursor = connection.cursor()

        query = "SELECT interaction FROM user_interactions WHERE user_id = %s"
        cursor.execute(query, (user_id,))

        interactions = cursor.fetchall()
        cursor.close()
        Database.return_connection(connection)

        targeted_ads = []
        for interaction in interactions:
            # Here you can add logic to generate targeted ads based on user interactions
            # For example, you can use the APIIntegration class to request ads related to the user's interactions
            ad = APIIntegration.google_api_request('ad_endpoint', {'interaction': interaction})
            targeted_ads.append(ad)

        return targeted_ads