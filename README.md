# ComfyUI Workflow Logger

A custom node for ComfyUI that logs workflow information to CSV files - perfect for tracking prompt variations, shot IDs, and generation parameters.

## 🆕 Version 1.1 - New Features!

- ✅ **CSV Reader Node** - Read data from existing CSV files
- ✅ **CSV Browser Node** - View entire CSV contents
- ✅ **Row Selection** - Read specific rows or latest entry
- ✅ All original logging features maintained

## Features

### Workflow Logger Node
- Collect workflow data with multiple string inputs
- Auto-append to CSV files
- Customizable output filename
- Supports ID, prompts, negative prompts, and custom fields
- UTF-8 encoding with BOM for Excel compatibility

### CSV Reader Node (NEW!)
- Read data from logged CSV files
- Access specific rows by index
- Get last row with index -1
- Outputs all fields individually for connecting to other nodes
- Summary output shows CSV stats

### CSV Browser Node (NEW!)
- Display entire CSV contents
- See row count and file location
- Preview all logged data in one view

## Installation

### Method 1: Git Clone (Recommended)
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TheBestManlyMan/ComfyUI-WorkflowLogger.git
```
Restart ComfyUI

### Method 2: Manual Install
1. Download this repository
2. Extract to `ComfyUI/custom_nodes/ComfyUI-WorkflowLogger/`
3. Restart ComfyUI

## Usage

### Workflow Logger Node
Add the **Workflow Logger** node (found under `utils` category)

**Inputs:**
- **id**: Shot or sequence ID (from video filename or other source)
- **prompt**: Main prompt text
- **prompt1**: Secondary prompt (e.g., background description)
- **prompt_neg**: Negative prompt
- **csv_filename**: Name of the CSV file to create/append to
- **shift** (optional): Additional parameter
- **seed** (optional): Generation seed

**Output:**
- **status**: Confirmation message showing save location

**How it works:**
- Automatically creates CSV file with headers on first use
- Continues appending rows to existing file (remembers where it left off)
- Saves to ComfyUI's main output folder

### CSV Reader Node (NEW!)
Add the **CSV Reader** node (found under `utils` category)

**Inputs:**
- **csv_filename**: Name of CSV file to read
- **row_index**: Which row to read (-1 for last, 0+ for specific row)

**Outputs:**
- **id**: Shot/sequence ID from selected row
- **prompt**: Prompt text
- **prompt1**: Secondary prompt
- **prompt_neg**: Negative prompt
- **shift**: Shift parameter
- **seed**: Seed value
- **csv_content**: Summary information about the CSV

### CSV Browser Node (NEW!)
Add the **CSV Browser** node (found under `utils` category)

**Inputs:**
- **csv_filename**: Name of CSV file to view

**Outputs:**
- **csv_data**: Full CSV contents formatted for viewing

## Example Workflows

### Basic Logging Workflow
```
Video Input → Get Filename → Workflow Logger
Text Input (prompt) → Workflow Logger
Text Input (prompt1) → Workflow Logger  
Text Input (prompt_neg) → Workflow Logger
```

### Read and Reuse Workflow (NEW!)
```
CSV Reader → [outputs] → Text Display
    OR
CSV Reader → [id] → Video Loader
CSV Reader → [prompt] → Text Node
CSV Reader → [prompt1] → Text Node
CSV Reader → Generate New Variation
```

### Browse Previous Entries (NEW!)
```
CSV Browser → Text Display/Save
```

## Output Format

CSV files are saved to: `ComfyUI/output/` (ComfyUI's default output folder)

Example CSV:
```csv
id,prompt,prompt1,prompt_neg,shift,seed
1_21_02,"a woman in grey coat...",on green screen,"no talking",,
1_21_03,"a woman with red hair...",on green screen,"no talking",,12345
```

## Use Cases

### VFX Shot Tracking
- Log every AI-generated shot variant
- Track which combinations work best
- Read previous shots for consistency

### Dataset Creation
- Build training datasets with metadata
- Read and verify logged entries
- Export for training pipelines

### A/B Testing
- Log multiple prompt variations
- Read specific versions for comparison
- Track performance of different approaches

### Workflow Iteration
- Save working prompts
- Load and modify previous successes
- Build upon proven configurations

## Tips & Best Practices

- Use consistent ID naming (e.g., `scene_shot_take`)
- One CSV per project for better organization
- Use CSV Reader to review what's been logged
- Use CSV Browser to see full dataset at a glance
- Row index -1 always gets the latest entry

## Requirements

- ComfyUI
- Python 3.x (comes with ComfyUI)

## Changelog

### Version 1.1.0 (2024-12-02)
- Added CSV Reader node for reading logged data
- Added CSV Browser node for viewing full CSV contents
- Support for row selection (specific index or latest)
- Individual output fields for easy node connections

### Version 1.0.0 (2024-12-02)
- Initial release
- Workflow Logger node with CSV export
- Support for id, prompts, and parameters

## License

MIT License - feel free to modify and use!

## Credits

Built for VFX artists tracking AI generation workflows 🎬
