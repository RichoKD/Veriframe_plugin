"""
Addon preferences for VeriFrame
"""

import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty, BoolProperty, IntProperty

class VeriFramePreferences(AddonPreferences):
    """VeriFrame addon preferences"""
    bl_idname = __name__.partition('.')[0]  # Get the addon module name
    
    # Default wallet settings
    default_wallet_address: StringProperty(
        name="Default Wallet Address",
        description="Default Starknet wallet address to use",
        default="",
        maxlen=66  # Starknet addresses are 66 characters
    )
    
    # Network settings
    default_rpc_url: StringProperty(
        name="Default RPC URL",
        description="Default Starknet RPC endpoint",
        default="https://api.cartridge.gg/x/starknet/sepolia"
    )
    
    default_contract_address: StringProperty(
        name="Default Contract Address",
        description="Default VeriFrame job registry contract address",
        default="0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8"
    )
    
    # IPFS settings
    default_ipfs_api_url: StringProperty(
        name="Default IPFS API URL",
        description="Default IPFS API endpoint",
        default="http://127.0.0.1:5001"
    )
    
    default_ipfs_gateway_url: StringProperty(
        name="Default IPFS Gateway URL",
        description="Default IPFS gateway for downloading files",
        default="http://127.0.0.1:8080"
    )
    
    # UI settings
    show_debug_info: BoolProperty(
        name="Show Debug Information",
        description="Show debug information in the UI",
        default=False
    )
    
    auto_save_jobs: BoolProperty(
        name="Auto Save Job History",
        description="Automatically save job history to blend file",
        default=True
    )
    
    max_job_history: IntProperty(
        name="Max Job History",
        description="Maximum number of jobs to keep in history",
        default=50,
        min=10,
        max=500
    )
    
    def draw(self, context):
        layout = self.layout
        
        # Wallet Settings
        box = layout.box()
        box.label(text="Wallet Settings", icon='FUND')
        col = box.column()
        col.prop(self, "default_wallet_address")
        
        # Network Settings
        box = layout.box()
        box.label(text="Network Settings", icon='WORLD')
        col = box.column()
        col.prop(self, "default_rpc_url")
        col.prop(self, "default_contract_address")
        
        # IPFS Settings
        box = layout.box()
        box.label(text="IPFS Settings", icon='PACKAGE')
        col = box.column()
        col.prop(self, "default_ipfs_api_url")
        col.prop(self, "default_ipfs_gateway_url")
        
        # UI Settings
        box = layout.box()
        box.label(text="UI Settings", icon='PREFERENCES')
        col = box.column()
        col.prop(self, "show_debug_info")
        col.prop(self, "auto_save_jobs")
        col.prop(self, "max_job_history")
        
        # Instructions
        box = layout.box()
        box.label(text="Instructions", icon='INFO')
        col = box.column()
        col.label(text="1. Set your Starknet wallet address above")
        col.label(text="2. Ensure IPFS node is running (default: localhost:5001)")
        col.label(text="3. Configure network settings if using custom endpoints")
        col.label(text="4. Use the VeriFrame panel in Render Properties")
        
        # Links
        row = layout.row()
        row.operator("wm.url_open", text="Documentation", icon='URL').url = "https://github.com/RichoKD/VeriFrame"
        row.operator("wm.url_open", text="Report Issue", icon='URL').url = "https://github.com/RichoKD/VeriFrame/issues"