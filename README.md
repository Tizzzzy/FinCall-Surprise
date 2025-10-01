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
- `ppt_id`: (String) The unique identifier for the corresponding presentation slides, located in the ppt_YYYY folder. The full filename is [ppt_id].pptx.
- `label`: (Integer) The ground-truth label for the data sample (e.g., 0 or 1).

## 📢 Data Availability Notice

Please note: Currently, only the data for 2019 (transcripts, mp3, and ppt files) is partially available. The complete multimodal data, including the corresponding mp3 and ppt files, will be released publicly upon acceptance of our work.

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
ppt_file_path = os.path.join(PPT_FOLDER, f"{ppt_id}.pptx")

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
