# ComfyUI Workflow Logger

Custom nodes for workflow management.

## Workflow Logger

Logs workflow data to CSV files.

### Inputs

- id (required, cannot be empty)
- prompt
- prompt1
- prompt_neg
- shift
- seed
- directory (defaults to ComfyUI output folder)
- csv_filename (default: workflow_log.csv)

### Outputs

Returns all 6 input values: (id, prompt, prompt1, prompt_neg, shift, seed)

### Behavior

If ID exists in CSV, replaces that row. Otherwise appends new row.

## Image Batch Sampler

Samples images from a batch using two modes.

### Inputs

- images (IMAGE batch)
- count (number of images when using even spacing mode)
- use_every_x (toggle between modes)
- every_x (interval when using every X mode)

### Outputs

- images (sampled IMAGE batch)

### Modes

**Even Spacing Mode (use_every_x = False):**
- Samples evenly across the batch
- Uses count parameter
- Examples:
  - 10 frames, count 5: returns [0, 2, 4, 6, 8]
  - 100 frames, count 2: returns [0, 50]

**Every X Mode (use_every_x = True):**
- Samples every X frames
- Uses every_x parameter
- Examples:
  - 10 frames, every 3: returns [0, 3, 6, 9]
  - 20 frames, every 5: returns [0, 5, 10, 15]

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TheBestManlyMan/ComfyUI-WorkflowLogger.git
```

Restart ComfyUI.
