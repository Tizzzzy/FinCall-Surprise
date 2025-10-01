# FinCall-Surprise

This repository contains financial earnings call data including transcripts, audio files (MP3), and presentation slides (PDF) for the years 2019, 2020, and 2021.

## Directory Structure
Our repo is organized in the following structure:
```
├── mp3_2019/
│   ├── 1079252536.mp3
│   └── ... (other mp3 files)
├── ppt_2019/
│   ├── 1000019806.pdf
│   └── ... (other pdf files)
├── transcripts_2019.json
├── transcripts_2020.json
├── transcripts_2021.json
└── ... (data for years 2020 and 2021 follow the same pattern)
```

## JSON File Structure

Each JSON file (e.g., `transcripts_2019.json`) contains earnings call data organized as a dictionary where:
- **Key**: A unique identifier for each earnings call entry
- **Value**: A dictionary with the following fields:

### Fields Description

| Field | Type | Description |
|-------|------|-------------|
| `input` | string | The full text transcript of the earnings call |
| `mp3_id` | string | The identifier for the corresponding MP3 audio file |
| `ppt_id` | string | The identifier for the corresponding presentation PDF file |
| `label` | integer | Ground truth label (0 or 1) indicating the earnings surprise classification |

### Example JSON Entry

```json
{
  "1630481": {
    "input": "Executives: Thank you. Good morning, everybody, and thanks for joining our call today...",
    "mp3_id": "567143602",
    "ppt_id": "568299786",
    "label": 1
  }
}
```

**Note**: Not all entries have corresponding MP3 and PDF files in the folders. The JSON files contain 900+ entries, but the mp3 and ppt folders contain only a subset of files.

## Usage

See `load_data_example.py` for a complete example of how to load the data and map transcripts to their corresponding audio and presentation files.
