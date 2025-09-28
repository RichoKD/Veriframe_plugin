"""
Example usage and testing script for VeriFrame Blender Plugin

This script demonstrates how to use the VeriFrame plugin programmatically
and can be used for testing plugin functionality.
"""

import bpy
import bmesh

def create_test_scene():
    """Create a simple test scene for rendering"""
    
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    
    # Add a cube
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
    cube = bpy.context.active_object
    cube.name = "TestCube"
    
    # Add a plane as ground
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, -1), scale=(5, 5, 1))
    plane = bpy.context.active_object
    plane.name = "Ground"
    
    # Add a light
    bpy.ops.object.light_add(type='SUN', location=(2, 2, 4))
    light = bpy.context.active_object
    light.name = "SunLight"
    light.data.energy = 3
    
    # Position camera
    bpy.ops.object.camera_add(location=(4, -4, 3))
    camera = bpy.context.active_object
    camera.name = "Camera"
    camera.rotation_euler = (1.1, 0, 0.785)
    
    # Set camera as active
    bpy.context.scene.camera = camera
    
    # Create materials
    create_test_materials()
    
    # Configure render settings
    configure_render_settings()
    
    print("Test scene created successfully!")

def create_test_materials():
    """Create some basic materials for testing"""
    
    # Cube material
    cube_mat = bpy.data.materials.new(name="CubeMaterial")
    cube_mat.use_nodes = True
    bsdf = cube_mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = (0.8, 0.2, 0.1, 1.0)  # Red color
    bsdf.inputs[9].default_value = 0.1  # Roughness
    
    # Assign to cube
    cube = bpy.data.objects["TestCube"]
    cube.data.materials.append(cube_mat)
    
    # Ground material
    ground_mat = bpy.data.materials.new(name="GroundMaterial")
    ground_mat.use_nodes = True
    bsdf = ground_mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = (0.1, 0.1, 0.1, 1.0)  # Dark gray
    bsdf.inputs[9].default_value = 0.8  # Roughness
    
    # Assign to ground
    ground = bpy.data.objects["Ground"]
    ground.data.materials.append(ground_mat)

def configure_render_settings():
    """Configure render settings for testing"""
    scene = bpy.context.scene
    
    # Basic render settings
    scene.render.engine = 'CYCLES'
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 25  # Lower for faster testing
    
    # Cycles settings
    scene.cycles.samples = 64  # Lower for faster testing
    scene.cycles.use_denoising = True
    
    # Output settings
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'

def test_veriframe_plugin():
    """Test VeriFrame plugin functionality"""
    
    # Check if plugin is installed and enabled
    addon_name = "veriframe_addon"
    if addon_name not in bpy.context.preferences.addons:
        print(f"ERROR: {addon_name} is not installed or enabled!")
        return False
    
    print("VeriFrame plugin is installed and enabled ✓")
    
    # Check if VeriFrame properties exist
    if not hasattr(bpy.context.scene, 'veriframe'):
        print("ERROR: VeriFrame properties not found!")
        return False
    
    print("VeriFrame properties found ✓")
    
    # Test property access
    props = bpy.context.scene.veriframe
    print(f"Default reward amount: {props.reward_amount}")
    print(f"Default deadline: {props.job_deadline} hours")
    print(f"Render engine: {props.render_engine}")
    print(f"Output format: {props.output_format}")
    
    # Test scene validation
    try:
        from veriframe_addon.utils import BlenderJobManager
        validation = BlenderJobManager.validate_scene()
        print(f"Scene validation: {'✓' if validation['valid'] else '✗'}")
        if validation['warnings']:
            print("Warnings:", validation['warnings'])
        if validation['issues']:
            print("Issues:", validation['issues'])
    except ImportError:
        print("Could not import VeriFrame utilities")
    
    return True

def demo_job_submission():
    """Demonstrate job submission workflow"""
    
    print("\n=== VeriFrame Job Submission Demo ===")
    
    # Create test scene
    create_test_scene()
    
    # Test plugin
    if not test_veriframe_plugin():
        print("Plugin test failed!")
        return
    
    # Configure VeriFrame settings
    props = bpy.context.scene.veriframe
    props.reward_amount = 5.0  # 5 STRK tokens
    props.job_deadline = 12    # 12 hours
    props.render_engine = 'CYCLES'
    props.output_format = 'PNG'
    
    print(f"\nJob Configuration:")
    print(f"- Reward: {props.reward_amount} STRK")
    print(f"- Deadline: {props.job_deadline} hours")
    print(f"- Engine: {props.render_engine}")
    print(f"- Format: {props.output_format}")
    
    # Check wallet connection
    if not props.wallet_connected:
        print("\nWallet not connected. In a real scenario:")
        print("1. Connect your Starknet wallet")
        print("2. Ensure you have STRK tokens")
        print("3. Click 'Submit Job' in the VeriFrame panel")
    else:
        print(f"\nWallet connected: {props.wallet_address}")
    
    print("\nTo submit this job:")
    print("1. Go to Properties > Render Properties")
    print("2. Find the VeriFrame panel")
    print("3. Connect your wallet if not already connected")
    print("4. Review job settings")
    print("5. Click 'Submit Job'")
    
    print("\nDemo completed!")

if __name__ == "__main__":
    # Run the demo
    demo_job_submission()