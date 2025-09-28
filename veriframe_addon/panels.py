"""
UI Panels for the VeriFrame addon
"""

import bpy
from bpy.types import Panel

class VF_PT_MainPanel(Panel):
    """Main VeriFrame panel in render properties"""
    bl_label = "VeriFrame"
    bl_idname = "VF_PT_main_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        props = context.scene.veriframe
        
        # Wallet status indicator
        if props.wallet_connected:
            layout.label(text="", icon='LINKED')
        else:
            layout.label(text="", icon='UNLINKED')
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.veriframe
        
        # Wallet Connection Section
        box = layout.box()
        row = box.row()
        row.label(text="Wallet", icon='FUND')
        
        if props.wallet_connected:
            row.label(text=f"Connected: {props.wallet_address[:10]}...")
            row.operator("veriframe.connect_wallet", text="", icon='FILE_REFRESH')
        else:
            row.operator("veriframe.connect_wallet", text="Connect Wallet")
        
        if not props.wallet_connected:
            box.label(text="Connect wallet to submit jobs", icon='INFO')
            return
        
        # Job Submission Section
        box = layout.box()
        box.label(text="Submit New Job", icon='PLUS')
        
        col = box.column(align=True)
        col.prop(props, "reward_amount")
        col.prop(props, "job_deadline")
        
        row = col.row(align=True)
        row.prop(props, "render_engine", expand=True)
        
        col.prop(props, "output_format")
        
        # Submit button
        row = box.row()
        row.scale_y = 1.5
        row.operator("veriframe.submit_job", text="Submit Job", icon='RENDER_ANIMATION')
        
        # Advanced Settings
        box = layout.box()
        row = box.row()
        row.prop(props, "show_advanced_settings", 
                icon="TRIA_DOWN" if props.show_advanced_settings else "TRIA_RIGHT",
                icon_only=True, emboss=False)
        row.label(text="Advanced Settings")
        
        if props.show_advanced_settings:
            col = box.column()
            col.prop(props, "rpc_url")
            col.prop(props, "contract_address")
            col.separator()
            col.prop(props, "ipfs_api_url")
            col.prop(props, "ipfs_gateway_url")

class VF_PT_JobHistoryPanel(Panel):
    """Panel for managing job history"""
    bl_label = "Job History"
    bl_idname = "VF_PT_job_history_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "VF_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        props = context.scene.veriframe
        
        # Auto refresh toggle
        layout.prop(props, "auto_refresh", text="", icon='FILE_REFRESH')
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.veriframe
        
        if not props.wallet_connected:
            layout.label(text="Connect wallet to view jobs", icon='INFO')
            return
        
        # Refresh controls
        row = layout.row()
        row.operator("veriframe.refresh_jobs", text="Refresh All", icon='FILE_REFRESH')
        
        if props.auto_refresh:
            row.prop(props, "refresh_interval", text="Interval (s)")
        
        # Jobs list
        if len(props.jobs) == 0:
            layout.label(text="No jobs submitted yet", icon='INFO')
            return
        
        # Job list
        box = layout.box()
        
        for i, job in enumerate(props.jobs):
            row = box.row()
            
            # Status icon
            status_icons = {
                'PENDING': 'TIME',
                'IN_PROGRESS': 'RENDER_ANIMATION',
                'COMPLETED': 'CHECKMARK',
                'FAILED': 'CANCEL',
                'CANCELLED': 'X'
            }
            row.label(text="", icon=status_icons.get(job.status, 'QUESTION'))
            
            # Job info
            col = row.column()
            col.label(text=f"Job {job.job_id}")
            
            sub_row = col.row()
            sub_row.scale_y = 0.8
            sub_row.label(text=f"Status: {job.status}")
            sub_row.label(text=f"Reward: {job.reward} STRK")
            
            # Action buttons
            col = row.column()
            col.scale_x = 0.8
            
            # Status check button
            op = col.operator("veriframe.check_job_status", text="", icon='FILE_REFRESH')
            op.job_id = job.job_id
            
            # Download button (only for completed jobs)
            if job.status == 'COMPLETED':
                op = col.operator("veriframe.download_result", text="", icon='IMPORT')
                op.job_id = job.job_id
            
            if i < len(props.jobs) - 1:
                box.separator()
        
        # Statistics
        completed_count = sum(1 for job in props.jobs if job.status == 'COMPLETED')
        total_reward = sum(job.reward for job in props.jobs if job.status == 'COMPLETED')
        
        if completed_count > 0:
            stats_box = layout.box()
            stats_box.label(text="Statistics", icon='GRAPH')
            
            row = stats_box.row()
            row.label(text=f"Completed: {completed_count}/{len(props.jobs)}")
            row.label(text=f"Total Spent: {total_reward} STRK")