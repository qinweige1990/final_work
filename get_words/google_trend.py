from apify_client import ApifyClient




def get_google_trend():
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_cgdkO2Br3SILtjnJlG9DbKFheZdzON37DMHK")

    # Prepare the Actor input
    run_input = {
        "geo": "US",
        "outputMode": "complete",
        "fromDate": "today",
        "toDate": "3 days",
        "maxItems": 100,
        "proxy": { "useApifyProxy": True },
        "extendOutputFunction": """async ({ data, item, request, customData, fromDate, toDate, Apify }) => {
      return item;
    }""",
        "extendScraperFunction": """async ({ data, item, request, addUrl, customData, fromDate, toDate, extendOutputFunction, Apify }) => {
     
    }""",
        "customData": {},
    }

    # Run the Actor and wait for it to finish
    run = client.actor("49HfNLFgg6B8YetTj").call(run_input=run_input)
    words = []
    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        words.append(item.get("query", "empty"))
    return words