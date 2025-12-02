import os
import csv
from datetime import datetime
import folder_paths

class WorkflowLoggerNode:
    """
    A custom ComfyUI node that collects workflow information and logs it to a CSV file.
    Saves to ComfyUI's output folder and continues from where it left off.
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "id": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt1": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt_neg": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "shift": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "seed": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "directory": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "csv_filename": ("STRING", {
                    "multiline": False,
                    "default": "workflow_log.csv"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("id", "prompt", "prompt1", "prompt_neg", "shift", "seed")
    FUNCTION = "log_to_csv"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def log_to_csv(self, id, prompt, prompt1, prompt_neg, shift, seed, directory, csv_filename):
        """
        Logs the workflow data to a CSV file in the specified directory.
        If id already exists, replaces that row. Otherwise, appends a new row.
        Returns the input tuple as output.
        """
        # Validate that ID is not empty
        if not id or id.strip() == "":
            error_msg = "✗ Error: ID is required and cannot be empty"
            print(error_msg)
            raise ValueError(error_msg)

        try:
            # Use specified directory, fallback to ComfyUI's output directory if not provided
            if directory and directory.strip():
                output_dir = directory.strip()
            else:
                output_dir = folder_paths.get_output_directory()

            # Create directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            csv_path = os.path.join(output_dir, csv_filename)

            # Define fieldnames
            fieldnames = ['id', 'prompt', 'prompt1', 'prompt_neg', 'shift', 'seed']

            # Prepare the new data row
            new_row = {
                'id': id,
                'prompt': prompt,
                'prompt1': prompt1,
                'prompt_neg': prompt_neg,
                'shift': shift,
                'seed': seed
            }

            # Read existing data if file exists
            existing_rows = []
            file_exists = os.path.isfile(csv_path)
            id_found = False

            if file_exists:
                with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row.get('id') == id:
                            # Replace the existing row with new data
                            existing_rows.append(new_row)
                            id_found = True
                        else:
                            existing_rows.append(row)

            # If id wasn't found or file doesn't exist, append the new row
            if not id_found:
                existing_rows.append(new_row)

            # Write all data back to CSV
            with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(existing_rows)

            action = "Updated" if id_found else "Added"
            status_msg = f"✓ {action} id '{id}' in {csv_path}"
            print(status_msg)

            # Return the input tuple
            return (id, prompt, prompt1, prompt_neg, shift, seed)

        except Exception as e:
            error_msg = f"✗ Error logging to CSV: {str(e)}"
            print(error_msg)
            raise RuntimeError(error_msg)


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


class CSVBrowserNode:
    """
    A custom ComfyUI node that displays all CSV content from ComfyUI's output folder.
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
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("csv_data",)
    FUNCTION = "browse_csv"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def browse_csv(self, csv_filename):
        """
        Reads and formats the entire CSV file from ComfyUI's output folder for display.
        """
        try:
            # Use ComfyUI's output directory
            output_dir = folder_paths.get_output_directory()
            csv_path = os.path.join(output_dir, csv_filename)
            
            if not os.path.isfile(csv_path):
                return (f"CSV file not found: {csv_path}",)
            
            # Read the entire CSV
            with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
                content = csvfile.read()
                
            row_count = content.count('\n')
            summary = f"=== CSV: {csv_filename} ===\n"
            summary += f"Total rows: {row_count - 1}\n"  # -1 for header
            summary += f"Location: {csv_path}\n"
            summary += "=" * 50 + "\n\n"
            summary += content
            
            print(f"✓ Loaded {csv_filename} ({row_count - 1} rows)")
            return (summary,)
            
        except Exception as e:
            error_msg = f"✗ Error browsing CSV: {str(e)}"
            print(error_msg)
            return (error_msg,)


# Node registration mapping
NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode,
    "CSVReader": CSVReaderNode,
    "CSVBrowser": CSVBrowserNode
}

# Display name mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger",
    "CSVReader": "CSV Reader",
    "CSVBrowser": "CSV Browser"
}
