"""
Operators for the VeriFrame addon
"""

import bpy
import bmesh
import os
import json
import requests
import tempfile
import shutil
from datetime import datetime, timedelta
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty

class VF_OT_ConnectWallet(Operator):
    """Connect to Starknet wallet"""
    bl_idname = "veriframe.connect_wallet"
    bl_label = "Connect Wallet"
    bl_description = "Connect to your Starknet wallet"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        props = context.scene.veriframe
        
        # In a real implementation, this would integrate with wallet extensions
        # For now, we'll simulate wallet connection
        if not props.wallet_address:
            self.report({'ERROR'}, "Please enter a wallet address in preferences")
            return {'CANCELLED'}
        
        props.wallet_connected = True
        self.report({'INFO'}, f"Connected to wallet: {props.wallet_address[:10]}...")
        return {'FINISHED'}

class VF_OT_SubmitJob(Operator):
    """Submit current blend file as a rendering job"""
    bl_idname = "veriframe.submit_job"
    bl_label = "Submit Job"
    bl_description = "Submit the current blend file to VeriFrame network"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        props = context.scene.veriframe
        
        # Validate settings
        if not props.wallet_connected:
            self.report({'ERROR'}, "Please connect your wallet first")
            return {'CANCELLED'}
        
        if props.reward_amount <= 0:
            self.report({'ERROR'}, "Reward amount must be greater than 0")
            return {'CANCELLED'}
        
        # Save current blend file to temporary location
        try:
            temp_dir = tempfile.mkdtemp()
            temp_blend_path = os.path.join(temp_dir, "job.blend")
            
            # Save the current blend file
            bpy.ops.wm.save_as_mainfile(filepath=temp_blend_path, copy=True)
            
            # Upload to IPFS
            ipfs_hash = self._upload_to_ipfs(temp_blend_path, props)
            if not ipfs_hash:
                self.report({'ERROR'}, "Failed to upload to IPFS")
                return {'CANCELLED'}
            
            # Submit job to contract
            job_id = self._submit_to_contract(ipfs_hash, props)
            if not job_id:
                self.report({'ERROR'}, "Failed to submit job to contract")
                return {'CANCELLED'}
            
            # Add job to tracking list
            job = props.jobs.add()
            job.job_id = job_id
            job.status = 'PENDING'
            job.reward = props.reward_amount
            job.deadline = props.job_deadline
            job.ipfs_hash = ipfs_hash
            job.submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Clean up temp file
            shutil.rmtree(temp_dir)
            
            self.report({'INFO'}, f"Job submitted successfully! ID: {job_id}")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Error submitting job: {str(e)}")
            return {'CANCELLED'}
    
    def _upload_to_ipfs(self, file_path, props):
        """Upload file to IPFS and return hash"""
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(
                    f"{props.ipfs_api_url}/api/v0/add",
                    files=files,
                    timeout=30
                )
                
            if response.status_code == 200:
                result = response.json()
                return result['Hash']
            else:
                print(f"IPFS upload failed: {response.text}")
                return None
                
        except Exception as e:
            print(f"IPFS upload error: {e}")
            return None
    
    def _submit_to_contract(self, ipfs_hash, props):
        """Submit job to smart contract"""
        # In a real implementation, this would interact with Starknet
        # For now, we'll simulate by generating a job ID
        import uuid
        job_id = str(uuid.uuid4())[:8]
        
        # Here you would typically:
        # 1. Connect to Starknet using starknet.py
        # 2. Call the job registry contract's submit_job function
        # 3. Pass ipfs_hash, reward_amount, and deadline
        # 4. Return the transaction hash or job ID
        
        return job_id

