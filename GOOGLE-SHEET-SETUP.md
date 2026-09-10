# Lead Forms: Email Delivery + Optional Google Sheet

Both forms on the site (the **quote funnel** at `/quote/` and the form at `/contact/`)
send every submission to **BVConsultings@outlook.com**. All settings live at the top of `site.js`.

## 1. Activate email delivery (one time, required)

The forms use [FormSubmit](https://formsubmit.co), a free form-to-email service for static websites.

1. Upload the site to your live domain (https://bvconsulting.live).
2. Go to https://bvconsulting.live/quote/ and submit a test.
3. Check the **BVConsultings@outlook.com** inbox (and the Junk folder) for an email from FormSubmit.
4. Click **Activate Form**. From now on every lead is emailed to you as a clean table.

Tip: submit your tests from the live site, not by double-clicking the HTML file on your computer.

**Optional privacy upgrade:** after activation, FormSubmit gives you a random "alias" string.
Replace the email in `formEndpoint` inside `site.js` with that alias so your address isn't visible in the page code:

```javascript
formEndpoint: "https://formsubmit.co/ajax/your-random-alias-string",
```

## 2. Optional: also log every lead to a Google Sheet

1. Create a Google Sheet named **BV Consulting Leads**.
2. Click **Extensions → Apps Script**, delete anything in the editor, paste the code below, and click **Save**.

```javascript
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    var p = e.parameter;
    // Build the header row automatically from whatever fields arrive.
    var headers = sheet.getLastRow() > 0
      ? sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0]
      : ["Timestamp"];
    Object.keys(p).forEach(function (k) {
      if (headers.indexOf(k) === -1) headers.push(k);
    });
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    var row = headers.map(function (h) { return h === "Timestamp" ? new Date() : (p[h] || ""); });
    sheet.appendRow(row);
    return ContentService.createTextOutput(JSON.stringify({ result: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ result: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

3. Click **Deploy → New deployment → Web app**.
   - Execute as: **Me**
   - Who has access: **Anyone**
4. Click **Deploy**, authorize, and copy the Web app URL (ends in `/exec`).
5. Open `site.js` and paste it into `googleSheetUrl`:

```javascript
googleSheetUrl: "https://script.google.com/macros/s/AKfyc.../exec",
```

Every lead will now be emailed to you **and** added as a new row with columns like
`form, services, practice_type, locations, software, biggest_challenge, name, practice, email, phone, state, city, website, details, page`.

Re-deploy after any script change (**Deploy → Manage deployments → Edit → New version**).

## 3. Optional: Google Analytics 4

Create a GA4 property at analytics.google.com, copy the Measurement ID (looks like `G-XXXXXXXXXX`),
and paste it into `gaId` in `site.js`. The site automatically tracks quote starts (`quote_start`), form leads (`generate_lead`),
thank-you page views (`quote_thank_you_view`), phone clicks (`click_to_call`), and email clicks (`click_email`).
Mark `generate_lead` and `click_to_call` as key events in GA4. For Google or Meta ads, use a visit to `/thank-you/` as your conversion.
