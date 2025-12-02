# Workflow Logger - Detailed Usage Guide

## Node Overview

The **Workflow Logger** node appears in ComfyUI under the `utils` category with these inputs:

### Required Inputs
- **id** (string) - Shot/sequence identifier from video filename
- **prompt** (string, multiline) - Main prompt text
- **prompt1** (string, multiline) - Secondary prompt (backgrounds, settings)
- **prompt_neg** (string, multiline) - Negative prompt
- **csv_filename** (string) - Output CSV filename

### Optional Inputs
- **shift** (string) - Additional parameter field
- **seed** (string) - Generation seed value

### Output
- **status** (string) - Confirmation message showing save location

## Common Workflow Patterns

### Pattern 1: Video Processing Pipeline
```
Load Video Node
    ↓ (video)
Video Info Node → Get Filename
    ↓ (filename)
    ├→ Workflow Logger [id input]
    
Text Prompt Node
    ↓ (text)
    └→ Workflow Logger [prompt input]

Background Prompt Node
    ↓ (text)
    └→ Workflow Logger [prompt1 input]

Negative Prompt Node  
    ↓ (text)
    └→ Workflow Logger [prompt_neg input]
```

### Pattern 2: Batch Processing with Iteration
```
For each video in folder:
    - Extract filename → id
    - Load prompts from database/file
    - Process generation
    - Log results to CSV
    - Move to next video
```

### Pattern 3: A/B Testing Setup
```
Same video, multiple prompt variations:
    - Keep same id
    - Vary prompt/prompt1/prompt_neg
    - Each variation creates new CSV row
    - Compare results in spreadsheet
```

## CSV Output Structure

Your CSV will look like this:

```csv
id,prompt,prompt1,prompt_neg,shift,seed
1_21_02,"a woman in grey coat...",on green screen,"no talking",,
1_21_03,"a woman with red hair...",on green screen,"no talking",,12345
```

- **Headers**: Auto-created on first run
- **Encoding**: UTF-8 with BOM (Excel-friendly)
- **Location**: `custom_nodes/ComfyUI-WorkflowLogger/output/`
- **Behavior**: Appends new row each execution

## Tips & Best Practices

### Organizing Your Data
1. **Use consistent ID naming**: `scene_shot_take` format (e.g., `1_21_02`)
2. **One CSV per project**: Set unique csv_filename for each project
3. **Include seed values**: Track seeds for reproducible results
4. **Use descriptive prompts**: Detailed prompts help review later

### Workflow Efficiency
- **Connect as output node**: Set it as the final node in your workflow
- **Use with batch processing**: Perfect for processing multiple files
- **Combine with conditionals**: Only log successful generations

### Troubleshooting
- **CSV not found**: Check `output/` folder in node directory
- **Encoding issues**: UTF-8 with BOM handles special characters
- **Missing data**: Empty fields show as blank in CSV
- **Duplicate entries**: Each workflow run appends - this is intentional!

## Example Use Cases

### VFX Shot Tracking
Track every AI-generated shot variant for a film/animation project:
- ID from shot list
- Prompt variations for each take
- Track which combinations work best

### Dataset Creation
Build training datasets with metadata:
- Log every generation with exact prompts
- Include seeds for reproducibility  
- Export CSV for training pipeline

### Client Deliverables
Document what was generated for clients:
- IDs match shot numbers
- Prompts show exact instructions used
- CSV becomes deliverable documentation

## Advanced: Extending the Node

Want to add more fields? Edit `__init__.py`:

```python
# Add to INPUT_TYPES "required" section:
"your_field": ("STRING", {
    "multiline": False,
    "default": ""
}),

# Add to fieldnames list:
fieldnames = ['id', 'prompt', 'prompt1', 'prompt_neg', 'shift', 'seed', 'your_field']

# Add to row_data dict:
row_data = {
    # ... existing fields ...
    'your_field': your_field
}

# Add to function signature:
def log_to_csv(self, id, prompt, prompt1, prompt_neg, csv_filename, shift="", seed="", your_field=""):
```

## Questions?

This is a simple, straightforward node - if something's not working:
1. Check the console for error messages
2. Verify the `output/` folder exists
3. Make sure all required inputs are connected
4. Test with the included `test_node.py` script

Happy logging! 📊
