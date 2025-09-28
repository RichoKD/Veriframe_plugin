# VeriFrame Blender Plugin

A Blender addon that enables users to submit rendering jobs directly to the VeriFrame decentralized network from within Blender.

## Features

- **Direct Blender Integration**: Submit render jobs without leaving Blender
- **Wallet Integration**: Connect your Starknet wallet for seamless transactions
- **IPFS Integration**: Automatic file upload and download via IPFS
- **Job Management**: Track job status and download completed renders
- **Scene Validation**: Automatic scene validation before submission
- **Flexible Settings**: Configure render engines, output formats, and network settings

## Installation

### Prerequisites

1. **Blender 4.0+**: Download from [blender.org](https://www.blender.org/)
2. **IPFS Node**: Install and run IPFS locally
   ```bash
   # Install IPFS
   wget https://dist.ipfs.io/go-ipfs/v0.13.0/go-ipfs_v0.13.0_linux-amd64.tar.gz
   tar -xvzf go-ipfs_v0.13.0_linux-amd64.tar.gz
   cd go-ipfs
   sudo ./install.sh
   
   # Initialize and start IPFS
   ipfs init
   ipfs daemon
   ```

3. **Starknet Wallet**: Set up a Starknet wallet (e.g., ArgentX, Braavos)

### Installing the Plugin

1. **Download the Plugin**
   ```bash
   git clone https://github.com/RichoKD/Veriframe_plugin.git
   cd Veriframe_plugin
   ```

2. **Install in Blender**
   - Open Blender
   - Go to `Edit > Preferences > Add-ons`
   - Click `Install...`
   - Navigate to the `veriframe_addon` folder and select it
   - Enable the "VeriFrame" addon

3. **Configure Settings**
   - In Blender preferences, find "VeriFrame" in the addon list
   - Click the dropdown arrow to expand settings
   - Enter your Starknet wallet address
   - Configure IPFS endpoints if using custom setup

## Usage

### Getting Started

1. **Open Blender** and create or open your scene
2. **Go to Properties Panel** → **Render Properties**
3. **Find the VeriFrame panel** (expand if collapsed)

### Connecting Your Wallet

1. In the VeriFrame panel, click **"Connect Wallet"**
2. Ensure your wallet address is configured in preferences
3. The panel will show "Connected" status when successful

### Submitting a Render Job

1. **Configure Job Settings**:
   - **Reward Amount**: Set the STRK token reward for workers
   - **Deadline**: Set job deadline in hours
   - **Render Engine**: Choose Cycles, Eevee, or Workbench
   - **Output Format**: Select PNG, JPEG, EXR, or TIFF

2. **Submit Job**:
   - Click **"Submit Job"** button
   - The plugin will:
     - Pack external files into the blend file
     - Upload to IPFS
     - Submit to the VeriFrame contract
     - Add job to your history

### Managing Jobs

1. **View Job History**:
   - Expand the "Job History" section
   - See all submitted jobs with their status

2. **Refresh Job Status**:
   - Click the refresh icon next to individual jobs
   - Or use "Refresh All" to update all jobs

3. **Download Results**:
   - When a job is completed, click the download icon
   - Results are saved to `veriframe_downloads` folder in your project

### Advanced Settings

Expand "Advanced Settings" to configure:
- **RPC URL**: Starknet network endpoint
- **Contract Address**: VeriFrame contract address
- **IPFS Settings**: API and gateway URLs

## Configuration

### Network Settings

The plugin supports both Sepolia testnet and mainnet:

- **Sepolia (Default)**:
  - RPC: `https://api.cartridge.gg/x/starknet/sepolia` 
  - Contract: `0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8`

- **Mainnet** (when deployed):
  - RPC: `https://api.cartridge.gg/x/starknet/mainnet`

### IPFS Configuration

Default local IPFS settings:
- **API**: `http://127.0.0.1:5001`
- **Gateway**: `http://127.0.0.1:8080`

For remote IPFS nodes, update these URLs in preferences.

## Features in Detail

### Scene Validation

The plugin automatically validates your scene before submission:
- **External Files**: Checks for unpacked images and textures
- **Resolution**: Warns about very high resolutions
- **Sample Count**: Alerts for excessive Cycles samples
- **Materials**: Identifies objects without materials

### Job Tracking

- **Real-time Status**: Jobs update from PENDING → IN_PROGRESS → COMPLETED
- **History Management**: Keeps track of all submitted jobs
- **Auto-refresh**: Optionally refresh job status automatically
- **Statistics**: View completion rates and total spending

### File Management

- **Automatic Packing**: External assets are packed before upload
- **Compression**: Files are optimized for network transfer  
- **Download Management**: Results are organized in dated folders
- **Cleanup**: Temporary files are automatically removed

## Troubleshooting

### Common Issues

1. **"IPFS connection failed"**
   - Ensure IPFS daemon is running: `ipfs daemon`
   - Check API URL in advanced settings
   - Verify firewall allows port 5001

2. **"Wallet not connected"**
   - Check wallet address in preferences
   - Ensure address format is correct (0x...)
   - Try refreshing the connection

3. **"Job submission failed"**
   - Verify you have sufficient STRK tokens
   - Check network connectivity
   - Ensure contract address is correct

4. **"Large file upload timeout"**
   - Reduce scene complexity
   - Pack only necessary assets
   - Use lower resolution textures

### Debug Information

Enable "Show Debug Information" in preferences to see:
- Detailed error messages
- Network request logs
- File upload progress
- Contract interaction details

### Log Files

Plugin logs are written to:
- **Windows**: `%APPDATA%\Blender Foundation\Blender\scripts\addons\veriframe_addon\logs`
- **macOS**: `~/Library/Application Support/Blender/scripts/addons/veriframe_addon/logs`
- **Linux**: `~/.config/blender/scripts/addons/veriframe_addon/logs`

## Limitations

### Current Version (1.0.0)

- **Wallet Integration**: Currently simulated, full wallet integration in development
- **Network**: Only Sepolia testnet supported initially
- **File Size**: Maximum 500MB blend files
- **Animation**: Single frame rendering only
- **Asset Library**: Custom assets must be packed manually

### Planned Features

- Full Starknet wallet integration
- Batch/animation rendering
- Asset marketplace integration
- Advanced render settings
- Mobile notifications
- Worker node ratings

## Development

### Building from Source

1. **Clone Repository**:
   ```bash
   git clone https://github.com/RichoKD/Veriframe_plugin.git
   cd Veriframe_plugin
   ```

2. **Development Setup**:
   ```bash
   # Create symbolic link for development
   ln -s $(pwd)/veriframe_addon ~/.config/blender/scripts/addons/veriframe_addon
   ```

3. **Testing**:
   - Reload addon in Blender: `F3` → "Reload Scripts"
   - Check console for errors: `Window` → `Toggle System Console`

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit a pull request

### Code Structure

```
veriframe_addon/
├── __init__.py          # Main addon registration
├── properties.py        # Blender properties and data
├── operators.py         # User actions and operations
├── panels.py           # UI panels and layout
├── preferences.py      # Addon preferences
├── utils.py           # Utility functions
└── config.py          # Configuration constants
```

## Support

- **Documentation**: [VeriFrame Docs](https://github.com/RichoKD/VeriFrame)
- **Issues**: [GitHub Issues](https://github.com/RichoKD/Veriframe_plugin/issues)
- **Community**: [Discord](https://discord.gg/veriframe)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Starknet](https://starknet.io/) for the L2 platform
- [IPFS](https://ipfs.io/) for decentralized storage
- [Blender Foundation](https://www.blender.org/) for the open-source 3D suite
- VeriFrame community for feedback and testing