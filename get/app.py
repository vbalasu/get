from chalice import Chalice

app = Chalice(app_name='get')


@app.route('/', cors=True)
def index():
    """USAGE: curl "http://127.0.0.1:8000?url=https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" """
    url = app.current_request.query_params.get('url')
    if url is None:
        return 'Missing url'
    else:
        print(url)
        import requests
        try:
            response = requests.get(url)
        except:
            return 'Error fetching data. Please check the url.'
        return {'content': response.content.decode(), 'headers': dict(response.headers), 'status_code': response.status_code}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
