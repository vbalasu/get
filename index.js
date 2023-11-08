if(typeof window == 'undefined') var axios = require('axios');   // Applies only to Node.js. Use CDN in index.html

async function readSpreadsheet(spreadsheetId, sheetName) {
    var response = await axios.get(`https://get.cloudmatica.com/sheets?spreadsheet_id=${spreadsheetId}&sheet_name=${sheetName}`);
    console.log(response);
    return response;
}

async function readPage(url) {
    var response = await axios.get(`https://get.cloudmatica.com?url=${url}`);
    console.log(response);
    return response;
}

readSpreadsheet('1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4', 'customers');
//readPage('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population');