import sqlite3


class FetcherDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                accessibility REAL,
                key REAL,
                link TEXT
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
            accessibility,
            key,
            link
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                activity["activity"],
                activity["type"],
                activity["participants"],
                activity["price"],
                activity["accessibility"],
                activity["key"],
                activity["link"],
            ),
        )
        self.conn.commit()

    def get_last_activities(self, num_activities):
        self.cursor.execute(
            """
            SELECT * FROM activities
            ORDER BY id DESC
            LIMIT ?
            """,
            (num_activities,),
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = FetcherDB("qq.db")

    activity_data = {
        "activity": "Learn and play a new card game",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "https://www.pagat.com/",
        "key": "9660022",
        "accessibility": 0,
    }

    db.insert_activity(activity_data)
