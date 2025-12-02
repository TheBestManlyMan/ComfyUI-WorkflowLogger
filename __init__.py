import os
import csv
from datetime import datetime

class WorkflowLoggerNode:
    """
    A custom ComfyUI node that collects workflow information and logs it to a CSV file.
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
                "csv_filename": ("STRING", {
                    "multiline": False,
                    "default": "workflow_log.csv"
                }),
            },
            "optional": {
                "shift": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "seed": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status",)
    FUNCTION = "log_to_csv"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def log_to_csv(self, id, prompt, prompt1, prompt_neg, csv_filename, shift="", seed=""):
        """
        Logs the workflow data to a CSV file.
        """
        try:
            # Determine the full path for the CSV file
            # You can customize this path as needed
            output_dir = os.path.join(os.path.dirname(__file__), "output")
            os.makedirs(output_dir, exist_ok=True)
            csv_path = os.path.join(output_dir, csv_filename)
            
            # Check if file exists to determine if we need to write headers
            file_exists = os.path.isfile(csv_path)
            
            # Prepare the data row
            row_data = {
                'id': id,
                'prompt': prompt,
                'prompt1': prompt1,
                'prompt_neg': prompt_neg,
                'shift': shift,
                'seed': seed
            }
            
            # Write to CSV
            with open(csv_path, 'a', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['id', 'prompt', 'prompt1', 'prompt_neg', 'shift', 'seed']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write header if file is new
                if not file_exists:
                    writer.writeheader()
                
                # Write the data row
                writer.writerow(row_data)
            
            status_msg = f"✓ Logged to {csv_path}"
            print(status_msg)
            return (status_msg,)
            
        except Exception as e:
            error_msg = f"✗ Error logging to CSV: {str(e)}"
            print(error_msg)
            return (error_msg,)


# Node registration mapping
NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode
}

# Display name mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger"
}
