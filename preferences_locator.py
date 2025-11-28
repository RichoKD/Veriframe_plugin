"""
VeriFrame Addon Preferences Locator
Run this script in Blender to find and access VeriFrame preferences
"""

import bpy
import addon_utils

def find_veriframe_preferences():
    """Locate and access VeriFrame addon preferences"""
    
    print("🔍 VeriFrame Preferences Locator")
    print("=" * 40)
    
    # Method 1: Check enabled addons
    enabled_addons = bpy.context.preferences.addons.keys()
    veriframe_addons = [name for name in enabled_addons if 'veriframe' in name.lower()]
    
    print(f"📦 Enabled addons containing 'veriframe': {veriframe_addons}")
    
    if not veriframe_addons:
        print("❌ No VeriFrame addon found in enabled addons!")
        print("\n📋 Steps to enable:")
        print("1. Edit > Preferences > Add-ons")
        print("2. Search for 'VeriFrame' or 'veriframe'")
        print("3. Check the checkbox to enable")
        return False
    
    # Method 2: Try to access preferences
    addon_name = veriframe_addons[0]
    print(f"✅ Found addon: {addon_name}")
    
    try:
        addon_prefs = bpy.context.preferences.addons[addon_name].preferences
        print("✅ Preferences accessible!")
        
        # Test preference properties
        if hasattr(addon_prefs, 'default_wallet_address'):
            print(f"   Default wallet: {addon_prefs.default_wallet_address}")
        if hasattr(addon_prefs, 'default_rpc_url'):
            print(f"   Default RPC: {addon_prefs.default_rpc_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Could not access preferences: {e}")
        return False

def show_preferences_location():
    """Show step-by-step instructions to find preferences"""
    
    print("\n🎯 HOW TO FIND VERIFRAME PREFERENCES:")
    print("-" * 40)
    print("1. 📋 Go to Edit > Preferences (or Blender > Preferences on macOS)")
    print("2. 🔧 Click on 'Add-ons' in the left sidebar")
    print("3. 🔍 Search for 'VeriFrame' in the search box")
    print("4. 📂 Look for 'VeriFrame' in the results")
    print("5. ▼ Click the dropdown arrow next to the addon name")
    print("6. ⚙️  The preferences panel will appear below")
    
    print("\n💡 ALTERNATIVE METHOD:")
    print("- Filter by category: Render")
    print("- Look for 'VeriFrame' in the Render category")

def open_preferences_automatically():
    """Try to automatically open the preferences"""
    
    try:
        # Switch to preferences
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
        
        # Try to filter to addons
        prefs = bpy.context.preferences
        prefs.active_section = 'ADDONS'
        
        print("✅ Opened Blender Preferences automatically")
        print("Now search for 'VeriFrame' in the Add-ons section")
        
        return True
        
    except Exception as e:
        print(f"⚠️  Could not open preferences automatically: {e}")
        return False

def test_addon_registration():
    """Test if the addon is properly registered"""
    
    print("\n🧪 ADDON REGISTRATION TEST:")
    print("-" * 30)
    
    # Check bl_info
    try:
        from . import bl_info
        print(f"✅ Addon name: {bl_info.get('name', 'Unknown')}")
        print(f"✅ Addon category: {bl_info.get('category', 'Unknown')}")
    except:
        print("⚠️  Could not access bl_info")
    
    # Check if VeriFramePreferences class exists
    if hasattr(bpy.types, 'VeriFramePreferences'):
        print("✅ VeriFramePreferences class is registered")
        
        # Get the bl_idname
        prefs_class = bpy.types.VeriFramePreferences
        if hasattr(prefs_class, 'bl_idname'):
            print(f"✅ Preferences bl_idname: {prefs_class.bl_idname}")
        
    else:
        print("❌ VeriFramePreferences class NOT registered")
        print("This is why you can't see the preferences!")
    
    # List all addon preferences
    print("\n📋 All registered addon preferences:")
    for cls_name in dir(bpy.types):
        if cls_name.endswith('Preferences'):
            cls = getattr(bpy.types, cls_name)
            if hasattr(cls, 'bl_idname'):
                print(f"   - {cls_name} (bl_idname: {cls.bl_idname})")

def fix_preferences_access():
    """Provide fixes for common preferences issues"""
    
    print("\n🔧 TROUBLESHOOTING STEPS:")
    print("-" * 25)
    
    # Check if addon is actually enabled
    addon_utils_mods = addon_utils.modules(refresh=False)
    veriframe_mod = None
    
    for mod in addon_utils_mods:
        if hasattr(mod, '__name__') and 'veriframe' in mod.__name__.lower():
            veriframe_mod = mod
            break
    
    if veriframe_mod:
        is_enabled = addon_utils.check(veriframe_mod.__name__)[1]
        print(f"✅ Addon module found: {veriframe_mod.__name__}")
        print(f"{'✅' if is_enabled else '❌'} Addon enabled: {is_enabled}")
        
        if not is_enabled:
            print("\n🔄 To enable the addon:")
            print("1. Go to Edit > Preferences > Add-ons")
            print("2. Find VeriFrame and check the checkbox")
            print("3. The preferences should appear below")
    else:
        print("❌ VeriFrame addon module not found")
        print("The addon may not be properly installed")
    
    print("\n🔄 If preferences still don't show:")
    print("1. Disable and re-enable the addon")
    print("2. Restart Blender")
    print("3. Reinstall the addon")
    print("4. Check Console for error messages")

if __name__ == "__main__":
    print("🚀 VeriFrame Preferences Diagnostic Tool")
    
    # Run all diagnostic functions
    found_prefs = find_veriframe_preferences()
    show_preferences_location()
    
    if not found_prefs:
        test_addon_registration()
        fix_preferences_access()
    
    # Try to open preferences automatically
    print("\n🎯 Attempting to open preferences...")
    if open_preferences_automatically():
        print("✅ Preferences should now be open - search for 'VeriFrame'")
    else:
        print("❌ Could not open preferences automatically")
        print("Please open manually: Edit > Preferences > Add-ons")
    
    print("\n📋 SUMMARY:")
    print("If you still can't find VeriFrame preferences:")
    print("1. Make sure the addon is enabled (checkbox checked)")
    print("2. Look for the dropdown arrow next to 'VeriFrame'")
    print("3. Click the arrow to expand preferences")
    print("4. Check Console for any error messages")