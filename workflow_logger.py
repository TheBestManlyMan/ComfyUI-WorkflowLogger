import os
import csv
import folder_paths


class WorkflowLoggerNode:
    """
    A custom ComfyUI node that collects workflow information and logs it to a CSV file.
    If id already exists, replaces that row. Otherwise, appends a new row.
    Returns the input tuple as output.
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
