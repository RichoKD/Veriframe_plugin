"""
Properties for the VeriFrame addon
"""

import bpy
from bpy.props import (
    StringProperty,
    FloatProperty,
    IntProperty,
    BoolProperty,
    EnumProperty,
    CollectionProperty
)

class VeriFrameJobItem(bpy.types.PropertyGroup):
    """Individual job item for tracking"""
    job_id: StringProperty(
        name="Job ID",
        description="Unique identifier for the job",
        default=""
    )
    
    status: EnumProperty(
        name="Status",
        description="Current job status",
        items=[
            ('PENDING', 'Pending', 'Job is waiting for a worker'),
            ('IN_PROGRESS', 'In Progress', 'Job is being processed'),
            ('COMPLETED', 'Completed', 'Job has been completed'),
            ('FAILED', 'Failed', 'Job failed to complete'),
            ('CANCELLED', 'Cancelled', 'Job was cancelled'),
        ],
        default='PENDING'
    )
    
    reward: FloatProperty(
        name="Reward",
        description="Reward amount in STRK tokens",
        default=0.0,
        min=0.0
    )
    
    deadline: IntProperty(
        name="Deadline",
        description="Job deadline (hours from submission)",
        default=24,
        min=1
    )
    
    ipfs_hash: StringProperty(
        name="IPFS Hash",
        description="IPFS hash of the uploaded blend file",
        default=""
    )
    
    result_hash: StringProperty(
        name="Result Hash",
        description="IPFS hash of the rendered result",
        default=""
    )
    
    submission_time: StringProperty(
        name="Submission Time",
        description="When the job was submitted",
        default=""
    )

class VeriFrameProperties(bpy.types.PropertyGroup):
    """Main properties for VeriFrame addon"""
    
    # Wallet and Network Settings
    wallet_address: StringProperty(
        name="Wallet Address",
        description="Your Starknet wallet address",
        default=""
    )
    
    wallet_connected: BoolProperty(
        name="Wallet Connected",
        description="Whether wallet is connected",
        default=False
    )
    
    rpc_url: StringProperty(
        name="RPC URL",
        description="Starknet RPC endpoint",
        default="https://api.cartridge.gg/x/starknet/sepolia"
    )
    
    contract_address: StringProperty(
        name="Contract Address",
        description="VeriFrame job registry contract address",
        default="0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8"
    )
    
    # IPFS Settings
    ipfs_api_url: StringProperty(
        name="IPFS API URL",
        description="IPFS API endpoint",
        default="http://127.0.0.1:5001"
    )
    
    ipfs_gateway_url: StringProperty(
        name="IPFS Gateway URL",
        description="IPFS gateway for downloading files",
        default="http://127.0.0.1:8080"
    )
    
    # Job Submission Settings
    reward_amount: FloatProperty(
        name="Reward Amount",
        description="Reward amount in STRK tokens",
        default=10.0,
        min=0.1,
        max=10000.0,
        precision=2
    )
    
    job_deadline: IntProperty(
        name="Deadline (hours)",
        description="Job deadline in hours from submission",
        default=24,
        min=1,
        max=168  # 1 week max
    )
    
    render_engine: EnumProperty(
        name="Render Engine",
        description="Rendering engine to use",
        items=[
            ('CYCLES', 'Cycles', 'Use Cycles rendering engine'),
            ('EEVEE', 'Eevee', 'Use Eevee rendering engine'),
            ('WORKBENCH', 'Workbench', 'Use Workbench rendering engine'),
        ],
        default='CYCLES'
    )
    
    output_format: EnumProperty(
        name="Output Format",
        description="Output image format",
        items=[
            ('PNG', 'PNG', 'Portable Network Graphics'),
            ('JPEG', 'JPEG', 'JPEG format'),
            ('EXR', 'EXR', 'OpenEXR format'),
            ('TIFF', 'TIFF', 'TIFF format'),
        ],
        default='PNG'
    )
    
    # Job Management
    jobs: CollectionProperty(
        type=VeriFrameJobItem,
        name="Jobs",
        description="List of submitted jobs"
    )
    
    active_job_index: IntProperty(
        name="Active Job Index",
        description="Index of the currently selected job",
        default=0
    )
    
    # UI State
    show_advanced_settings: BoolProperty(
        name="Show Advanced Settings",
        description="Show advanced network and IPFS settings",
        default=False
    )
    
    auto_refresh: BoolProperty(
        name="Auto Refresh",
        description="Automatically refresh job status",
        default=True
    )
    
    refresh_interval: IntProperty(
        name="Refresh Interval",
        description="Auto refresh interval in seconds",
        default=30,
        min=10,
        max=300
    )