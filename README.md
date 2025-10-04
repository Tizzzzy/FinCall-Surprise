# FinCall-Surprise
This is the official repo for paper: "FinCall-Surprise: A Large-Scale Multi-modal Benchmark for Earning Surprise Prediction"

## Directory Structure
Our repo is organized in the following structure:
```
├── mp3_2019/
│   ├── 1630481.mp3
│   └── ... (other mp3 files)
├── ppt_2019/
│   ├── 1630481.ppt
│   └── ... (other ppt files)
├── transcripts_2019.json
├
└── ... (data for year 2020 and 2021)
```

## JSON File Structure
Each JSON file is a dictionary where the keys are unique Call IDs. Each Call ID maps to an object containing the full transcript and metadata needed to link to the corresponding audio and slide files.

Here is a breakdown of the structure for a single entry:

```json
{
    "call_id": {
        "input": "Executives: Thank you. Good morning, everybody...",
        "mp3_id": "567143602",
        "ppt_id": "568299786",
        "label": 1
    },
    ...
}
```
- `input`: (String) The full text transcript of the earnings call.
- `mp3_id`: (String) The unique identifier for the corresponding MP3 audio file, located in the mp3_YYYY folder. The full filename is [mp3_id].mp3.
- `ppt_id`: (String) The unique identifier for the corresponding presentation slides, located in the ppt_YYYY folder. The full filename is [ppt_id].pdf.
- `label`: (Integer) The ground-truth label for the data sample (e.g., 0 or 1).

## 📢 Full Dataset Download

Please note: This GitHub repository contains all the conference call text transcripts (in json) but only a small sample of the large MP3 and PPT files for 2019 to keep the repository lightweight.

The complete multimodal dataset (all MP3 and PPT files for 2019-2021) is hosted on Google Drive due to its size. Download from [here](https://drive.google.com/drive/folders/1gdoRW2jhHQzabyzuCdJMGECUhw5eZ2-6?usp=sharing).

To ensure the code works correctly, follow these steps after downloading:
1. Download all the .zip files from the Google Drive link.
2. Unzip each file (e.g., mp3_2019.zip, ppt_2019.zip, etc.).
3. Place the resulting folders (mp3_2019, ppt_2019, etc.) in the root of this project directory, so they are alongside the transcripts_YYYY.json files.

## Usage Example

Below is a Python script demonstrating how to load the JSON file and map each entry to its associated transcript, file paths, and label.

``` python
import json
import os

# --- Configuration ---
# Change this to the year you want to process
YEAR = 2019

JSON_FILE = f"transcripts_{YEAR}.json"
MP3_FOLDER = f"mp3_{YEAR}"
PPT_FOLDER = f"ppt_{YEAR}"

# --- Load the JSON data ---
try:
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✅ Successfully loaded {len(data)} entries from {JSON_FILE}")
except FileNotFoundError:
    print(f"❌ Error: '{JSON_FILE}' not found. Please make sure the file is in the correct directory.")
    exit()

# --- Process and Map Data ---
# Get the first call ID from the dataset as an example
example_call_id = list(data.keys())[0]
print(f"\n--- Processing Example Entry (Call ID: {example_call_id}) ---")

# Extract the data for this specific call
call_data = data[example_call_id]

# 1. Get the text transcript
text_transcript = call_data.get("input")

# 2. Construct the MP3 file path
mp3_id = call_data.get("mp3_id")
mp3_file_path = os.path.join(MP3_FOLDER, f"{mp3_id}.mp3")

# 3. Construct the PPT file path
ppt_id = call_data.get("ppt_id")
ppt_file_path = os.path.join(PPT_FOLDER, f"{ppt_id}.pdf")

# 4. Get the ground truth label
ground_truth = call_data.get("label")

# --- Display the final variables ---
print(f"\nFinal variables for Call ID {example_call_id}:")
print(f"\n1. Text Transcript (first 100 chars):")
print(f"   '{text_transcript[:100]}...'")

print(f"\n2. MP3 File Path:")
print(f"   '{mp3_file_path}'")

print(f"\n3. PPT File Path:")
print(f"   '{ppt_file_path}'")

print(f"\n4. Ground Truth Label:")
print(f"   {ground_truth}")

# You can now loop through all items in `data.items()` to process the entire dataset.
# for call_id, call_data in data.items():
#     # ... repeat the process above for each call
```
