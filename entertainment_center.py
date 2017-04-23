import requests
import movies
import json
import fresh_tomatoes

''' The movies_to_search_array contains the movies that will be presented in
    the we page. New films can be added if the array sintax is respected.
    Film names can also be changed. '''

movies_to_search = ["Godfather","Pulp Fiction","Reservoir Dogs",
                    "First Blood","Magnolia","Django Unchained"]

movies_array = [] # final array to call fre"Magnolia"sh_tomatoes

# API URL's to search a film details, poster and video
base_url = 'https://api.themoviedb.org/3/search/movie?api_key={key}&query='
API_KEY='a8cb555f0dd72144e16336cb914a68a5'
url_with_key=base_url.format(key=API_KEY)
poster_url='http://image.tmdb.org/t/p/original/'
you_tube = 'https://www.youtube.com/watch?v='

def load_movie(url):
    '''creates a movie instance with information fectechd by the API'''

    payload = "{}"
    payload2 = "{}"
    # cals the API to fetch the movie information
    response = requests.request("GET", url, data=payload)
    # converts the response object into json format
    json_data = response.json()
    # formats data in urls to fecth posters and you_tube_url for trailers
    complete_poster_path=poster_url+json_data["results"][0]["poster_path"]
    id=json_data["results"][0]["id"]
    trailer_url='http://api.themoviedb.org/3/movie/{id}/videos?api_key={key}'
    movie_trailer_url=trailer_url.format(id=id,key=API_KEY)
    # calls the API a second time to get the youtube key for trailers
    response2=requests.request("GET",movie_trailer_url,data=payload2)
    json_data_youtube=response2.json()
    you_tube_url=you_tube + json_data_youtube["results"][0]["key"]
    # creates the movie instance
    movie_information = movies.Movie(json_data["results"][0]["title"],
                        json_data["results"][0]["overview"],
                        complete_poster_path,
                        you_tube_url,
                        json_data["results"][0]["vote_average"])
    # adds a movie to the movies array
    movies_array.append(movie_information)

# cicles the movies_to_search array and calls load_movies function for each film
for movie in movies_to_search:

    # Replaces blanks by "+" to use in the search
    movie_string_to_search = movie.replace(' ','+')
    url = url_with_key + movie_string_to_search
    # call the function to fecth movie information and creates the movie object
    load_movie(url)

# calls the fuction that creates the dinamyc web page
fresh_tomatoes.open_movies_page(movies_array)










