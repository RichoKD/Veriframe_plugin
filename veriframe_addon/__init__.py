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
    properties.VeriFrameProperties,
    operators.VF_OT_SubmitJob,
    operators.VF_OT_CheckJobStatus,
    operators.VF_OT_DownloadResult,
    operators.VF_OT_ConnectWallet,
    operators.VF_OT_RefreshJobs,
    panels.VF_PT_MainPanel,
    panels.VF_PT_JobHistoryPanel,
)

def register():
    """Register all classes and properties"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Add properties to scene
    bpy.types.Scene.veriframe = bpy.props.PointerProperty(type=properties.VeriFrameProperties)

def unregister():
    """Unregister all classes and properties"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    # Remove properties from scene
    del bpy.types.Scene.veriframe

if __name__ == "__main__":
    register()