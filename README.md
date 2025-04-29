# Oh Snap Party Aggregator

This project aggregates attendee data across multiple Google Sheets stored in structured Google Drive folders.  
It builds a unified dataset for analyzing party participation, arrival behavior, song preferences, and audience trends over time, with ML and statistical enhancement capabilities.

---

## 📑 Table of Contents

- [🚀 How It Works](#-how-it-works)
- [📦 Folder and File Structure](#-folder-and-file-structure)
- [🛠️ Google Apps Script Setup](#️-google-apps-script-setup)
- [🧪 Features Implemented](#-features-implemented)
- [📈 Machine Learning and Data Science Extensions](#-machine-learning-and-data-science-extensions)
- [🛤️ Planned Enhancements](#-planned-enhancements)
- [📚 Future Fun Ideas](#-future-fun-ideas)
- [⚙️ Tech Stack](#-tech-stack)

---

## 🚀 How It Works

1. **Google Drive Integration**:
   - Authenticate using a Service Account.
   - Find all Google Sheets inside one-level subfolders of a given root folder.

2. **Google Apps Script Highlight Detection**:
   - A small Google Apps Script automatically scans each sheet for highlighted (painted) cells.
   - Detected highlights are marked into a new `arrived_marker` column.
   - If the participant manually marked 'arrived' but no highlight exists, the script updates `arrived_marker` to `"true"`.

3. **Data Caching**:
   - Fetched sheet data is cached locally to avoid redundant API calls.

4. **Data Cleaning**:
   - Merges columns containing partial names into a unified `full_name` field.
   - Merges song requests and special notes into clean fields.
   - Drops empty or irrelevant columns.

5. **Data Consolidation**:
   - Combines all parties' data into a single Pandas DataFrame.
   - Adds metadata like `file_id`, `folder_name`, `timestamp`.
   - Merges manual and highlight-based arrival detections.

6. **Data Science Enhancements**:
   - Applies Exploratory Data Analysis (EDA).
   - Tests behavioral hypotheses.
   - Builds predictive ML models.
   - Runs NLP over song requests and special notes.

---

## 📦 Folder and File Structure

- **Root Google Drive Folder**: Contains one level of subfolders (each representing a party date).
- **Inside Each Subfolder**: One or more Google Sheets (`.gsheet`) containing party participant data.
- **Local Cache File**: `cache.json` caching parsed Sheets to speed up reprocessing.

---

## 🛠️ Google Apps Script Setup

In order to detect painted cells inside Google Sheets:

1. Open [Google Apps Script](https://script.google.com/home) ➔ Create New Project.
2. Paste the following key functions:
   - `processAllSheetsFromList()` (to loop over all your file IDs).
   - `markFirstHighlightedCellColor(spreadsheet)` (to detect highlights and mark colors).
3. Share all party files with your Google account if needed.
4. Run `processAllSheetsFromList` manually once.
5. Grant necessary permissions (Drive + Spreadsheet access).

**Result:**  
All party Sheets will have an `arrived_marker` column:
- **If painted:** first detected color code (`#ffff00`, etc.).
- **If arrived manually (text only):** `"true"`.
- **If neither:** defaults to `#ffffff`.

---

## 🧪 Features Implemented

- [x] Google Drive integration to list Google Sheets
- [x] Data caching locally for development speed
- [x] Google Apps Script highlight detection (`arrived_marker`)
- [x] Merge partial names and notes into clean fields
- [x] Remove empty/irrelevant columns
- [x] Unified DataFrame of all parties
- [x] Count and analyze participant appearances
- [x] Arrival detection from color or manual fields

---

## 📈 Machine Learning and Data Science Extensions

| Task | Method | Status |
|------|--------|--------|
| **Top 10 Participants** | pandas value_counts | Planned |
| **Arrival Frequency Analysis** | pandas groupby, aggregation | Planned |
| **Hypothesis Testing: Requesters vs Non-Requesters** | Chi-Square Test (scipy) | Planned |
| **Arrival Prediction Model** | Logistic Regression (sklearn) | Planned |
| **Guest Loyalty Clustering** | KMeans (sklearn) | Planned |
| **Bag-of-Words on Song Requests** | TF-IDF Vectorization (sklearn) | Planned |
| **Sentiment Analysis of Notes** | TextBlob, VADER | Planned |
| **Heatmaps of Attendance** | seaborn heatmap | Planned |

---

## 🛤️ Planned Enhancements

- [ ] **Transpose the Final DataFrame**: Names as rows, party folders as columns for arrival tracking.
- [ ] **Build ML Classifiers**: Predict next arrival based on engagement.
- [ ] **Sentiment Analysis**: Analyze emotional tone of free-text notes.
- [ ] **Bag-of-Words Modeling**: Extract dominant topics from song requests.
- [ ] **Returning vs New Audience Analysis**: Loyalty tracking per participant.
- [ ] **Heatmaps and Dashboards**: Visualize party attendance and sentiment trends.
- [ ] **Automatic Re-run Triggers**: Google Apps Script timed auto-update.

---

## 📚 Future Fun Ideas

- 🎵 Most requested song prediction.
- 😃 Crowd mood prediction based on party notes.
- 🧠 Predict attendance churn using survival analysis.
- 📈 Build a public dashboard for viewing dynamic party metrics.
- 🔮 Predict next week's likely attendance volume based on historical patterns.

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **pandas** — Data manipulation and analysis
- **gspread + gspread_dataframe** — Google Sheets interaction
- **google-api-python-client** — Google Drive API
- **openpyxl** — Excel file handling
- **python-dotenv** — Environment variable loading
- **Google Apps Script** — Spreadsheet highlight detection
- **scikit-learn** — ML models (Logistic Regression, Clustering)
- **scipy** — Statistical tests (Chi-square, T-tests)
- **nltk / textblob / VADER** — Natural Language Processing
- **seaborn / matplotlib** — Visualization
- **Streamlit** *(planned)* — Dashboard UI

---

## 📊 Pipeline Overview (System Architecture)
[Google Drive Folder with Party Sheets]
            |
            v
[Google Apps Script]
   - Detects highlighted arrivals
   - Marks 'arrived_marker' column (#ffff00, true, etc.)
            |
            v
[Local Python Aggregation]
   - gspread reads Sheets
   - pandas processes names, dates, markers
   - Merges party data into unified DataFrame
            |
            v
[Data Science Layer]
   - Clean DataFrame
   - Hypothesis Testing
   - Regression / Correlation analysis
   - ML modeling on participation, preferences
            |
            v
[Insights and Outputs]
   - Attendance trends
   - Returning vs new guest behavior
   - Popular song prediction
   - Sentiment analysis of free-text fields
   - Dashboards / Reporting