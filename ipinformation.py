import socket

# Open the input file and read the content
with open("urls.txt", "r") as inp_file:
    urls = inp_file.readlines()

# Open the output file for writing
with open("iploc.txt", "w") as out_file:
    # Loop through each URL
    for url in urls:
        # Remove any extra spaces and newlines
        url = url.strip()
        # Use the socket library to get the IP address for the URL
        try:
            ip = socket.gethostbyname(url)
        except:
            ip = 'unknown'
        # Use the API to get the location information for the IP
        # Here you need to use a location API, such as: ipwhois, ipinfo, etc.
        location = 'unknown'
        # Write the URL, IP, and location information to the output file
        out_file.write(f"{url},{ip},{location}\n")
