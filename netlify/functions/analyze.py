
import requests
from collections import Counter

def get_holder_clusters(token_address):
    url = f"https://public-api.solscan.io/token/holders?tokenAddress={token_address}&limit=1000"
    headers = {"accept": "application/json"}
    res = requests.get(url, headers=headers)
    holders = res.json()
    total_supply = sum(float(holder["amount"]) for holder in holders)

    percentages = [round(float(holder["amount"]) / total_supply * 100, 2) for holder in holders]
    clusters = Counter(percentages)
    return [f"{p:.2f}%" for p, c in clusters.items() if c >= 3]

def handler(event, context):
    try:
        import json
        body = json.loads(event["body"])
        token_address = body.get("token")

        same_buys = get_holder_clusters(token_address)
        suspicious_wallets = ["FakeWallet1", "FakeWallet2"]
        volume = 12345
        snipers = ["Sniper1", "Sniper2"]
        chart_url = "https://cdn.devbot.net/chart.png"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "volume": volume,
                "suspicious_wallets": suspicious_wallets,
                "same_buys": same_buys,
                "snipers": snipers,
                "chart_url": chart_url
            }),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
