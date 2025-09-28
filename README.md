# VeriFrame Blender Plugin

A Blender addon for the VeriFrame decentralized rendering platform. This plugin allows users to submit Blender rendering jobs directly to the VeriFrame network from within Blender.

## Overview

VeriFrame is a blockchain-powered platform that connects 3D artists with distributed rendering workers. This Blender plugin provides seamless integration, allowing you to:

- Submit render jobs directly from Blender
- Connect your Starknet wallet for payments
- Track job progress in real-time
- Download completed renders automatically
- Manage job history and settings

## Quick Start

1. **Install the Plugin**: Follow the [Installation Guide](INSTALLATION.md)
2. **Read the Documentation**: See [Plugin README](PLUGIN_README.md) for detailed usage
3. **Learn about VeriFrame**: Check out the [Platform Overview](Platform.md)

## Features

### 🎨 Blender Integration
- Native Blender addon with intuitive UI
- Supports Cycles, Eevee, and Workbench render engines
- Automatic scene validation and optimization
- Multiple output formats (PNG, JPEG, EXR, TIFF)

### 🔗 Blockchain Integration
- Starknet wallet connectivity
- Smart contract interaction for job submission
- Automatic payment handling with STRK tokens
- Transparent and verifiable transactions

### 📁 Decentralized Storage
- IPFS integration for file upload/download
- Automatic asset packing and optimization
- Secure and distributed file storage
- Fast global content delivery

### 📊 Job Management
- Real-time job status tracking
- Comprehensive job history
- Download management and organization
- Statistics and analytics

## Installation

### Prerequisites
- Blender 4.0+
- IPFS node (local or remote)
- Starknet wallet with STRK tokens

### Quick Install
```bash
git clone https://github.com/RichoKD/Veriframe_plugin.git
# Follow installation instructions in INSTALLATION.md
```

## Usage

1. **Open Blender** and navigate to Render Properties
2. **Find VeriFrame Panel** and connect your wallet
3. **Configure job settings** (reward, deadline, render engine)
4. **Submit your job** and track progress
5. **Download results** when completed

For detailed usage instructions, see [PLUGIN_README.md](PLUGIN_README.md).

## Project Structure

```
veriframe_addon/
├── __init__.py              # Main addon entry point
├── properties.py            # Blender properties and data structures
├── operators.py             # User actions and operations
├── panels.py               # UI panels and layouts
├── preferences.py          # Addon preferences and settings
├── utils.py                # Utility functions and managers
├── config.py               # Configuration constants
└── blender_manifest.toml   # Addon manifest
```

## Development

### Setting up Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RichoKD/Veriframe_plugin.git
   cd Veriframe_plugin
   ```

2. **Create development link**:
   ```bash
   ln -s $(pwd)/veriframe_addon ~/.config/blender/4.0/scripts/addons/veriframe_addon
   ```

3. **Enable developer mode** in Blender preferences

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly with different scenes
5. Submit a pull request

## Documentation

- [**Installation Guide**](INSTALLATION.md) - Step-by-step setup instructions
- [**Plugin Documentation**](PLUGIN_README.md) - Comprehensive usage guide
- [**Platform Overview**](Platform.md) - VeriFrame platform documentation

## Support

- **Issues**: [GitHub Issues](https://github.com/RichoKD/Veriframe_plugin/issues)
- **Documentation**: [Plugin README](PLUGIN_README.md)
- **Community**: [VeriFrame Discord](https://discord.gg/veriframe)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [VeriFrame Platform](https://github.com/RichoKD/VeriFrame) - Main platform repository
- [VeriFrame Contracts](https://github.com/RichoKD/VeriFrame/tree/main/contracts) - Smart contracts
- [VeriFrame Worker](https://github.com/RichoKD/VeriFrame/tree/main/worker) - Worker node implementation