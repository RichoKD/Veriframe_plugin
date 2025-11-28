"""
VeriFrame Plugin UI Location Guide
Run this script in Blender's Text Editor to help locate the VeriFrame UI
"""

import bpy

def check_veriframe_ui():
    """Check if VeriFrame UI components are properly registered and provide location guide"""
    
    print("🔍 VeriFrame UI Location Check")
    print("=" * 40)
    
    # Check if addon is enabled
    addon_name = "veriframe_addon"
    if addon_name not in bpy.context.preferences.addons:
        print("❌ VeriFrame addon is not enabled!")
        print("\n📋 To enable the addon:")
        print("1. Go to Edit > Preferences > Add-ons")
        print("2. Search for 'VeriFrame'")
        print("3. Check the checkbox to enable it")
        return False
    
    print("✅ VeriFrame addon is enabled")
    
    # Check if properties are available
    if not hasattr(bpy.context.scene, 'veriframe'):
        print("❌ VeriFrame properties not found!")
        print("Try reloading the addon or restarting Blender")
        return False
    
    print("✅ VeriFrame properties are available")
    
    # Check if panels are registered
    panel_classes = ['VF_PT_MainPanel', 'VF_PT_JobHistoryPanel']
    registered_panels = []
    
    for panel_class in panel_classes:
        if hasattr(bpy.types, panel_class):
            registered_panels.append(panel_class)
            print(f"✅ Panel {panel_class} is registered")
        else:
            print(f"❌ Panel {panel_class} is NOT registered")
    
    if not registered_panels:
        print("\n❌ No VeriFrame panels found!")
        return False
    
    # Provide UI location instructions
    print("\n🎯 WHERE TO FIND VERIFRAME UI:")
    print("-" * 30)
    print("1. 📋 Open Properties Panel (usually on the right side)")
    print("2. 🎥 Click the RENDER PROPERTIES tab (camera icon)")
    print("3. 📜 Scroll down to find 'VeriFrame' section")
    print("4. 📂 Click the arrow to expand the VeriFrame panel")
    
    print("\n🖼️  UI PATH: Properties > Render Properties > VeriFrame")
    
    # Check current workspace
    current_workspace = bpy.context.workspace.name
    print(f"\n📐 Current workspace: {current_workspace}")
    
    if current_workspace not in ['Shading', 'Layout', 'Modeling']:
        print("💡 TIP: Try switching to 'Shading' or 'Layout' workspace for better visibility")
    
    # Test property access
    try:
        props = bpy.context.scene.veriframe
        print(f"\n🔧 VeriFrame Properties Test:")
        print(f"   Reward Amount: {props.reward_amount}")
        print(f"   Job Deadline: {props.job_deadline} hours")
        print(f"   Render Engine: {props.render_engine}")
        print("✅ Properties are working correctly")
    except Exception as e:
        print(f"❌ Property access failed: {e}")
        return False
    
    # Check operators
    operators = ['connect_wallet', 'submit_job', 'check_job_status', 'download_result', 'refresh_jobs']
    working_operators = 0
    
    for op in operators:
        if hasattr(bpy.ops, 'veriframe') and hasattr(bpy.ops.veriframe, op):
            working_operators += 1
    
    print(f"\n🎛️  Operators available: {working_operators}/{len(operators)}")
    
    if working_operators == len(operators):
        print("✅ All VeriFrame operators are working")
    else:
        print("⚠️  Some operators may not be available")
    
    return True

def show_render_properties():
    """Try to automatically show the render properties"""
    
    # Try to set the properties context to render
    try:
        # Find a properties area
        for area in bpy.context.screen.areas:
            if area.type == 'PROPERTIES':
                for space in area.spaces:
                    if space.type == 'PROPERTIES':
                        space.context = 'RENDER'
                        print("✅ Switched to Render Properties automatically")
                        return True
        
        print("⚠️  Could not find Properties panel to switch to Render Properties")
        return False
        
    except Exception as e:
        print(f"⚠️  Could not switch to Render Properties: {e}")
        return False

def manual_panel_check():
    """Manual check for panel visibility"""
    
    print("\n🔧 MANUAL TROUBLESHOOTING:")
    print("-" * 25)
    
    # Check if we're in the right context
    current_mode = bpy.context.mode
    print(f"Current mode: {current_mode}")
    
    if current_mode != 'OBJECT':
        print("💡 TIP: Switch to Object mode for full UI access")
    
    # Check active object
    if bpy.context.active_object:
        obj_type = bpy.context.active_object.type
        print(f"Active object type: {obj_type}")
    else:
        print("No active object selected")
        print("💡 TIP: Select an object to ensure all panels are visible")
    
    # Check screen layout
    areas = [area.type for area in bpy.context.screen.areas]
    if 'PROPERTIES' in areas:
        print("✅ Properties panel is available in current layout")
    else:
        print("❌ Properties panel not found in current layout")
        print("💡 TIP: Switch to 'Layout' or 'Shading' workspace")

if __name__ == "__main__":
    print("🚀 VeriFrame UI Location Helper")
    print("🔍 Checking VeriFrame installation and UI...")
    
    if check_veriframe_ui():
        print("\n📍 QUICK LOCATION GUIDE:")
        print("   Properties Panel → Render Properties Tab → VeriFrame Section")
        
        # Try to automatically switch to render properties
        show_render_properties()
        
        print("\n🎉 VeriFrame should be visible in the Render Properties!")
        print("\nIf you still can't see it:")
        print("- Make sure Properties panel is visible")
        print("- Click the camera icon (Render Properties)")
        print("- Scroll down to find VeriFrame section")
        print("- Click the arrow to expand it")
        
    else:
        print("\n❌ VeriFrame UI check failed!")
        manual_panel_check()
        print("\nTroubleshooting steps:")
        print("1. Check if addon is enabled in Preferences")
        print("2. Try restarting Blender")
        print("3. Check Console for error messages")
        print("4. Reinstall the addon if needed")