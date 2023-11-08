async function readSpreadsheet(spreadsheetId, sheetName) {
    const axios = require('axios');
    var response = await axios.get(`https://get.cloudmatica.com/sheets?spreadsheet_id=${spreadsheetId}&sheet_name=${sheetName}`);
    console.log(response);
}

readSpreadsheet('1pYY4glskbi8RMXXPaH4SGJI5O-J_tXzAq1uImt2siv4', 'customers');