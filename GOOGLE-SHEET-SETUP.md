# Connecting the Quote Form to Google Sheets

The quote form on `quote.html` works out of the box as a demo (loading bar, confetti, and the success popup all run). To actually **save each submission into a Google Sheet**, follow these one-time steps.

## 1. Create the sheet
1. Go to [sheets.google.com](https://sheets.google.com) and create a new spreadsheet.
2. Name it something like **BV Consulting Quotes**.
3. In **row 1**, add these column headers, one per cell (left to right):

```
Timestamp | service | device | who | urgency | location | name | phone | email | details
```

## 2. Add the Apps Script
1. In the sheet, click **Extensions → Apps Script**.
2. Delete anything in the editor and paste the code below.
3. Click **Save** (disk icon).

```javascript
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    var p = e.parameter;
    sheet.appendRow([
      new Date(),
      p.service || "",
      p.device || "",
      p.who || "",
      p.urgency || "",
      p.location || "",
      p.name || "",
      p.phone || "",
      p.email || "",
      p.details || ""
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ result: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

## 3. Deploy it as a Web App
1. Click **Deploy → New deployment**.
2. Click the gear icon → choose **Web app**.
3. Set:
   - **Description:** BV Quote Form
   - **Execute as:** Me
   - **Who has access:** **Anyone**
4. Click **Deploy**, authorize when prompted, and **copy the Web app URL** (it ends in `/exec`).

## 4. Paste the URL into the site
1. Open `quote.html` in a text editor.
2. Near the bottom, find this line:

```javascript
var GOOGLE_SCRIPT_URL = ""; // <-- paste your Apps Script Web App URL here
```

3. Paste your URL between the quotes:

```javascript
var GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfyc.../exec";
```

4. Save and re-upload the file to your web host.

That's it. Every quote submission now appends a new row to your Google Sheet, while the visitor still sees the loading bar, confetti, and success popup.

## Optional: also save contact-page messages
The contact form in `contact.html` can use the **same** Apps Script URL. Open `contact.html`, find the comment in the submit handler, and add a matching `fetch()` call (the data fields would be `name`, `phone`, `email`, `message`).

## Optional: get an email for every submission
Add this line inside `doPost`, right after `sheet.appendRow(...)`:

```javascript
MailApp.sendEmail("bvconsultings@outlook.com", "New Quote Request",
  "Name: " + p.name + "\nPhone: " + p.phone + "\nEmail: " + p.email +
  "\nService: " + p.service + "\nDetails: " + p.details);
```

Re-deploy after any change (**Deploy → Manage deployments → Edit → New version**).