class VF_OT_CheckJobStatus(Operator):
    """Check status of a specific job"""
    bl_idname = "veriframe.check_job_status"
    bl_label = "Check Status"
    bl_description = "Check the status of the selected job"
    bl_options = {'REGISTER'}
    
    job_id: StringProperty(
        name="Job ID",
        description="ID of the job to check",
        default=""
    )
    
    def execute(self, context):
        props = context.scene.veriframe
        
        if not self.job_id and props.active_job_index < len(props.jobs):
            job = props.jobs[props.active_job_index]
            self.job_id = job.job_id
        
        if not self.job_id:
            self.report({'ERROR'}, "No job selected")
            return {'CANCELLED'}
        
        # Query contract for job status
        status = self._get_job_status(self.job_id, props)
        
        # Update job status in list
        for job in props.jobs:
            if job.job_id == self.job_id:
                job.status = status
                break
        
        self.report({'INFO'}, f"Job {self.job_id}: {status}")
        return {'FINISHED'}
    
    def _get_job_status(self, job_id, props):
        """Get job status from contract"""
        # In a real implementation, this would query the smart contract
        # For now, we'll simulate status progression
        import random
        statuses = ['PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED']
        return random.choice(statuses)

class VF_OT_DownloadResult(Operator):
    """Download completed render result"""
    bl_idname = "veriframe.download_result"
    bl_label = "Download Result"
    bl_description = "Download the rendered result from IPFS"
    bl_options = {'REGISTER'}
    
    job_id: StringProperty(
        name="Job ID",
        description="ID of the job to download",
        default=""
    )
    
    def execute(self, context):
        props = context.scene.veriframe
        
        if not self.job_id and props.active_job_index < len(props.jobs):
            job = props.jobs[props.active_job_index]
            self.job_id = job.job_id
        
        job = None
        for j in props.jobs:
            if j.job_id == self.job_id:
                job = j
                break
        
        if not job:
            self.report({'ERROR'}, "Job not found")
            return {'CANCELLED'}
        
        if job.status != 'COMPLETED':
            self.report({'ERROR'}, "Job is not completed yet")
            return {'CANCELLED'}
        
        if not job.result_hash:
            # Try to get result hash from contract
            result_hash = self._get_result_hash(job.job_id, props)
            if result_hash:
                job.result_hash = result_hash
            else:
                self.report({'ERROR'}, "No result available")
                return {'CANCELLED'}
        
        # Download from IPFS
        success = self._download_from_ipfs(job.result_hash, props)
        if success:
            self.report({'INFO'}, "Result downloaded successfully")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Failed to download result")
            return {'CANCELLED'}
    
    def _get_result_hash(self, job_id, props):
        """Get result hash from contract"""
        # In a real implementation, this would query the smart contract
        # For completed jobs to get the IPFS hash of the result
        return "QmExampleResultHash123456789"
    
    def _download_from_ipfs(self, ipfs_hash, props):
        """Download file from IPFS"""
        try:
            # Create downloads directory if it doesn't exist
            downloads_dir = os.path.join(bpy.path.abspath("//"), "veriframe_downloads")
            os.makedirs(downloads_dir, exist_ok=True)
            
            # Download the file
            url = f"{props.ipfs_gateway_url}/ipfs/{ipfs_hash}"
            response = requests.get(url, timeout=60)
            
            if response.status_code == 200:
                file_path = os.path.join(downloads_dir, f"{ipfs_hash}.zip")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Download error: {e}")
            return False

class VF_OT_RefreshJobs(Operator):
    """Refresh status of all jobs"""
    bl_idname = "veriframe.refresh_jobs"
    bl_label = "Refresh Jobs"
    bl_description = "Refresh the status of all jobs"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        props = context.scene.veriframe
        
        updated_count = 0
        for job in props.jobs:
            old_status = job.status
            new_status = self._get_job_status(job.job_id, props)
            if old_status != new_status:
                job.status = new_status
                updated_count += 1
        
        self.report({'INFO'}, f"Refreshed {updated_count} job(s)")
        return {'FINISHED'}
    
    def _get_job_status(self, job_id, props):
        """Get job status from contract"""
        # Simulate status progression
        import random
        statuses = ['PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED']
        return random.choice(statuses)