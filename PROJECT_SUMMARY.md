# ComfyUI Workflow Logger - Project Summary

## 🎯 What We Built

A custom ComfyUI node that logs workflow data to CSV files - perfect for tracking shot IDs, prompts, and generation parameters for VFX/animation pipelines.

## 📦 Package Contents

```
ComfyUI-WorkflowLogger/
├── __init__.py              # Main node code
├── README.md                # Installation & overview
├── QUICKSTART.md            # 5-minute setup guide
├── USAGE_GUIDE.md           # Detailed usage examples
├── GITHUB_SETUP.md          # How to upload to GitHub
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT License
├── .gitignore              # Git ignore rules
├── test_node.py            # Test script
├── example_workflow.json   # Example usage
└── output/                 # CSV files saved here
```

## ✅ Features Implemented

- ✅ String inputs: id, prompt, prompt1, prompt_neg
- ✅ Optional inputs: shift, seed
- ✅ Automatic CSV creation with headers
- ✅ Append mode (builds dataset over multiple runs)
- ✅ Customizable output filename
- ✅ UTF-8 with BOM encoding (Excel-friendly)
- ✅ Status output showing save confirmation
- ✅ Comprehensive documentation
- ✅ Test script included
- ✅ Ready for GitHub upload

## 🚀 Next Steps

### 1. Test Locally
```bash
cd ComfyUI-WorkflowLogger
python test_node.py
```

### 2. Install in ComfyUI
- Copy folder to: `ComfyUI/custom_nodes/`
- Restart ComfyUI
- Find node under `utils` category

### 3. Upload to GitHub
- Follow instructions in `GITHUB_SETUP.md`
- Share with the community!

## 💡 How It Works

```
Your Workflow:
Video → Get Filename → [id]
                         ↓
Text Nodes → [prompt, prompt1, prompt_neg]
                         ↓
              [Workflow Logger]
                         ↓
              output/your_file.csv
```

Each workflow execution = 1 new row in CSV

## 🎨 Customization Ideas

Want to extend it? Easy modifications:

1. **Add more fields**: Edit `__init__.py` INPUT_TYPES
2. **Change output location**: Modify `output_dir` path
3. **Add timestamps**: Include datetime in row_data
4. **Export formats**: Add JSON/Excel export options
5. **Preview UI**: Display logged data in ComfyUI

## 📊 Example Output

```csv
id,prompt,prompt1,prompt_neg,shift,seed
1_21_02,"woman walking",green screen background,"no talking",,
1_21_03,"woman waving",green screen background,"no talking",,12345
```

## 🔧 Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses standard library)
- **ComfyUI Version**: Compatible with current versions
- **File Size**: ~15KB total
- **Performance**: Lightweight, minimal overhead

## 📝 Code Quality

- Clean, readable code
- Proper error handling
- Informative console output
- UTF-8 encoding support
- Cross-platform compatible

## 🎓 Learning Resources

If you want to build more nodes:
- Study `__init__.py` structure
- Check ComfyUI custom node docs
- Experiment with INPUT_TYPES
- Join ComfyUI Discord/community

## 🤝 Contributing

This is your node! Feel free to:
- Modify for your needs
- Share improvements
- Help others in the community
- Build derivative works

## 📄 License

MIT License - Free to use, modify, and share!

---

Built for VFX artists tracking AI workflows 🎬
Houdini FX artists welcome! 🌊
