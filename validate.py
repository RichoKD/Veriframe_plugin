#!/usr/bin/env python3
"""
VeriFrame Blender Plugin Validation Script
Validates the plugin structure and requirements before packaging
"""

import os
import sys
import json
from pathlib import Path

def validate_plugin_structure():
    """Validate the plugin directory structure"""
    
    print("🔍 Validating plugin structure...")
    
    addon_dir = Path("veriframe_addon")
    if not addon_dir.exists():
        print("❌ Error: veriframe_addon directory not found!")
        return False
    
    required_files = [
        "__init__.py",
        "properties.py", 
        "operators.py",
        "panels.py",
        "preferences.py",
        "utils.py",
        "config.py",
        "blender_manifest.toml"
    ]
    
    missing_files = []
    for file in required_files:
        if not (addon_dir / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files present")
    return True

def validate_python_syntax():
    """Validate Python syntax in all Python files"""
    
    print("🐍 Validating Python syntax...")
    
    addon_dir = Path("veriframe_addon")
    python_files = list(addon_dir.glob("*.py"))
    
    syntax_errors = []
    
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), py_file, 'exec')
        except SyntaxError as e:
            syntax_errors.append(f"{py_file}: {e}")
    
    if syntax_errors:
        print("❌ Python syntax errors found:")
        for error in syntax_errors:
            print(f"   {error}")
        return False
    
    print(f"✅ All {len(python_files)} Python files have valid syntax")
    return True

def validate_blender_manifest():
    """Validate the Blender manifest file"""
    
    print("📋 Validating Blender manifest...")
    
    manifest_path = Path("veriframe_addon/blender_manifest.toml")
    if not manifest_path.exists():
        print("❌ Error: blender_manifest.toml not found!")
        return False
    
    try:
        # Basic validation - in a real scenario you'd use a TOML parser
        with open(manifest_path, 'r') as f:
            content = f.read()
            
        required_fields = [
            "schema_version", "id", "name", "version", 
            "type", "blender_version_min"
        ]
        
        missing_fields = []
        for field in required_fields:
            if f'"{field}"' not in content:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing manifest fields: {missing_fields}")
            return False
            
        print("✅ Manifest file is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error reading manifest: {e}")
        return False

def validate_documentation():
    """Validate documentation files"""
    
    print("📚 Validating documentation...")
    
    required_docs = [
        "README.md",
        "PLUGIN_README.md", 
        "INSTALLATION.md",
        "CHANGELOG.md",
        "LICENSE"
    ]
    
    missing_docs = []
    for doc in required_docs:
        if not Path(doc).exists():
            missing_docs.append(doc)
    
    if missing_docs:
        print(f"❌ Missing documentation: {missing_docs}")
        return False
    
    # Check if docs have content
    empty_docs = []
    for doc in required_docs:
        if Path(doc).stat().st_size < 100:  # Less than 100 bytes
            empty_docs.append(doc)
    
    if empty_docs:
        print(f"⚠️  Warning: Very small documentation files: {empty_docs}")
    
    print("✅ All documentation present")
    return True

def validate_addon_info():
    """Validate addon bl_info in __init__.py"""
    
    print("ℹ️  Validating addon info...")
    
    init_file = Path("veriframe_addon/__init__.py")
    if not init_file.exists():
        print("❌ Error: __init__.py not found!")
        return False
    
    try:
        with open(init_file, 'r') as f:
            content = f.read()
        
        if "bl_info" not in content:
            print("❌ Error: bl_info not found in __init__.py!")
            return False
        
        required_bl_info = [
            '"name"', '"author"', '"version"', '"blender"',
            '"location"', '"description"', '"category"'
        ]
        
        missing_info = []
        for info in required_bl_info:
            if info not in content:
                missing_info.append(info)
        
        if missing_info:
            print(f"❌ Missing bl_info fields: {missing_info}")
            return False
        
        print("✅ Addon info is complete")
        return True
        
    except Exception as e:
        print(f"❌ Error reading __init__.py: {e}")
        return False

def check_file_sizes():
    """Check for reasonable file sizes"""
    
    print("📏 Checking file sizes...")
    
    addon_dir = Path("veriframe_addon")
    large_files = []
    total_size = 0
    
    for file_path in addon_dir.rglob("*"):
        if file_path.is_file():
            size = file_path.stat().st_size
            total_size += size
            
            # Flag files larger than 1MB
            if size > 1024 * 1024:
                large_files.append((file_path, size))
    
    if large_files:
        print("⚠️  Large files detected:")
        for file_path, size in large_files:
            print(f"   {file_path}: {size / (1024*1024):.1f} MB")
    
    print(f"📦 Total addon size: {total_size / 1024:.1f} KB")
    
    if total_size > 10 * 1024 * 1024:  # 10MB
        print("⚠️  Warning: Addon is quite large (>10MB)")
    
    return True

def validate_requirements():
    """Validate requirements.txt"""
    
    print("📋 Validating requirements...")
    
    req_file = Path("requirements.txt")
    if not req_file.exists():
        print("⚠️  Warning: requirements.txt not found")
        return True
    
    try:
        with open(req_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        if not lines:
            print("⚠️  Warning: requirements.txt is empty")
        else:
            print(f"✅ Found {len(lines)} requirements")
            
        return True
        
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def main():
    """Run all validation checks"""
    
    print("🚀 VeriFrame Blender Plugin Validation")
    print("=====================================")
    
    checks = [
        ("Plugin Structure", validate_plugin_structure),
        ("Python Syntax", validate_python_syntax),
        ("Blender Manifest", validate_blender_manifest),
        ("Documentation", validate_documentation), 
        ("Addon Info", validate_addon_info),
        ("File Sizes", check_file_sizes),
        ("Requirements", validate_requirements)
    ]
    
    passed = 0
    failed = 0
    
    for check_name, check_func in checks:
        print(f"\n--- {check_name} ---")
        try:
            if check_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Check failed with exception: {e}")
            failed += 1
    
    print(f"\n{'='*40}")
    print(f"📊 Validation Results:")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 All validations passed! Plugin is ready for packaging.")
        return 0
    else:
        print(f"\n⚠️  {failed} validation(s) failed. Please fix issues before packaging.")
        return 1

if __name__ == "__main__":
    sys.exit(main())