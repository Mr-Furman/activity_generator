import requests


class BoredAPIFetcher:
    BASE_URL = "https://www.boredapi.com/api/activity"

    def get_random_activity(
        self,
        type=None,
        participants=None,
        price=None,
        link=None,
        key=None,
        accessibility=None,
        minprice=None,
        maxprice=None,
        minaccessibility=None,
        maxaccessibility=None,
    ):
        params = {
            "type": type,
            "participants": participants,
            "price": price,
            "link": link,
            "key": key,
            "accessibility": accessibility,
            "minprice": minprice,
            "maxprice": maxprice,
            "minaccessibility": minaccessibility,
            "maxaccessibility": maxaccessibility,
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch an activity from the API.")
            return None
