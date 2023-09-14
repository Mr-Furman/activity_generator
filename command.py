import argparse

from data_fetcher import BoredAPIFetcher
from db_lite.database_sqllite import FetcherDB

# If you use POSTGRES 'from db_postgres.database_postgres import FetcherDB'


def parse_args():
    parser = argparse.ArgumentParser(description="Bored API Command Line Tool")
    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")

    parser_new = subparsers.add_parser("new", help="Get a new random activity")
    parser_new.add_argument("--type", help="Type of the activity")
    parser_new.add_argument(
        "--participants", type=int, help="The number of participants"
    )
    parser_new.add_argument("--price_min", type=float, help="Minimum price")
    parser_new.add_argument("--price_max", type=float, help="Maximum price")
    parser_new.add_argument(
        "--accessibility_min", type=float, help="Minimum accessibility"
    )
    parser_new.add_argument(
        "--accessibility_max", type=float, help="Maximum accessibility"
    )
    parser_new.add_argument("--key", type=int, help="key")
    parser_new.add_argument("--link", type=float, help="link")

    subparsers.add_parser("list",
                          help="List recent activities from the database")

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == "new":
        api_client = BoredAPIFetcher()

        query_params = {
            "type": args.type,
            "participants": args.participants,
            "minprice": args.price_min,
            "maxprice": args.price_max,
            "minaccessibility": args.accessibility_min,
            "maxaccessibility": args.accessibility_max,
            "key": args.key,
            "link": args.link,
        }

        random_activity = api_client.get_random_activity(**query_params)

        if random_activity:
            db = FetcherDB("my_activities.db")
            # If you use POSTGRES keep it empty

            activity_description = random_activity.get("activity", "")

            db.insert_activity(
                {
                    "activity": activity_description,
                    "type": args.type,
                    "participants": args.participants,
                    "price": args.price_max,
                    "accessibility": args.accessibility_max,
                    "key": args.key,
                    "link": args.link,
                }
            )

            db.close()

            print("Random Activity:", activity_description)

    elif args.command == "list":
        db = FetcherDB("my_activities.db")  # If you use POSTGRES keep it empty
        recent_activities = db.get_last_activities(5)
        db.close()
        for activity in recent_activities:
            print(activity)


if __name__ == "__main__":
    main()
