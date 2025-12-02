#!/usr/bin/env python3
"""
Test script for WorkflowLoggerNode CSV update functionality
"""
import os
import csv
import sys
import tempfile

# Mock folder_paths module for testing
class MockFolderPaths:
    @staticmethod
    def get_output_directory():
        # Use temp directory for testing
        return tempfile.gettempdir()

sys.modules['folder_paths'] = MockFolderPaths()

# Now import the node
from __init__ import WorkflowLoggerNode

def test_csv_logger():
    """Test the CSV logger with id replacement functionality"""

    # Create a node instance
    node = WorkflowLoggerNode()

    # Use a test CSV filename
    test_csv = "test_workflow_log.csv"
    test_csv_path = os.path.join(tempfile.gettempdir(), test_csv)

    # Clean up any existing test file
    if os.path.exists(test_csv_path):
        os.remove(test_csv_path)

    print("=" * 60)
    print("Testing WorkflowLogger CSV Update Functionality")
    print("=" * 60)

    # Test 1: Add first entry
    print("\n1. Adding entry with id='001'...")
    result = node.log_to_csv(
        id="001",
        prompt="A beautiful sunset",
        prompt1="cinematic lighting",
        prompt_neg="blurry, low quality",
        csv_filename=test_csv,
        shift="1.5",
        seed="12345"
    )
    print(f"   Result: {result[0]}")

    # Test 2: Add second entry
    print("\n2. Adding entry with id='002'...")
    result = node.log_to_csv(
        id="002",
        prompt="A majestic mountain",
        prompt1="high detail",
        prompt_neg="cartoon",
        csv_filename=test_csv,
        shift="2.0",
        seed="67890"
    )
    print(f"   Result: {result[0]}")

    # Test 3: Update first entry (id='001')
    print("\n3. Updating entry with id='001' (should replace)...")
    result = node.log_to_csv(
        id="001",
        prompt="An updated sunset scene",
        prompt1="dramatic colors",
        prompt_neg="dark, gloomy",
        csv_filename=test_csv,
        shift="3.0",
        seed="99999"
    )
    print(f"   Result: {result[0]}")

    # Test 4: Add third entry
    print("\n4. Adding entry with id='003'...")
    result = node.log_to_csv(
        id="003",
        prompt="A peaceful lake",
        prompt1="reflections",
        prompt_neg="busy, crowded",
        csv_filename=test_csv,
        shift="1.0",
        seed="11111"
    )
    print(f"   Result: {result[0]}")

    # Verify the CSV contents
    print("\n" + "=" * 60)
    print("CSV File Contents:")
    print("=" * 60)

    with open(test_csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        print(f"\nTotal rows: {len(rows)}")
        print("\nRow details:")
        for i, row in enumerate(rows, 1):
            print(f"\n  Row {i}:")
            print(f"    ID: {row['id']}")
            print(f"    Prompt: {row['prompt']}")
            print(f"    Prompt1: {row['prompt1']}")
            print(f"    Prompt_neg: {row['prompt_neg']}")
            print(f"    Shift: {row['shift']}")
            print(f"    Seed: {row['seed']}")

    # Verify expectations
    print("\n" + "=" * 60)
    print("Verification:")
    print("=" * 60)

    assert len(rows) == 3, f"Expected 3 rows, got {len(rows)}"
    print("✓ Row count is correct (3 rows)")

    # Check that id='001' was updated
    row_001 = next((r for r in rows if r['id'] == '001'), None)
    assert row_001 is not None, "ID '001' not found"
    assert row_001['prompt'] == "An updated sunset scene", "ID '001' was not updated"
    assert row_001['seed'] == "99999", "ID '001' seed was not updated"
    print("✓ ID '001' was successfully updated")

    # Check that id='002' exists
    row_002 = next((r for r in rows if r['id'] == '002'), None)
    assert row_002 is not None, "ID '002' not found"
    print("✓ ID '002' exists")

    # Check that id='003' exists
    row_003 = next((r for r in rows if r['id'] == '003'), None)
    assert row_003 is not None, "ID '003' not found"
    print("✓ ID '003' exists")

    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)

    # Clean up
    print(f"\nTest CSV location: {test_csv_path}")
    print("(Keeping test file for manual inspection)")

if __name__ == "__main__":
    try:
        test_csv_logger()
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
