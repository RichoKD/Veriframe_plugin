"""
Test script to verify VeriFrame addon registration
Run this in Blender's Text Editor or console to test the addon
"""

import bpy

def test_addon_registration():
    """Test if the VeriFrame addon is properly registered"""
    
    print("Testing VeriFrame addon registration...")
    
    # Check if addon is installed and enabled
    addon_name = "veriframe_addon"
    if addon_name not in bpy.context.preferences.addons:
        print(f"❌ ERROR: {addon_name} is not installed or enabled!")
        return False
    
    print("✅ Addon is installed and enabled")
    
    # Test if VeriFrameJobItem is registered
    try:
        # Try to create an instance of VeriFrameJobItem
        test_item = bpy.types.VeriFrameJobItem()
        print("✅ VeriFrameJobItem is properly registered")
    except AttributeError:
        print("❌ ERROR: VeriFrameJobItem is not registered")
        return False
    
    # Test if VeriFrameProperties is registered
    try:
        # Check if scene has veriframe property
        if hasattr(bpy.context.scene, 'veriframe'):
            props = bpy.context.scene.veriframe
            print("✅ VeriFrameProperties is properly registered")
            
            # Test collection property
            try:
                job = props.jobs.add()
                job.job_id = "test_job_123"
                job.status = 'PENDING'
                job.reward = 5.0
                print("✅ CollectionProperty (jobs) is working correctly")
                
                # Clean up test data
                props.jobs.clear()
                
            except Exception as e:
                print(f"❌ ERROR: CollectionProperty failed: {e}")
                return False
                
        else:
            print("❌ ERROR: VeriFrameProperties not found in scene")
            return False
    except Exception as e:
        print(f"❌ ERROR: VeriFrameProperties registration failed: {e}")
        return False
    
    # Test operators
    operators_to_test = [
        'veriframe.connect_wallet',
        'veriframe.submit_job',
        'veriframe.check_job_status',
        'veriframe.download_result',
        'veriframe.refresh_jobs'
    ]
    
    for op_id in operators_to_test:
        if hasattr(bpy.ops, op_id.split('.')[0]) and hasattr(getattr(bpy.ops, op_id.split('.')[0]), op_id.split('.')[1]):
            print(f"✅ Operator {op_id} is registered")
        else:
            print(f"❌ ERROR: Operator {op_id} is not registered")
            return False
    
    # Test panels
    panel_classes = ['VF_PT_MainPanel', 'VF_PT_JobHistoryPanel']
    for panel_class in panel_classes:
        if hasattr(bpy.types, panel_class):
            print(f"✅ Panel {panel_class} is registered")
        else:
            print(f"❌ ERROR: Panel {panel_class} is not registered")
            return False
    
    print("\n🎉 All registration tests passed!")
    print("The VeriFrame addon is properly registered and ready to use.")
    return True

def test_basic_functionality():
    """Test basic functionality of the addon"""
    
    print("\nTesting basic functionality...")
    
    props = bpy.context.scene.veriframe
    
    # Test property defaults
    print(f"Default reward amount: {props.reward_amount}")
    print(f"Default deadline: {props.job_deadline} hours")
    print(f"Default render engine: {props.render_engine}")
    print(f"Default output format: {props.output_format}")
    
    # Test property setting
    props.reward_amount = 15.0
    props.job_deadline = 48
    props.render_engine = 'EEVEE'
    props.output_format = 'JPEG'
    
    print(f"Updated reward amount: {props.reward_amount}")
    print(f"Updated deadline: {props.job_deadline} hours")
    print(f"Updated render engine: {props.render_engine}")
    print(f"Updated output format: {props.output_format}")
    
    # Reset to defaults
    props.reward_amount = 10.0
    props.job_deadline = 24
    props.render_engine = 'CYCLES'
    props.output_format = 'PNG'
    
    print("✅ Property system is working correctly")

if __name__ == "__main__":
    # Run tests
    if test_addon_registration():
        test_basic_functionality()
    else:
        print("Registration test failed - check addon installation")