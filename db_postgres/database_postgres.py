from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()


class FetcherDB:
    def __init__(self):
        dbname = os.getenv("POSTGRES_DB")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")

        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activities (
                id SERIAL PRIMARY KEY,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                link TEXT,
                key INTEGER,
                accessibility REAL
            )
        """
        )
        self.conn.commit()

    def insert_activity(self, activity):
        self.cursor.execute(
            """
            INSERT INTO activities (
            activity,
            type,
            participants,
            price,
            link,
            key,
            accessibility)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            (
                activity["activity"],
                activity["type"],
                activity["participants"],
                activity["price"],
                activity["link"],
                activity["key"],
                activity["accessibility"],
            ),
        )
        self.conn.commit()

    def get_last_activities(self, num_activities):
        self.cursor.execute(
            """
            SELECT * FROM activities
            ORDER BY id DESC
            LIMIT %s
        """,
            (num_activities,),
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
