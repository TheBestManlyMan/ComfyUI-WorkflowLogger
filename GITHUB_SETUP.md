# GitHub Upload Instructions

## Quick Start: Getting Your Node on GitHub

### 1. Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Name it: `ComfyUI-WorkflowLogger`
4. Description: "Custom ComfyUI node for logging workflow data to CSV files"
5. Make it Public (so others can use it!)
6. DON'T initialize with README (we already have one)
7. Click "Create repository"

### 2. Upload Your Files

**Option A: Using GitHub Web Interface (Easiest)**
1. On your new repository page, click "uploading an existing file"
2. Drag and drop ALL files from the `ComfyUI-WorkflowLogger` folder:
   - `__init__.py`
   - `README.md`
   - `LICENSE`
   - `.gitignore`
   - `test_node.py`
   - `example_workflow.json`
3. Add commit message: "Initial commit - Workflow Logger node"
4. Click "Commit changes"

**Option B: Using Git Command Line**
```bash
cd ComfyUI-WorkflowLogger
git init
git add .
git commit -m "Initial commit - Workflow Logger node"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ComfyUI-WorkflowLogger.git
git push -u origin main
```

### 3. Customize Your Repository

**Update README.md:**
- Replace `YOUR_USERNAME` with your actual GitHub username in the installation instructions

**Update LICENSE:**
- Replace `[Your Name]` with your actual name

**Add a repository description:**
- Click "About" (⚙️ icon) on the right side of your repo
- Add: "Custom ComfyUI node for logging workflow data to CSV"
- Add topics: `comfyui`, `comfyui-custom-nodes`, `workflow`, `csv-logger`

### 4. Share Your Node!

Once uploaded, users can install it with:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/YOUR_USERNAME/ComfyUI-WorkflowLogger.git
```

### 5. Test Installation

Before sharing publicly, test your node:
1. Clone it into your ComfyUI/custom_nodes/ folder
2. Restart ComfyUI
3. Look for "Workflow Logger" under the utils category
4. Run a test workflow to make sure CSV logging works!

## Making Updates

When you improve the node:
```bash
git add .
git commit -m "Description of your changes"
git push
```

Users can update with:
```bash
cd ComfyUI/custom_nodes/ComfyUI-WorkflowLogger
git pull
```

## Need Help?

- [GitHub Docs](https://docs.github.com/en/get-started/quickstart)
- Test your node with `python test_node.py` before uploading
- Make sure all files are included in your commit

Happy coding! 🎬
