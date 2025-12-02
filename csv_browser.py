import os
import folder_paths


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
