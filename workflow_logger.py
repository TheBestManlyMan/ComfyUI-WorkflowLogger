import os
import csv
import folder_paths


class WorkflowLoggerNode:

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
        if not id or id.strip() == "":
            error_msg = "Error: ID is required and cannot be empty"
            print(error_msg)
            raise ValueError(error_msg)

        try:
            if directory and directory.strip():
                output_dir = directory.strip()
            else:
                output_dir = folder_paths.get_output_directory()

            os.makedirs(output_dir, exist_ok=True)

            csv_path = os.path.join(output_dir, csv_filename)

            fieldnames = ['id', 'prompt', 'prompt1', 'prompt_neg', 'shift', 'seed']

            new_row = {
                'id': id,
                'prompt': prompt,
                'prompt1': prompt1,
                'prompt_neg': prompt_neg,
                'shift': shift,
                'seed': seed
            }

            existing_rows = []
            file_exists = os.path.isfile(csv_path)
            id_found = False

            if file_exists:
                with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row.get('id') == id:
                            existing_rows.append(new_row)
                            id_found = True
                        else:
                            existing_rows.append(row)

            if not id_found:
                existing_rows.append(new_row)

            with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(existing_rows)

            action = "Updated" if id_found else "Added"
            status_msg = f"{action} id '{id}' in {csv_path}"
            print(status_msg)

            return (id, prompt, prompt1, prompt_neg, shift, seed)

        except Exception as e:
            error_msg = f"Error logging to CSV: {str(e)}"
            print(error_msg)
            raise RuntimeError(error_msg)
