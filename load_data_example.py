"""
Example script demonstrating how to load FinCall-Surprise data.

This script shows how to:
1. Load the JSON transcript file
2. Map each entry's mp3_id and ppt_id to the actual file paths
3. Extract the four key variables:
   - text transcript
   - ppt file path
   - mp3 file path
   - ground truth label
"""

import json
import os
from pathlib import Path


def load_fincall_data(json_path, mp3_folder, ppt_folder):
    """
    Load financial call data and map to file paths.
    
    Args:
        json_path (str): Path to the JSON transcript file (e.g., 'transcripts_2019.json')
        mp3_folder (str): Path to the folder containing MP3 files (e.g., 'mp3_2019')
        ppt_folder (str): Path to the folder containing PDF files (e.g., 'ppt_2019')
    
    Returns:
        list: List of dictionaries, each containing:
            - 'call_id': Unique identifier for the earnings call
            - 'transcript': Text transcript of the earnings call
            - 'mp3_path': Path to the MP3 file (None if file doesn't exist)
            - 'ppt_path': Path to the presentation PDF file (None if file doesn't exist)
            - 'ground_truth': Ground truth label (0 or 1)
    """
    # Load the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get available MP3 and PDF files
    mp3_files = {}
    if os.path.exists(mp3_folder):
        for filename in os.listdir(mp3_folder):
            if filename.endswith('.mp3'):
                file_id = filename.replace('.mp3', '')
                mp3_files[file_id] = os.path.join(mp3_folder, filename)
    
    ppt_files = {}
    if os.path.exists(ppt_folder):
        for filename in os.listdir(ppt_folder):
            if filename.endswith('.pdf'):
                file_id = filename.replace('.pdf', '')
                ppt_files[file_id] = os.path.join(ppt_folder, filename)
    
    # Process each entry
    processed_data = []
    for call_id, entry in data.items():
        # Extract the four key variables
        transcript = entry['input']
        mp3_id = entry['mp3_id']
        ppt_id = entry['ppt_id']
        ground_truth = entry['label']
        
        # Map IDs to file paths
        mp3_path = mp3_files.get(mp3_id, None)
        ppt_path = ppt_files.get(ppt_id, None)
        
        processed_data.append({
            'call_id': call_id,
            'transcript': transcript,
            'mp3_path': mp3_path,
            'ppt_path': ppt_path,
            'ground_truth': ground_truth
        })
    
    return processed_data


def main():
    """
    Example usage of the load_fincall_data function.
    """
    # Example: Load 2019 data
    json_path = 'transcripts_2019.json'
    mp3_folder = 'mp3_2019'
    ppt_folder = 'ppt_2019'
    
    print(f"Loading data from {json_path}...")
    data = load_fincall_data(json_path, mp3_folder, ppt_folder)
    
    print(f"\nTotal entries loaded: {len(data)}")
    
    # Count entries with available files
    entries_with_mp3 = sum(1 for entry in data if entry['mp3_path'] is not None)
    entries_with_ppt = sum(1 for entry in data if entry['ppt_path'] is not None)
    entries_with_both = sum(1 for entry in data if entry['mp3_path'] is not None and entry['ppt_path'] is not None)
    
    print(f"Entries with MP3 files: {entries_with_mp3}")
    print(f"Entries with PDF files: {entries_with_ppt}")
    print(f"Entries with both files: {entries_with_both}")
    
    # Display first entry as example
    if data:
        print("\n" + "="*80)
        print("EXAMPLE ENTRY:")
        print("="*80)
        example = data[0]
        print(f"Call ID: {example['call_id']}")
        print(f"Transcript (first 200 chars): {example['transcript'][:200]}...")
        print(f"MP3 Path: {example['mp3_path']}")
        print(f"PPT Path: {example['ppt_path']}")
        print(f"Ground Truth Label: {example['ground_truth']}")
    
    # Example: Access the four key variables for each entry
    print("\n" + "="*80)
    print("ACCESSING THE FOUR KEY VARIABLES:")
    print("="*80)
    
    for i, entry in enumerate(data[:3]):  # Show first 3 entries
        print(f"\nEntry {i+1} (Call ID: {entry['call_id']}):")
        
        # Variable 1: Text transcript
        transcript = entry['transcript']
        print(f"  1. Text Transcript: {len(transcript)} characters")
        
        # Variable 2: PPT file path
        ppt_file_path = entry['ppt_path']
        print(f"  2. PPT File Path: {ppt_file_path if ppt_file_path else 'Not available'}")
        
        # Variable 3: MP3 file path
        mp3_file_path = entry['mp3_path']
        print(f"  3. MP3 File Path: {mp3_file_path if mp3_file_path else 'Not available'}")
        
        # Variable 4: Ground truth
        ground_truth = entry['ground_truth']
        print(f"  4. Ground Truth: {ground_truth}")
    
    print("\n" + "="*80)
    print("You can process each entry to extract these four variables as shown above.")
    print("="*80)


if __name__ == '__main__':
    main()
