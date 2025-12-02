# 🚀 Quick Start Guide

Get up and running with Workflow Logger in 5 minutes!

## Step 1: Install (Choose One Method)

### A) Direct Download
1. Download the `ComfyUI-WorkflowLogger` folder
2. Copy it to: `ComfyUI/custom_nodes/`
3. Restart ComfyUI

### B) Git Clone
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/YOUR_USERNAME/ComfyUI-WorkflowLogger.git
```
Then restart ComfyUI

## Step 2: Verify Installation

Look for **"Workflow Logger"** in your nodes list under the `utils` category

## Step 3: Test It Out

### Method 1: Quick Test in ComfyUI
1. Add a "Workflow Logger" node
2. Add text nodes and connect to inputs
3. Fill in:
   - id: `test_001`
   - prompt: `a beautiful landscape`
   - prompt1: `at sunset`
   - prompt_neg: `blurry, low quality`
   - csv_filename: `my_test.csv`
4. Run the workflow
5. Check: `ComfyUI/custom_nodes/ComfyUI-WorkflowLogger/output/my_test.csv`

### Method 2: Command Line Test
```bash
cd ComfyUI/custom_nodes/ComfyUI-WorkflowLogger/
python test_node.py
```

Should output: ✓ Logged to output/test_output.csv

## Step 4: Build Your Workflow

Connect these nodes to Workflow Logger:
- **Video filename** → id
- **Your prompts** → prompt, prompt1, prompt_neg
- **Generation settings** → shift, seed (optional)

Each time your workflow runs, it adds a row to the CSV!

## Need Help?

- 📖 See `USAGE_GUIDE.md` for detailed examples
- 🐛 Check console for error messages
- 💬 Open an issue on GitHub

## Next Steps

- Read `USAGE_GUIDE.md` for workflow patterns
- Check `GITHUB_SETUP.md` to publish your own version
- Customize the node by editing `__init__.py`

That's it! Start logging your workflow data! 📊
