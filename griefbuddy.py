#!/usr/bin/env python3
#
# griefbuddy.py
# k0rnh0li0 2021
#
# Search Shodan for all Minecraft server IPs connected
# to the public internet, for the lulz.
# This program is Free Software, licensed under the
# terms of GNU GPLv3. See LICENSE.txt for details.

import requests
import json

# Shodan search query endpoint
API_URL = "https://api.shodan.io/shodan/host/search"

# results per page
PAGE_SIZE = 100

# user config loaded from config.json
CONFIG = {}


def do_request(page_num):
    # construct API request
    api_params = {
        "key": CONFIG["API_KEY"],
        "page": page_num,
        "query": "Minecraft"
    }

    if CONFIG["MC_VERSION"] != "":
        api_params["query"] = "Minecraft " + CONFIG["MC_VERSION"]

    result = requests.get(API_URL, params=api_params)

    if result.status_code == 401:
        print("Error 401 from Shodan, your API key is most likely incorrect.")
        print("Go to https://account.shodan.io/ and copy the API key into")
        print("your config.json correctly.")
        exit()

    result = result.json()
    if "error" in result:
        # API call returned an error
        print("SHODAN ERROR: " + result["error"])
        return None

    return result


def parse_page(page_json):
    result = []
    for server in page_json["matches"]:
        if CONFIG["ACTIVE_ONLY"]:
            if "Online Players: 0" in server["data"]:
                continue

        ip = server["ip_str"]
        port = str(server["port"])
        result.append(ip + ":" + port)
    return result


def print_ips(ips):
    if CONFIG["OUTPUT_FILE"] == "":
        # print results to stdout
        for ip in ips:
            print(ip)
    else:
        try:
            with open(CONFIG["OUTPUT_FILE"], "w") as f:
                for ip in ips:
                    f.write(ip + "\n")
        except Exception as e:
            print("Failed to open output file!")
            print(e)
            exit()


if __name__ == "__main__":
    print("GriefBuddy 2021")
    print("I AM THE GREAT K0RNH0LI0!")
    print("https://twitter.com/gr8_k0rnh0li0\n")

    try:
        with open("config.json") as f:
            CONFIG = json.loads(f.read())
    except Exception as e:
        print("Failed to load config.json!")
        print(e)
        exit()

    if CONFIG["API_KEY"] == "":
        print("API_KEY must be set!")
        print("Create a free account at https://shodan.io/ and")
        print("put your API key in config.json.")
        exit()

    page_range = CONFIG["PAGES"]
    if isinstance(page_range, int) and page_range < 1:
        print("PAGES must be greater than 0.")
        exit()

    print("Searching for servers...")

    # parse the provided page range as an inclusive range
    lower_page = -1
    upper_page = -1
    if isinstance(page_range, int):
        lower_page = 1
        upper_page = page_range
    else:  # assume a range is given as a string
        lower_page, upper_page = [int(x) for x in page_range.split("-")]

    for i in range(lower_page, upper_page + 1):
        resp = do_request(i)

        if resp is not None:
            ips = parse_page(resp)
            print_ips(ips)  # print ips on the go in case of an error
