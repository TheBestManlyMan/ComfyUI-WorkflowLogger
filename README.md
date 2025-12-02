# ComfyUI Workflow Logger

Logs workflow data to CSV files.

## Inputs

- id (required, cannot be empty)
- prompt
- prompt1
- prompt_neg
- shift
- seed
- directory (defaults to ComfyUI output folder)
- csv_filename (default: workflow_log.csv)

## Outputs

Returns all 6 input values: (id, prompt, prompt1, prompt_neg, shift, seed)

## Behavior

If ID exists in CSV, replaces that row. Otherwise appends new row.

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TheBestManlyMan/ComfyUI-WorkflowLogger.git
```

Restart ComfyUI.
