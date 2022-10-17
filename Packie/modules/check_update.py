import urllib.request

url = 'https://raw.githubusercontent.com/st-stratus/packie/main/VERSION.txt'
version = urllib.request.urlopen(url).read().decode('utf-8')
f = open('version.txt', 'r')
legacy_version = f.read()
f.close()

if not version == legacy_version:
    update = True
elif version == legacy_version:
    update = False