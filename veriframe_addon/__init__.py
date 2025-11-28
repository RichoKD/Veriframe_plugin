"""
VeriFrame Blender Plugin
A Blender addon for submitting rendering jobs to the VeriFrame decentralized network.
"""

bl_info = {
    "name": "VeriFrame",
    "author": "VeriFrame Team",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Properties > Render Properties > VeriFrame",
    "description": "Submit Blender rendering jobs to the VeriFrame decentralized network",
    "category": "Render",
    "support": "COMMUNITY",
    "doc_url": "https://github.com/RichoKD/VeriFrame",
    "tracker_url": "https://github.com/RichoKD/VeriFrame/issues",
}

import bpy
from . import properties
from . import operators
from . import panels
from . import preferences

classes = (
    preferences.VeriFramePreferences,
    properties.VeriFrameJobItem,  # Must be registered before VeriFrameProperties
    properties.VeriFrameProperties,
    operators.VF_OT_SubmitJob,
    operators.VF_OT_CheckJobStatus,
    operators.VF_OT_DownloadResult,
    operators.VF_OT_ConnectWallet,
    operators.VF_OT_QuickConnect,
    operators.VF_OT_DisconnectWallet,
    operators.VF_OT_RefreshJobs,
    panels.VF_PT_MainPanel,
    panels.VF_PT_JobHistoryPanel,
)

def register():
    """Register all classes and properties"""
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
            print(f"✅ Registered: {cls.__name__}")
        except ValueError as e:
            if "already registered" in str(e):
                print(f"⚠️  Already registered: {cls.__name__}")
            else:
                print(f"❌ Failed to register {cls.__name__}: {e}")
                raise
    
    # Add properties to scene
    bpy.types.Scene.veriframe = bpy.props.PointerProperty(type=properties.VeriFrameProperties)

def unregister():
    """Unregister all classes and properties"""
    # Remove properties from scene first
    if hasattr(bpy.types.Scene, 'veriframe'):
        del bpy.types.Scene.veriframe
    
    # Unregister classes in reverse order
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
            print(f"✅ Unregistered: {cls.__name__}")
        except Exception as e:
            print(f"⚠️  Could not unregister {cls.__name__}: {e}")

if __name__ == "__main__":
    register()