// Took painted cells in marker from the google sheets and create a new column with the color (with google app scripts)
// This script processes all spreadsheets ids listed in the cached sheets.

function processAllSheetsFromCache() {
  const fileIds = ['file_id_1', 'file_id_2']; // Replace with your actual file IDs

  fileIds.forEach((fileId) => {
    try {
      const spreadsheet = SpreadsheetApp.openById(fileId);
      markHighlightedRows(spreadsheet);
    } catch (error) {
      Logger.log(`Failed to process file ${fileId}: ${error}`);
    }
  });
}

function markHighlightedRows(spreadsheet) {
  const sheet = spreadsheet.getSheets()[0];
  const range = sheet.getDataRange();
  const backgrounds = range.getBackgrounds();
  const values = range.getValues();

  const headerRow = values[0];

  let markerCol = headerRow.indexOf("arrived_marker");

  if (markerCol === -1) {
    markerCol = headerRow.length;
    sheet.getRange(1, markerCol + 1).setValue("arrived_marker");
  }

  for (let row = 1; row < backgrounds.length; row++) {
    let rowBackgrounds = backgrounds[row];
    let highlighted = false;

    for (let col = 0; col < rowBackgrounds.length; col++) {
      if (
        rowBackgrounds[col] !== "#ffffff" &&
        rowBackgrounds[col] !== "#000000"
      ) {
        highlighted = true;
        break;
      }
    }

    const markerValue = highlighted ? "highlighted" : "none";
    sheet.getRange(row + 1, markerCol + 1).setValue(markerValue);
  }
}
