# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-12-02

### Added
- Initial release of Workflow Logger node
- CSV logging functionality with customizable fields
- Support for id, prompt, prompt1, prompt_neg inputs
- Optional shift and seed parameters
- Auto-header creation for new CSV files
- UTF-8 with BOM encoding for Excel compatibility
- Status output showing save confirmation
- Example workflow and test script
- Comprehensive documentation

### Features
- Append mode for building datasets over multiple runs
- Customizable CSV filename
- Automatic output directory creation
- Multiline text support for prompts
- Simple, lightweight implementation with no external dependencies

## Future Considerations

Potential features for future versions:
- [ ] GUI preview of logged data within ComfyUI
- [ ] Batch mode with manual save trigger
- [ ] Export to other formats (JSON, Excel)
- [ ] Timestamp auto-generation
- [ ] Custom field ordering
- [ ] Clear/reset CSV option
