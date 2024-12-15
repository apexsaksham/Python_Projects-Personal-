import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Cat Fact: {data['fact']}")
    else:
        print("Failed to fetch cat fact.")

# Run the function
get_cat_fact()
