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

Samples evenly-spaced images from a batch.

### Inputs

- images (IMAGE batch)
- count (number of images to sample)

### Outputs

- images (sampled IMAGE batch)

### Behavior

Samples images evenly across the batch. For example:
- 10 images, count 5: returns indices [0, 2, 4, 6, 8]
- 100 images, count 2: returns indices [0, 50]

If count is greater than batch size, returns all images.

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TheBestManlyMan/ComfyUI-WorkflowLogger.git
```

Restart ComfyUI.
