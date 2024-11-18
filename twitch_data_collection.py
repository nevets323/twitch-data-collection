import requests

# Replace these with your actual credentials
CLIENT_ID = '2gxqbk1qse4qrt83vldcslha8gd2p2'
CLIENT_SECRET = '5urudlj12m4d88funqa7uq9n7fvnyd'


def get_twitch_access_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json().get("access_token")


def get_live_streams(access_token, client_id):
    url = "https://api.twitch.tv/helix/streams"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def main():
    try:
        access_token = get_twitch_access_token(CLIENT_ID, CLIENT_SECRET)
        live_streams = get_live_streams(access_token, CLIENT_ID)
        print("Live Streams Data:")
        print(live_streams)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

