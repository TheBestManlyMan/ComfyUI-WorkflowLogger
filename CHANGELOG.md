# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2024-12-02

### Added
- **CSV Reader Node** - Read data from existing CSV files
  - Select specific rows by index (0, 1, 2, etc.)
  - Use -1 to get the latest row
  - Outputs all fields individually for connecting to other nodes
  - Includes summary output with CSV statistics
- **CSV Browser Node** - View entire CSV contents
  - Display full CSV file in ComfyUI
  - Shows row count and file location
  - Perfect for reviewing all logged data at once
- Row selection functionality for precise data access
- Individual field outputs from CSV Reader for easy workflow integration

### Changed
- **Output location** now uses ComfyUI's main output folder (`ComfyUI/output/`) instead of custom_nodes folder
- All nodes automatically read/write from the standard ComfyUI output directory
- Automatic file continuation - reads existing file and appends new rows seamlessly

### Features Added
- Read and reuse previously logged prompts
- Browse complete workflow history
- Connect CSV data to other nodes for iteration
- Load specific shot configurations by row index
- Centralized CSV storage in ComfyUI's output folder

### Technical Improvements
- Better error handling for missing files
- Clear status messages in console
- Support for row range validation
- Uses `folder_paths.get_output_directory()` for proper ComfyUI integration

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
- [ ] Batch import/export functionality
- [ ] Delete or edit specific rows
- [ ] CSV merging capabilities
- [ ] Export to other formats (JSON, Excel)
- [ ] Search/filter functionality
- [ ] GUI preview of logged data within ComfyUI
- [ ] Timestamp auto-generation
- [ ] Custom field ordering
- [ ] Data validation rules
