# Oh Snap Party Aggregator

This project aggregates attendee data across multiple Google Sheets stored in structured Google Drive folders.  
It builds a unified dataset for analyzing party participation, special requests, and audience trends over time.

## 🚀 How It Works

1. **Google Drive Integration**:
   - Authenticate using a Service Account.
   - Find all Google Sheets inside one-level sub-folders of a given root folder.

2. **Data Caching**:
   - Fetched sheet data is cached locally to avoid redundant API calls.

3. **Data Cleaning**:
   - Merges columns containing partial names into a unified `full_name` field.
   - Merges special song requests and notes into consistent columns.
   - Drops empty or irrelevant columns.

4. **Data Consolidation**:
   - Combines all parties' data into a single Pandas DataFrame.
   - Adds metadata like `file_id` and `folder_name` for tracking.

## 📦 Folder and File Structure

- **Root Google Drive Folder**: One depth of subfolders (each representing a party).

- **Inside Each Subfolder**: One or more Google Sheets (`.gsheet`) containing party participant data.

## 🧪 Features Implemented

- [x] List and fetch Google Sheets from Drive
- [x] Cache data locally for faster development
- [x] Merge partial name columns
- [x] Merge free-text fields (song requests, special notes)
- [x] Remove empty and irrelevant columns
- [x] Create a unified attendance DataFrame

## 🛤️ Planned Enhancements

- [ ] Transpose the final DataFrame: **names as rows, party folders as columns**
- [ ] Highlight arrivals using Google Sheets markers (`arrived` field detection)
- [ ] Build **ML Bag-of-Words** models for analyzing song requests (e.g., word clouds, topic modeling)
- [ ] Perform **Sentiment Analysis** on special request texts (e.g., happy/sad themes)
- [ ] Calculate **returning vs. new participants** across parties and overall trends

## 📚 Future Fun Ideas

- 🎵 Most requested song prediction
- 😃 Crowd mood analysis by sentiment across months
- 🧠 Predict audience size based on past special requests

## ⚙️ Tech Stack

- Python 3.10+
- pandas
- gspread + gspread_dataframe
- google-api-python-client
- openpyxl
- dotenv

### ✅ Must-Have Next Steps
 **Transpose Meta Table** | Names in rows, party dates in columns | Required to track attendance over time |
 **Mark `arrived`** | Extract from color/marker manually or via Apps Script | To correctly analyze who actually arrived |
 **Robust Caching by Timestamp** | Invalidate cache if Google Sheet is updated (optional) | Avoid stale data in cache |

---

### 🎯 Nice-to-Have Enhancements
 **Bag-of-Words for Song Requests**  NLP feature extraction (`sklearn` `CountVectorizer`) | Understand most common themes |
 **Sentiment Analysis** | Use `textlob` / `transformers` to classify special requests | Measure emotional content |
 **New vs Returning Audience Analyis** | Compare names across parties using set operations | Identify loyal participants vs first-timers |
 **Heatmaps** | Attendance heatmap (person × party matrix) | Visualize loyalty and absences |
 **Streamlit Dashboard** | UI for viewing attendance trends | Make it interactive and shareable |
 **Logging**: Use `logging` modul instead of `print()` for debug logs.
 **Progress Bar**: Add `tqdm` toshow progress on large folders.
 **Test Suite**: Add basic `pytst` for key logic (e.g., merge columns).
