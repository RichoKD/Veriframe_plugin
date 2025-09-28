# Changelog

All notable changes to the VeriFrame Blender Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-09-28

### Added
- Initial release of the VeriFrame Blender Plugin
- Core plugin architecture with modular design
- Blender 4.0+ compatibility
- Starknet wallet integration (simulated for v1.0)
- IPFS file upload and download functionality
- Job submission and tracking system
- Real-time job status monitoring
- Comprehensive UI in Render Properties panel
- Scene validation and optimization
- Multiple render engine support (Cycles, Eevee, Workbench)
- Multiple output format support (PNG, JPEG, EXR, TIFF)
- Job history management and statistics
- Auto-refresh functionality for job status
- Advanced network and IPFS configuration
- Comprehensive addon preferences
- Debug mode and logging
- Automatic file packing for external assets
- Download management with organized folders
- Error handling and user feedback
- Complete documentation and installation guides
- Packaging and distribution scripts
- Example usage and testing scripts

### Features
- **Direct Blender Integration**: Submit jobs without leaving Blender
- **Wallet Connectivity**: Connect Starknet wallets for payments
- **IPFS Storage**: Decentralized file storage and retrieval
- **Job Management**: Track and manage rendering jobs
- **Scene Validation**: Automatic scene optimization
- **Flexible Configuration**: Customize network and storage settings
- **User-Friendly UI**: Intuitive panels and controls
- **Comprehensive Logging**: Debug information and error tracking

### Technical Details
- Built with Blender Python API (bpy)
- Modular architecture for easy maintenance
- RESTful API integration for IPFS
- Smart contract interaction framework
- Type hints and comprehensive documentation
- Error handling and graceful degradation
- Cross-platform compatibility (Windows, macOS, Linux)

### Documentation
- Complete installation guide
- Comprehensive user manual
- Developer documentation
- API reference
- Troubleshooting guide
- Example scripts and usage demos

### Known Limitations
- Wallet integration is simulated (full integration in v1.1)
- Single frame rendering only (animation support in v1.2)
- Maximum 500MB file size limit
- Sepolia testnet only for initial release

### Dependencies
- Blender 4.0+
- Python 3.10+ (included with Blender)
- requests library for HTTP operations
- IPFS node for file storage
- Starknet wallet for payments

## [Unreleased]

### Planned for v1.1
- Full Starknet wallet integration using starknet.py
- Mainnet support
- Enhanced error handling and recovery
- Performance optimizations
- Additional render settings
- Batch job submission
- Mobile notifications

### Planned for v1.2
- Animation rendering support
- Advanced asset management
- Worker node ratings and selection
- Custom render farm integration
- Asset marketplace integration
- Advanced statistics and analytics

### Planned for v1.3
- Real-time collaboration features
- Advanced scene analysis
- Custom shader networks
- GPU optimization
- Advanced file compression
- Multi-language support

## Security

### v1.0.0 Security Features
- Input validation for all user data
- Secure file handling and temporary cleanup
- Safe external process execution
- Network request timeout and error handling
- User data privacy protection

### Known Security Considerations
- IPFS files are publicly accessible
- Wallet integration requires user trust
- Network communication is not encrypted by default
- File upload size limits to prevent abuse

## Support and Compatibility

### Supported Blender Versions
- Blender 4.0.0 and above
- Tested with Blender 4.1.x

### Supported Platforms
- Windows 10/11 (x64)
- macOS 10.15+ (Intel and Apple Silicon)
- Linux (Ubuntu 20.04+, other distributions)

### Network Support
- Starknet Sepolia Testnet
- IPFS (local or remote nodes)
- Custom RPC endpoints

## Migration Guide

### From Development to v1.0.0
- No migration needed for new installations
- Follow standard installation procedures

### Future Migration Notes
- Upgrade guides will be provided for major versions
- Backward compatibility maintained where possible
- Data migration tools for job history

## Contributors

- VeriFrame Team - Initial development
- Community contributors - Testing and feedback

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.