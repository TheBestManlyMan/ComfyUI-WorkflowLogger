# ComfyUI Workflow Logger

A custom node for ComfyUI that logs workflow information to CSV files - perfect for tracking prompt variations, shot IDs, and generation parameters.

## Features

- ✅ Collect workflow data with multiple string inputs
- ✅ Auto-append to CSV files
- ✅ Customizable output filename
- ✅ Supports ID, prompts, negative prompts, and custom fields
- ✅ UTF-8 encoding with BOM for Excel compatibility

## Installation

### Method 1: Git Clone (Recommended)
1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ComfyUI-WorkflowLogger.git
   ```

3. Restart ComfyUI

### Method 2: Manual Install
1. Download this repository
2. Extract to `ComfyUI/custom_nodes/ComfyUI-WorkflowLogger/`
3. Restart ComfyUI

## Usage

1. Add the **Workflow Logger** node to your workflow (found under `utils` category)

2. Connect your inputs:
   - **id**: Shot or sequence ID (from video filename or other source)
   - **prompt**: Main prompt text
   - **prompt1**: Secondary prompt (e.g., background description)
   - **prompt_neg**: Negative prompt
   - **csv_filename**: Name of the CSV file to create/append to
   - **shift** (optional): Additional parameter
   - **seed** (optional): Generation seed

3. Each time the workflow runs, it will append a new row to the CSV

4. CSV files are saved to: `ComfyUI/custom_nodes/ComfyUI-WorkflowLogger/output/`

## Example Workflow

```
Video Input → Get Filename → Workflow Logger
Text Input (prompt) → Workflow Logger
Text Input (prompt1) → Workflow Logger  
Text Input (prompt_neg) → Workflow Logger
```

## Output Format

The CSV will have the following columns:
```csv
id,prompt,prompt1,prompt_neg,shift,seed
1_21_02,"a woman in a grey coat...",on a green screen background,"moving mouth, talking...",,
```

## Tips

- Use the same `csv_filename` across multiple workflow runs to build up a dataset
- The ID field works great with video filename extractors
- All text fields support multiline input
- CSV files use UTF-8 with BOM encoding (Excel-friendly)

## Requirements

- ComfyUI
- Python 3.x (comes with ComfyUI)

## License

MIT License - feel free to modify and use!

## Credits

Built for VFX artists tracking AI generation workflows 🎬
