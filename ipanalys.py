import requests
import socket

class urlsAnalysis:
    def init(self, filename):
        self.urls = []
        with open(filename, 'r') as f:
         for line in f:
          self.urls.append(line.strip())
    def chklinks(self, output_file='links_txt.txt'):
        links = []
        for url in self.urls:
            try:
                req = requests.get(url)
                if req.status_code == 200:
                    html = req.text
                    start = 0
                    while True:
                        start = html.find('href=', start)
                        if start == -1:
                            break
                        start += 6
                        end = html.find('"', start)
                        link = html[start:end]
                        if link.startswith('http') and link not in links:
                            links.append(link)
            except:
                pass
        with open(output_file, 'w') as f:
            for link in links:
                f.write(link + '\n')

    def chkip(self, output_file='iploc.txt'):
        ips = []
        for url in self.urls:
            try:
                addr = socket.gethostbyname(url)
                if addr not in ips:
                    ips.append(addr)
            except:
                pass
        locations = []
        for ip in ips:
            try:
                req = requests.get('https://ipinfo.io/' + ip + '/json')
                if req.status_code == 200:
                    data = req.json()
                    location = data['city'] + ', ' + data['region'] + ', ' + data['country']
                    locations.append(location)
            except:
                pass
        with open(output_file, 'w') as f:
            for location in locations:
                f.write(location + '\n')
urls = urlsAnalysis('urls.txt')
urls.chklinks()
urls.chkip()