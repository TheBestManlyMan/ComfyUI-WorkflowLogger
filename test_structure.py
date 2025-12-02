#!/usr/bin/env python3
"""
Test script to verify the restructured node imports work correctly
"""
import sys
import os
import tempfile

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock folder_paths module for testing
class MockFolderPaths:
    @staticmethod
    def get_output_directory():
        return tempfile.gettempdir()

sys.modules['folder_paths'] = MockFolderPaths()

print("=" * 60)
print("Testing Restructured Node Imports")
print("=" * 60)

# Test 1: Import individual modules
print("\n1. Testing individual module imports...")
try:
    from workflow_logger import WorkflowLoggerNode
    print("   ✓ workflow_logger.py imports successfully")

    from csv_reader import CSVReaderNode
    print("   ✓ csv_reader.py imports successfully")

    from csv_browser import CSVBrowserNode
    print("   ✓ csv_browser.py imports successfully")
except Exception as e:
    print(f"   ✗ Failed to import individual modules: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 2: Verify node classes have required attributes
print("\n2. Verifying node class attributes...")
try:
    required_attrs = ["INPUT_TYPES", "RETURN_TYPES", "RETURN_NAMES", "FUNCTION", "CATEGORY"]

    for attr in required_attrs:
        if not hasattr(WorkflowLoggerNode, attr):
            print(f"   ✗ WorkflowLoggerNode missing attribute: {attr}")
            sys.exit(1)

    print("   ✓ WorkflowLoggerNode has all required attributes")
    print(f"     - FUNCTION: {WorkflowLoggerNode.FUNCTION}")
    print(f"     - CATEGORY: {WorkflowLoggerNode.CATEGORY}")
    print(f"     - RETURN_TYPES: {len(WorkflowLoggerNode.RETURN_TYPES)} outputs")
except Exception as e:
    print(f"   ✗ Error verifying node attributes: {e}")
    sys.exit(1)

# Test 3: Test instantiation
print("\n3. Testing node instantiation...")
try:
    workflow_logger_instance = WorkflowLoggerNode()
    print("   ✓ Successfully instantiated WorkflowLoggerNode")

    csv_reader_instance = CSVReaderNode()
    print("   ✓ Successfully instantiated CSVReaderNode")

    csv_browser_instance = CSVBrowserNode()
    print("   ✓ Successfully instantiated CSVBrowserNode")
except Exception as e:
    print(f"   ✗ Error instantiating nodes: {e}")
    sys.exit(1)

# Test 4: Verify INPUT_TYPES method works
print("\n4. Testing INPUT_TYPES methods...")
try:
    wl_inputs = WorkflowLoggerNode.INPUT_TYPES()
    assert "required" in wl_inputs, "WorkflowLogger missing 'required' in INPUT_TYPES"
    assert "id" in wl_inputs["required"], "WorkflowLogger missing 'id' input"
    print("   ✓ WorkflowLoggerNode.INPUT_TYPES() works correctly")

    reader_inputs = CSVReaderNode.INPUT_TYPES()
    assert "required" in reader_inputs, "CSVReader missing 'required' in INPUT_TYPES"
    print("   ✓ CSVReaderNode.INPUT_TYPES() works correctly")

    browser_inputs = CSVBrowserNode.INPUT_TYPES()
    assert "required" in browser_inputs, "CSVBrowser missing 'required' in INPUT_TYPES"
    print("   ✓ CSVBrowserNode.INPUT_TYPES() works correctly")
except Exception as e:
    print(f"   ✗ Error testing INPUT_TYPES: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ All structure tests passed!")
print("=" * 60)
print("\nRepository structure successfully follows Kaskis pattern:")
print("  - workflow_logger.py (WorkflowLoggerNode)")
print("  - csv_reader.py (CSVReaderNode)")
print("  - csv_browser.py (CSVBrowserNode)")
print("  - __init__.py (imports and registers all nodes)")
