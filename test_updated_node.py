#!/usr/bin/env python3
"""
Test script for updated WorkflowLoggerNode with directory support and tuple output
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

def test_updated_node():
    """Test the updated CSV logger with directory and tuple output"""

    # Create a node instance
    node = WorkflowLoggerNode()

    # Create a test directory
    test_dir = os.path.join(tempfile.gettempdir(), "comfyui_test")
    os.makedirs(test_dir, exist_ok=True)

    # Use a test CSV filename
    test_csv = "workflow_data.csv"
    test_csv_path = os.path.join(test_dir, test_csv)

    # Clean up any existing test file
    if os.path.exists(test_csv_path):
        os.remove(test_csv_path)

    print("=" * 60)
    print("Testing Updated WorkflowLogger Node")
    print("=" * 60)

    # Test 1: Add first entry with all required fields
    print("\n1. Adding entry with id='img_001'...")
    result = node.log_to_csv(
        id="img_001",
        prompt="A beautiful sunset over the ocean",
        prompt1="vibrant colors, golden hour",
        prompt_neg="blurry, low quality, dark",
        shift="1.5",
        seed="12345",
        directory=test_dir,
        csv_filename=test_csv
    )
    print(f"   Returned tuple: {result}")
    assert len(result) == 6, f"Expected 6 values, got {len(result)}"
    assert result[0] == "img_001", "ID mismatch"
    print("   ✓ Correct tuple returned")

    # Test 2: Add second entry
    print("\n2. Adding entry with id='img_002'...")
    result = node.log_to_csv(
        id="img_002",
        prompt="A majestic mountain landscape",
        prompt1="snow-capped peaks, blue sky",
        prompt_neg="foggy, overcast",
        shift="2.0",
        seed="67890",
        directory=test_dir,
        csv_filename=test_csv
    )
    print(f"   Returned tuple: {result}")
    assert result[0] == "img_002", "ID mismatch"
    print("   ✓ Correct tuple returned")

    # Test 3: Update first entry (should replace)
    print("\n3. Updating entry with id='img_001' (should replace)...")
    result = node.log_to_csv(
        id="img_001",
        prompt="An UPDATED sunset scene",
        prompt1="dramatic skies, clouds",
        prompt_neg="boring, plain",
        shift="3.0",
        seed="99999",
        directory=test_dir,
        csv_filename=test_csv
    )
    print(f"   Returned tuple: {result}")
    assert result[0] == "img_001", "ID mismatch"
    assert result[1] == "An UPDATED sunset scene", "Prompt mismatch"
    assert result[5] == "99999", "Seed mismatch"
    print("   ✓ Correct tuple returned with updated values")

    # Test 4: Try empty ID (should fail)
    print("\n4. Testing empty ID validation (should fail)...")
    try:
        result = node.log_to_csv(
            id="",
            prompt="This should fail",
            prompt1="test",
            prompt_neg="test",
            shift="1.0",
            seed="123",
            directory=test_dir,
            csv_filename=test_csv
        )
        print("   ✗ FAILED: Should have raised ValueError")
        sys.exit(1)
    except ValueError as e:
        print(f"   ✓ Correctly raised ValueError: {e}")

    # Test 5: Test with empty directory (should use fallback)
    print("\n5. Testing with empty directory (should use fallback)...")
    result = node.log_to_csv(
        id="img_003",
        prompt="Using fallback directory",
        prompt1="default location",
        prompt_neg="custom path",
        shift="1.0",
        seed="55555",
        directory="",
        csv_filename="fallback_test.csv"
    )
    print(f"   ✓ Used fallback directory successfully")
    # Clean up fallback test file
    fallback_path = os.path.join(tempfile.gettempdir(), "fallback_test.csv")
    if os.path.exists(fallback_path):
        os.remove(fallback_path)

    # Verify the CSV contents
    print("\n" + "=" * 60)
    print("CSV File Contents:")
    print("=" * 60)

    with open(test_csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        print(f"\nTotal rows: {len(rows)}")
        print(f"CSV location: {test_csv_path}")
        print("\nRow details:")
        for i, row in enumerate(rows, 1):
            print(f"\n  Row {i}:")
            print(f"    ID: {row['id']}")
            print(f"    Prompt: {row['prompt'][:50]}...")
            print(f"    Shift: {row['shift']}")
            print(f"    Seed: {row['seed']}")

    # Verify expectations
    print("\n" + "=" * 60)
    print("Verification:")
    print("=" * 60)

    assert len(rows) == 2, f"Expected 2 rows, got {len(rows)}"
    print("✓ Row count is correct (2 rows)")

    # Check that id='img_001' was updated
    row_001 = next((r for r in rows if r['id'] == 'img_001'), None)
    assert row_001 is not None, "ID 'img_001' not found"
    assert row_001['prompt'] == "An UPDATED sunset scene", "ID 'img_001' was not updated"
    assert row_001['seed'] == "99999", "ID 'img_001' seed was not updated"
    print("✓ ID 'img_001' was successfully updated")

    # Check that id='img_002' exists
    row_002 = next((r for r in rows if r['id'] == 'img_002'), None)
    assert row_002 is not None, "ID 'img_002' not found"
    print("✓ ID 'img_002' exists")

    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
    print(f"\nTest CSV location: {test_csv_path}")

if __name__ == "__main__":
    try:
        test_updated_node()
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
