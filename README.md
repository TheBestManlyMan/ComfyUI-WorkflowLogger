# ComfyUI Workflow Logger

Custom nodes for logging workflow data to CSV files in ComfyUI.

## Nodes

### Workflow Logger
Logs workflow information to CSV files with ID-based row replacement.

**Inputs:**
- `id` - Unique identifier (required, cannot be empty)
- `prompt` - Main prompt text
- `prompt1` - Secondary prompt
- `prompt_neg` - Negative prompt
- `shift` - Custom parameter
- `seed` - Generation seed
- `directory` - Save location (defaults to ComfyUI output folder)
- `csv_filename` - CSV filename (default: workflow_log.csv)

**Outputs:**
Returns all 6 input values as tuple: `(id, prompt, prompt1, prompt_neg, shift, seed)`

**Behavior:**
- If ID exists in CSV: replaces that row with new data
- If ID doesn't exist: appends new row
- Creates directory automatically if needed
- Creates CSV with headers on first use

### CSV Reader
Reads data from CSV files.

**Inputs:**
- `csv_filename` - CSV file to read
- `row_index` - Row to read (-1 for last row, 0+ for specific row)

**Outputs:**
`(id, prompt, prompt1, prompt_neg, shift, seed, csv_content)`

### CSV Browser
Displays entire CSV file contents.

**Inputs:**
- `csv_filename` - CSV file to view

**Outputs:**
- `csv_data` - Formatted CSV contents

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TheBestManlyMan/ComfyUI-WorkflowLogger.git
```

Restart ComfyUI.

## Example Usage

```
Text → Workflow Logger → [outputs can connect to other nodes]
```

CSV files are saved to the specified directory or ComfyUI's output folder by default.

## License

MIT
