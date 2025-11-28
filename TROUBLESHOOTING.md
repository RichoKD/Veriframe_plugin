# VeriFrame Plugin Registration Troubleshooting

## Common Registration Errors and Solutions

### Error: "already registered as a subclass 'VeriFramePreferences'"

**Cause**: The `bl_idname` in the preferences class doesn't match the addon folder name exactly.

**Solution**: ✅ **FIXED** - Updated `preferences.py`:
```python
class VeriFramePreferences(AddonPreferences):
    bl_idname = "veriframe_addon"  # Must match folder name exactly
```

### Error: "'jobs' CollectionProperty could not register"

**Cause**: The `VeriFrameJobItem` class wasn't registered before `VeriFrameProperties` that references it.

**Solution**: ✅ **FIXED** - Updated registration order in `__init__.py`:
```python
classes = (
    preferences.VeriFramePreferences,
    properties.VeriFrameJobItem,      # Must be first
    properties.VeriFrameProperties,   # References VeriFrameJobItem
    # ... other classes
)
```

## Installation Verification

After installing the plugin, you can verify it's working correctly:

### 1. Check Console Output
When enabling the addon, you should see:
```
✅ Registered: VeriFramePreferences
✅ Registered: VeriFrameJobItem
✅ Registered: VeriFrameProperties
✅ Registered: VF_OT_SubmitJob
✅ Registered: VF_OT_CheckJobStatus
✅ Registered: VF_OT_DownloadResult
✅ Registered: VF_OT_ConnectWallet
✅ Registered: VF_OT_RefreshJobs
✅ Registered: VF_PT_MainPanel
✅ Registered: VF_PT_JobHistoryPanel
```

### 2. Check UI Panel
- Go to **Properties** → **Render Properties**
- Look for **VeriFrame** panel
- Panel should expand without errors

### 3. Run Test Script
Copy and run this in Blender's Text Editor:
```python
import bpy

# Test if properties are available
props = bpy.context.scene.veriframe
print(f"Reward amount: {props.reward_amount}")

# Test if operators are available
print("Available operators:")
for op in ['connect_wallet', 'submit_job', 'check_job_status']:
    if hasattr(bpy.ops.veriframe, op):
        print(f"  ✅ veriframe.{op}")
    else:
        print(f"  ❌ veriframe.{op}")
```

## Clean Installation Steps

If you're having persistent issues:

### 1. Complete Uninstall
```python
# In Blender Console
import addon_utils
addon_utils.disable("veriframe_addon", default_set=True)
```

### 2. Remove Files
- Close Blender
- Delete the addon folder from your addons directory
- Restart Blender

### 3. Fresh Install
- Extract the new package
- Copy `veriframe_addon` folder to addons directory
- Restart Blender
- Enable the addon

## Debug Mode

Enable debug output by adding this to the top of `__init__.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Common File Locations

### Blender Addons Directory:
- **Linux**: `~/.config/blender/4.0/scripts/addons/`
- **Windows**: `%APPDATA%\Blender Foundation\Blender\4.0\scripts\addons\`
- **macOS**: `~/Library/Application Support/Blender/4.0/scripts/addons/`

### Console Access:
- **Windows**: `Window` → `Toggle System Console`
- **Linux/macOS**: Run Blender from terminal to see console output

## Still Having Issues?

1. Check Blender version (requires 4.0+)
2. Verify Python version (3.10+ recommended)
3. Check console for detailed error messages
4. Try the test registration script: `test_registration.py`
5. Report issues with console output and Blender version

The plugin has been tested and validated, so these fixes should resolve the registration errors you encountered.