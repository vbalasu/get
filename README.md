# get

Simple mechanism to fetch information from the web, consisting of:

1. An AWS Lambda (chalice) serverless endpoint at https://get.cloudmatica.com that proxies requests
2. A Javascript client that uses this endpoint

```
USAGE: curl "http://127.0.0.1:8000?url=https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
              curl "https://get.cloudmatica.com?url=https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" 
```

You can also fetch data from Google Spreadsheets

```
USAGE: curl "http://127.0.0.1:8000/sheets?spreadsheet_id=1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4&sheet_name=customers" 
              curl "https://get.cloudmatica.com/sheets?spreadsheet_id=1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4&sheet_name=customers" 
              assuming the spreadsheet has been shared with sheets@cloudmatica.iam.gserviceaccount.com
```

Use the same Javascript in NodeJS and the browser by using a conditional require as follows:
```
if(typeof window == 'undefined') var axios = require('axios');   // Applies only to Node.js. Use CDN in index.html
```

[index.html](./index.html)