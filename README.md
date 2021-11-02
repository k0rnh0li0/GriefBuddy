# GriefBuddy
**ALTERNATIVELY:** You can go to http://k0rnh0l.io/griefbuddy and see the 100 most recently-indexed servers right in your browser. 

You can also go to https://grief.getgle.org to use the Getgle Version of GriefBuddy in your browser!

This script searches Shodan for Minecraft server IPs to grief. This will return all servers connected to the public
internet which Shodan has indexed, regardless of whether or not they have been advertised anywhere. Some will have a whitelist,
but I've found that most don't.

Results are output in the format `<IP>:<PORT>`. IPs will be output ordered by how recently Shodan indexed
them, so results near the top will be "fresher".

## Setup
1. First you need a Shodan API key. Go to https://shodan.io/ and register for a free account. Then go to https://account.shodan.io/, copy
your API key, and paste it between the empty quotes after "API_KEY:" in config.json. Don't share your API key or commit it to
version control!

2. Next, install Python 3 and the pip package manager, if you don't have them.

3. Install the requests library: `$ python3 -m pip install requests`.

4. Clone this repository: `$ git clone https://github.com/k0rnh0li0/GriefBuddy.git`.

5. Edit `config.json` according to your preferences. See section "Configuration" for details. At minimum, you must enter your API key.

6. Run the script: `$ python3 griefbuddy.py`

**NOTE:** Griefing Minecraft servers is *not* illegal. However, be aware that only you, and no one else, are responsible for any
illegal activities you may partake in based on these IP lists. Don't be stupid.

## Configuration
This section documents the settings in `config.json`. It's not necessary to edit `config.json` other than to enter your API key, but you can
change the script's behavior by editing this file.

* `API_KEY` - This must be set. Get your API key from https://account.shodan.io/.
* `PAGES` - How many pages of results to query. Shodan returns 100 results per page. The first page is always free, but querying any pages
beyond the first page will charge you 1 API credit. For example, if you set PAGES to 5, you will be charged 4 API credits total when you
run the script. The first page is usually good enough anyway, it gets updated often as Shodan indexes new servers.
* `MC_VERSION` - Search for a specific Minecraft server version. You can leave this blank, but results may be less reliable and the script
may not work correctly. I recommend having a Minecraft version set.
* `ACTIVE_ONLY` - If you set this to `true`, IPs will only be output if Shodan shows that they have a non-zero Online Players count. This
would be a good way to find servers that people are currently playing on.
* `OUTPUT_FILE` - Leave this blank if you want to display the IP list directly in the terminal. If you set this to a filename, the script will
attempt to write the IP results to the file you specified.

## Contributing
Contributions are welcome in the form of pull requests, issues, and epic grief screenshots in the Discussions tab.

If you open an issue about a bug, it would be helpful to include the contents of your `config.json` file ***WITH YOUR API KEY REDACTED***
so we can figure out what's going on.
