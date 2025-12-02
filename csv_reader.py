import os
import csv
import folder_paths


class CSVReaderNode:
    """
    A custom ComfyUI node that reads CSV files from ComfyUI's output folder.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "csv_filename": ("STRING", {
                    "multiline": False,
                    "default": "workflow_log.csv"
                }),
            },
            "optional": {
                "row_index": ("INT", {
                    "default": -1,
                    "min": -1,
                    "max": 10000,
                    "step": 1,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("id", "prompt", "prompt1", "prompt_neg", "shift", "seed", "csv_content")
    FUNCTION = "read_csv"
    CATEGORY = "utils"

    def read_csv(self, csv_filename, row_index=-1):
        """
        Reads the CSV file from ComfyUI's output folder and returns data.
        row_index: -1 for last row, 0+ for specific row
        """
        try:
            # Use ComfyUI's output directory
            output_dir = folder_paths.get_output_directory()
            csv_path = os.path.join(output_dir, csv_filename)

            # Check if file exists
            if not os.path.isfile(csv_path):
                error_msg = f"CSV file not found: {csv_path}"
                print(error_msg)
                return ("", "", "", "", "", "", error_msg)

            # Read the CSV file
            with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)

                if not rows:
                    return ("", "", "", "", "", "", "CSV file is empty")

                # Get the specified row
                if row_index == -1:
                    # Get last row
                    row = rows[-1]
                elif 0 <= row_index < len(rows):
                    # Get specific row
                    row = rows[row_index]
                else:
                    error_msg = f"Row index {row_index} out of range (0-{len(rows)-1})"
                    print(error_msg)
                    return ("", "", "", "", "", "", error_msg)

                # Create summary of full CSV
                csv_summary = f"CSV has {len(rows)} rows\n"
                csv_summary += f"Latest ID: {rows[-1].get('id', '')}\n"
                csv_summary += f"Returning row {row_index if row_index >= 0 else len(rows)-1}"

                # Return the row data
                return (
                    row.get('id', ''),
                    row.get('prompt', ''),
                    row.get('prompt1', ''),
                    row.get('prompt_neg', ''),
                    row.get('shift', ''),
                    row.get('seed', ''),
                    csv_summary
                )

        except Exception as e:
            error_msg = f"✗ Error reading CSV: {str(e)}"
            print(error_msg)
            return ("", "", "", "", "", "", error_msg)
