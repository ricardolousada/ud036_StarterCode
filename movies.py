import urllib

# Base URL being accessed
url = 'https://api.themoviedb.org/3/search/movie?api_key=a8cb555f0dd72144e16336cb914a68a5&query=Jack+Reacher' # NORA


# Make a GET request and read the response
u = urllib.urlopen(url)
resp = u.read()
print(resp)
#ver como usar json
# estudar a possibilidade de usar o package requests