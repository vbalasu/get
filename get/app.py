from chalice import Chalice

app = Chalice(app_name='get')

def read_spreadsheet(spreadsheet_id, sheet_name, credential_file):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, ['https://www.googleapis.com/auth/spreadsheets.readonly'])
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key(spreadsheet_id)
    worksheet = sh.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return data

@app.route('/sheets', cors=True)
def sheets():
    """USAGE: curl "http://127.0.0.1:8000/sheets?spreadsheet_id=1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4&sheet_name=customers" 
              curl "https://get.cloudmatica.com/sheets?spreadsheet_id=1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4&sheet_name=customers" 
              assuming the spreadsheet has been shared with sheets@cloudmatica.iam.gserviceaccount.com """
    credential_file = 'chalicelib/cloudmatica-99fecc8e9b94.json'
    spreadsheet_id = app.current_request.query_params.get('spreadsheet_id')
    sheet_name = app.current_request.query_params.get('sheet_name')
    print(spreadsheet_id, sheet_name, credential_file)
    return read_spreadsheet(spreadsheet_id, sheet_name, credential_file)

@app.route('/', cors=True)
def index():
    """USAGE: curl "http://127.0.0.1:8000?url=https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
              curl "https://get.cloudmatica.com?url=https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" """
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
