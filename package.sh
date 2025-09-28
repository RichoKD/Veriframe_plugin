#!/bin/bash

# VeriFrame Blender Plugin Packaging Script
# This script packages the addon for distribution

set -e

PLUGIN_NAME="veriframe_addon"
VERSION="1.0.0"
OUTPUT_DIR="dist"
PACKAGE_NAME="${PLUGIN_NAME}_v${VERSION}"

echo "📦 Packaging VeriFrame Blender Plugin v${VERSION}"

# Create output directory
mkdir -p "${OUTPUT_DIR}"

# Clean previous builds
rm -rf "${OUTPUT_DIR}/${PACKAGE_NAME}"*

# Create package directory
mkdir -p "${OUTPUT_DIR}/${PACKAGE_NAME}"

# Copy addon files
echo "📁 Copying addon files..."
cp -r "${PLUGIN_NAME}" "${OUTPUT_DIR}/${PACKAGE_NAME}/"

# Copy documentation
echo "📄 Copying documentation..."
cp README.md "${OUTPUT_DIR}/${PACKAGE_NAME}/"
cp PLUGIN_README.md "${OUTPUT_DIR}/${PACKAGE_NAME}/"
cp INSTALLATION.md "${OUTPUT_DIR}/${PACKAGE_NAME}/"
cp LICENSE "${OUTPUT_DIR}/${PACKAGE_NAME}/"
cp requirements.txt "${OUTPUT_DIR}/${PACKAGE_NAME}/"

# Create installation script
echo "🔧 Creating installation script..."
cat > "${OUTPUT_DIR}/${PACKAGE_NAME}/install.py" << 'EOF'
#!/usr/bin/env python3
"""
VeriFrame Blender Plugin Installer
Run this script to automatically install the plugin in Blender
"""

import os
import shutil
import sys
from pathlib import Path

def get_blender_addons_path():
    """Get the Blender addons directory for the current platform"""
    
    if sys.platform.startswith('linux'):
        return Path.home() / '.config' / 'blender' / '4.0' / 'scripts' / 'addons'
    elif sys.platform.startswith('win'):
        import os
        appdata = os.environ.get('APPDATA', '')
        return Path(appdata) / 'Blender Foundation' / 'Blender' / '4.0' / 'scripts' / 'addons'
    elif sys.platform.startswith('darwin'):  # macOS
        return Path.home() / 'Library' / 'Application Support' / 'Blender' / '4.0' / 'scripts' / 'addons'
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

def install_plugin():
    """Install the VeriFrame plugin"""
    
    current_dir = Path(__file__).parent
    addon_source = current_dir / 'veriframe_addon'
    
    if not addon_source.exists():
        print("❌ Error: veriframe_addon directory not found!")
        return False
    
    try:
        addons_path = get_blender_addons_path()
        addon_dest = addons_path / 'veriframe_addon'
        
        # Create addons directory if it doesn't exist
        addons_path.mkdir(parents=True, exist_ok=True)
        
        # Remove existing installation
        if addon_dest.exists():
            print("🗑️  Removing existing installation...")
            shutil.rmtree(addon_dest)
        
        # Copy addon
        print("📦 Installing VeriFrame addon...")
        shutil.copytree(addon_source, addon_dest)
        
        print("✅ VeriFrame plugin installed successfully!")
        print(f"📁 Installed to: {addon_dest}")
        print("\nNext steps:")
        print("1. Start Blender")
        print("2. Go to Edit > Preferences > Add-ons")
        print("3. Search for 'VeriFrame' and enable it")
        print("4. Configure your wallet address in the addon preferences")
        
        return True
        
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 VeriFrame Blender Plugin Installer")
    print("====================================")
    
    if install_plugin():
        input("\nPress Enter to exit...")
    else:
        input("\nInstallation failed. Press Enter to exit...")
        sys.exit(1)
EOF

# Create ZIP package
echo "🗜️  Creating ZIP package..."
cd "${OUTPUT_DIR}"
zip -r "${PACKAGE_NAME}.zip" "${PACKAGE_NAME}/" -x "*.pyc" "*/__pycache__/*"

# Create TAR package
echo "🗜️  Creating TAR package..."
tar -czf "${PACKAGE_NAME}.tar.gz" "${PACKAGE_NAME}/"

# Generate checksums
echo "🔐 Generating checksums..."
sha256sum "${PACKAGE_NAME}.zip" > "${PACKAGE_NAME}.zip.sha256"
sha256sum "${PACKAGE_NAME}.tar.gz" > "${PACKAGE_NAME}.tar.gz.sha256"

cd ..

# Display results
echo ""
echo "✅ Packaging complete!"
echo "📦 Packages created:"
echo "   - ${OUTPUT_DIR}/${PACKAGE_NAME}.zip"
echo "   - ${OUTPUT_DIR}/${PACKAGE_NAME}.tar.gz"
echo ""
echo "📋 Package contents:"
echo "   - veriframe_addon/     (Blender addon)"
echo "   - README.md           (Project overview)"
echo "   - PLUGIN_README.md    (Plugin documentation)"
echo "   - INSTALLATION.md     (Installation guide)"
echo "   - LICENSE             (MIT license)"
echo "   - install.py          (Auto-installer)"
echo ""
echo "🚀 Ready for distribution!"

# Optional: Create release info
cat > "${OUTPUT_DIR}/release_info.md" << EOF
# VeriFrame Blender Plugin v${VERSION}

## Installation

### Automatic Installation (Recommended)
1. Download and extract the package
2. Run \`python install.py\` in the extracted folder
3. Start Blender and enable the addon

### Manual Installation
1. Download and extract the package
2. Copy \`veriframe_addon\` folder to your Blender addons directory
3. Enable the addon in Blender preferences

## Package Contents
- **veriframe_addon/**: Complete Blender addon
- **README.md**: Project overview and quick start
- **PLUGIN_README.md**: Comprehensive plugin documentation  
- **INSTALLATION.md**: Step-by-step installation guide
- **LICENSE**: MIT license terms
- **install.py**: Automatic installer script

## Checksums
- ZIP: \`$(cat ${PACKAGE_NAME}.zip.sha256)\`
- TAR: \`$(cat ${PACKAGE_NAME}.tar.gz.sha256)\`

## Requirements
- Blender 4.0+
- IPFS node (local or remote)
- Starknet wallet with STRK tokens

## Support
- Documentation: [Plugin README](PLUGIN_README.md)
- Issues: [GitHub Issues](https://github.com/RichoKD/Veriframe_plugin/issues)
- Community: [VeriFrame Discord](https://discord.gg/veriframe)
EOF

echo "📋 Release info: ${OUTPUT_DIR}/release_info.md"