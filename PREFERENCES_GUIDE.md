# VeriFrame Addon Preferences - Location Guide

## 📍 Where to Find VeriFrame Preferences

### Step-by-Step Instructions:

1. **Open Blender Preferences**
   - Go to `Edit` → `Preferences...`
   - (On macOS: `Blender` → `Preferences...`)

2. **Navigate to Add-ons Section**
   - Click on `Add-ons` in the left sidebar
   - You should see a search box at the top

3. **Find VeriFrame Addon**
   - Type `VeriFrame` in the search box
   - OR filter by category: select `Render` from the dropdown
   - Look for "VeriFrame" in the results

4. **Access Preferences**
   - Find the VeriFrame addon entry
   - **Click the dropdown arrow (▼)** next to the addon name
   - The preferences panel will expand below

5. **Configure Settings**
   - Enter your Starknet wallet address
   - Configure network and IPFS settings if needed
   - Click "Save Preferences" when done

## 🔍 If You Can't Find the Addon

### Check if VeriFrame is Enabled:
- Look for a **checkbox** next to "VeriFrame"
- If unchecked, **click the checkbox** to enable it
- The preferences should appear below after enabling

### Alternative Search Methods:
1. **Search by name**: Type "VeriFrame" or "veriframe"
2. **Browse by category**: Select "Render" category
3. **Show all**: Clear the search box and scroll through all addons

### Visual Indicators:
- ✅ **Enabled addon**: Checkbox is checked, preferences visible below
- ❌ **Disabled addon**: Checkbox is unchecked, no preferences shown
- 🔍 **Not found**: Addon may not be installed properly

## 🛠️ Troubleshooting

### If VeriFrame doesn't appear in the list:
1. **Check installation**:
   - Verify the `veriframe_addon` folder is in your Blender addons directory
   - Restart Blender after installation

2. **Check for errors**:
   - Open Blender Console: `Window` → `Toggle System Console`
   - Look for error messages when enabling the addon

3. **Reinstall if needed**:
   - Disable the addon (uncheck box)
   - Remove the `veriframe_addon` folder
   - Reinstall using the provided packages

### If preferences don't show after enabling:
1. **Refresh the addon list**:
   - Click the "Refresh" button in the Add-ons preferences
   - Or restart Blender

2. **Check the dropdown arrow**:
   - Look for a small arrow (▼) next to "VeriFrame"
   - Click it to expand the preferences

## 📂 Addon Directory Locations

Your Blender addons are located at:

- **Windows**: `%APPDATA%\Blender Foundation\Blender\4.0\scripts\addons\`
- **macOS**: `~/Library/Application Support/Blender/4.0/scripts/addons/`
- **Linux**: `~/.config/blender/4.0/scripts/addons/`

The VeriFrame addon should be in a folder named `veriframe_addon` in this directory.

## ⚙️ Preference Options

Once you find the VeriFrame preferences, you can configure:

- **Default Wallet Address**: Your Starknet wallet address
- **Network Settings**: RPC URL and contract address
- **IPFS Settings**: API and gateway URLs
- **UI Options**: Debug mode, auto-save settings

## 🎯 Quick Test

Run this in Blender's Python Console to test:
```python
import bpy
# Check if addon is enabled
print("veriframe_addon" in bpy.context.preferences.addons)
# Check if preferences are accessible
if "veriframe_addon" in bpy.context.preferences.addons:
    prefs = bpy.context.preferences.addons["veriframe_addon"].preferences
    print("Preferences found!")
```

## 📞 Still Need Help?

If you still can't find the preferences:
1. Run the included `preferences_locator.py` script
2. Check the Console for error messages
3. Try the automatic installer script
4. Report the issue with your Blender version and OS