# Installation Guide for VeriFrame Blender Plugin

## Quick Start

### Step 1: Install Prerequisites

1. **Install Blender 4.0+**
   ```bash
   # Ubuntu/Debian
   sudo snap install blender --classic
   
   # Or download from https://www.blender.org/download/
   ```

2. **Install and Start IPFS**
   ```bash
   # Download IPFS
   wget https://dist.ipfs.io/kubo/v0.18.1/kubo_v0.18.1_linux-amd64.tar.gz
   tar -xvzf kubo_v0.18.1_linux-amd64.tar.gz
   cd kubo
   sudo bash install.sh
   
   # Initialize IPFS
   ipfs init
   
   # Start IPFS daemon
   ipfs daemon
   ```

3. **Set up Starknet Wallet**
   - Install [ArgentX](https://www.argent.xyz/argent-x/) or [Braavos](https://braavos.app/)
   - Create wallet and get some Sepolia testnet tokens

### Step 2: Install the Plugin

#### Method 1: Direct Installation (Recommended)

1. **Download the plugin**:
   ```bash
   git clone https://github.com/RichoKD/Veriframe_plugin.git
   cd Veriframe_plugin
   ```

2. **Install in Blender**:
   - Open Blender
   - Go to `Edit` → `Preferences` → `Add-ons`
   - Click `Install...`
   - Select the entire `veriframe_addon` folder
   - Enable the "VeriFrame" checkbox

#### Method 2: Development Installation

1. **Clone to Blender addons directory**:
   ```bash
   # Linux
   git clone https://github.com/RichoKD/Veriframe_plugin.git ~/.config/blender/4.0/scripts/addons/veriframe_addon
   
   # Windows
   git clone https://github.com/RichoKD/Veriframe_plugin.git "%APPDATA%\Blender Foundation\Blender\4.0\scripts\addons\veriframe_addon"
   
   # macOS  
   git clone https://github.com/RichoKD/Veriframe_plugin.git "~/Library/Application Support/Blender/4.0/scripts/addons/veriframe_addon"
   ```

2. **Enable in Blender**:
   - Restart Blender
   - Go to `Edit` → `Preferences` → `Add-ons`
   - Search for "VeriFrame"
   - Enable the checkbox

### Step 3: Configure the Plugin

1. **Open Blender Preferences**:
   - `Edit` → `Preferences` → `Add-ons`
   - Find "VeriFrame" and click the dropdown arrow

2. **Configure Settings**:
   ```
   Default Wallet Address: [Your Starknet wallet address]
   Default RPC URL: https://api.cartridge.gg/x/starknet/sepolia
   Default Contract Address: 0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8
   Default IPFS API URL: http://127.0.0.1:5001
   Default IPFS Gateway URL: http://127.0.0.1:8080
   ```

3. **Save Preferences**: Click "Save Preferences"

### Step 4: First Use

1. **Open Blender** and create a simple scene
2. **Navigate to Render Properties**:
   - Properties panel → Render Properties (camera icon)
   - Find "VeriFrame" panel

3. **Connect Wallet**:
   - Click "Connect Wallet" button
   - Verify connection status

4. **Submit Test Job**:
   - Set reward amount (e.g., 1 STRK)
   - Set deadline (e.g., 24 hours)
   - Click "Submit Job"

## Detailed Configuration

### IPFS Configuration

#### Local IPFS Node (Recommended)
```bash
# Start IPFS with custom config
ipfs config Addresses.API /ip4/127.0.0.1/tcp/5001
ipfs config Addresses.Gateway /ip4/127.0.0.1/tcp/8080
ipfs daemon
```

#### Remote IPFS Node
If using a remote IPFS node:
1. Update API URL: `http://your-ipfs-node:5001`
2. Update Gateway URL: `http://your-ipfs-node:8080`

### Network Configuration

#### Sepolia Testnet (Default)
```
RPC URL: https://api.cartridge.gg/x/starknet/sepolia
Contract: 0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8
```

#### Alternative RPCs
- Alchemy: `https://starknet-sepolia.g.alchemy.com/v2/YOUR_KEY`
- Infura: `https://starknet-sepolia.infura.io/v3/YOUR_KEY`

### Wallet Setup

1. **Get Wallet Address**:
   - Open your Starknet wallet extension
   - Copy your wallet address (starts with 0x...)

2. **Get Test Tokens**:
   - Visit [Starknet Sepolia Faucet](https://faucet.goerli.starknet.io/)
   - Request test STRK tokens

3. **Configure in Plugin**:
   - Paste wallet address in preferences
   - Connect wallet in VeriFrame panel

## Troubleshooting Installation

### Common Issues

#### "Module not found" errors
```bash
# Install missing Python packages in Blender's Python
/path/to/blender/python/bin/python -m pip install requests
```

#### IPFS connection failed
```bash
# Check IPFS status
ipfs id

# Restart IPFS daemon
pkill ipfs
ipfs daemon
```

#### Blender can't find the addon
- Ensure the folder is named exactly `veriframe_addon`
- Check that `__init__.py` exists in the addon folder
- Restart Blender completely

#### Wallet connection issues
- Verify wallet address format (66 characters, starts with 0x)
- Check network connectivity
- Ensure RPC URL is accessible

### Debug Mode

Enable debug mode for detailed logging:
1. Go to VeriFrame preferences
2. Enable "Show Debug Information"
3. Check Blender console: `Window` → `Toggle System Console`

### Log Files

Find logs at:
- **Linux**: `~/.config/blender/4.0/scripts/addons/veriframe_addon/logs/`
- **Windows**: `%APPDATA%\Blender Foundation\Blender\4.0\scripts\addons\veriframe_addon\logs\`
- **macOS**: `~/Library/Application Support/Blender/4.0/scripts/addons/veriframe_addon/logs/`

## Updating the Plugin

### Git Update
```bash
cd /path/to/veriframe_addon
git pull origin main
```

### Manual Update
1. Download new version
2. Remove old `veriframe_addon` folder
3. Install new version
4. Restart Blender

## Uninstallation

1. **Disable Addon**:
   - `Edit` → `Preferences` → `Add-ons`
   - Find "VeriFrame" and uncheck it

2. **Remove Files**:
   ```bash
   # Linux
   rm -rf ~/.config/blender/4.0/scripts/addons/veriframe_addon
   
   # Windows
   rmdir /s "%APPDATA%\Blender Foundation\Blender\4.0\scripts\addons\veriframe_addon"
   
   # macOS
   rm -rf "~/Library/Application Support/Blender/4.0/scripts/addons/veriframe_addon"
   ```

## Getting Help

### Documentation
- Plugin README: [PLUGIN_README.md](PLUGIN_README.md)
- VeriFrame Platform: [Platform.md](Platform.md)

### Support Channels
- GitHub Issues: [Create Issue](https://github.com/RichoKD/Veriframe_plugin/issues)
- Discord: [VeriFrame Community](https://discord.gg/veriframe)

### System Requirements

**Minimum Requirements:**
- Blender 4.0+
- Python 3.10+ (included with Blender)
- 4GB RAM
- Internet connection
- 1GB free disk space

**Recommended:**
- Blender 4.1+
- 8GB+ RAM
- SSD storage
- Stable internet connection
- Dedicated GPU for local preview rendering

## Next Steps

After installation:
1. Read the [Usage Guide](PLUGIN_README.md#usage)
2. Try the [Quick Start Tutorial](PLUGIN_README.md#getting-started)
3. Join the [VeriFrame Community](https://discord.gg/veriframe)
4. Explore [Advanced Features](PLUGIN_README.md#features-in-detail)