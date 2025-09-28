"""
Utility functions for VeriFrame addon
"""

import os
import json
import requests
import tempfile
import hashlib
from typing import Optional, Dict, Any

class IPFSManager:
    """Handles IPFS operations"""
    
    def __init__(self, api_url: str, gateway_url: str):
        self.api_url = api_url.rstrip('/')
        self.gateway_url = gateway_url.rstrip('/')
    
    def upload_file(self, file_path: str) -> Optional[str]:
        """Upload a file to IPFS and return the hash"""
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(
                    f"{self.api_url}/api/v0/add",
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
    
    def download_file(self, ipfs_hash: str, output_path: str) -> bool:
        """Download a file from IPFS"""
        try:
            url = f"{self.gateway_url}/ipfs/{ipfs_hash}"
            response = requests.get(url, timeout=60)
            
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                print(f"IPFS download failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"IPFS download error: {e}")
            return False
    
    def get_file_info(self, ipfs_hash: str) -> Optional[Dict[str, Any]]:
        """Get information about a file on IPFS"""
        try:
            response = requests.post(
                f"{self.api_url}/api/v0/object/stat",
                params={'arg': ipfs_hash},
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
                
        except Exception as e:
            print(f"IPFS info error: {e}")
            return None

class StarknetManager:
    """Handles Starknet contract interactions"""
    
    def __init__(self, rpc_url: str, contract_address: str):
        self.rpc_url = rpc_url
        self.contract_address = contract_address
    
    def submit_job(self, ipfs_hash: str, reward_amount: float, deadline_hours: int, wallet_address: str) -> Optional[str]:
        """Submit a job to the VeriFrame contract"""
        # In a real implementation, this would:
        # 1. Use starknet.py to connect to the network
        # 2. Create a contract instance
        # 3. Call the submit_job function with proper parameters
        # 4. Handle transaction signing and submission
        # 5. Return the transaction hash or job ID
        
        # For now, we'll simulate this
        import uuid
        job_id = str(uuid.uuid4())[:8]
        print(f"Simulated job submission: {job_id}")
        return job_id
    
    def get_job_status(self, job_id: str) -> str:
        """Get the status of a job from the contract"""
        # In a real implementation, this would query the contract
        # For simulation, we'll return random status
        import random
        statuses = ['PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED']
        return random.choice(statuses)
    
    def get_job_result(self, job_id: str) -> Optional[str]:
        """Get the result IPFS hash for a completed job"""
        # In a real implementation, this would query the contract
        # For simulation, return a mock hash
        return "QmExampleResultHash123456789"
    
    def cancel_job(self, job_id: str, wallet_address: str) -> bool:
        """Cancel a pending job"""
        # In a real implementation, this would call the contract
        print(f"Simulated job cancellation: {job_id}")
        return True

class BlenderJobManager:
    """Manages Blender-specific job operations"""
    
    @staticmethod
    def prepare_blend_file(output_path: str, render_settings: Dict[str, Any]) -> bool:
        """Prepare the current blend file for remote rendering"""
        try:
            import bpy
            
            # Save current render settings
            original_engine = bpy.context.scene.render.engine
            original_format = bpy.context.scene.render.image_settings.file_format
            
            # Apply job-specific settings
            if 'engine' in render_settings:
                bpy.context.scene.render.engine = render_settings['engine']
            
            if 'format' in render_settings:
                bpy.context.scene.render.image_settings.file_format = render_settings['format']
            
            # Pack external data
            bpy.ops.file.pack_all()
            
            # Save the prepared file
            bpy.ops.wm.save_as_mainfile(filepath=output_path, copy=True)
            
            # Restore original settings
            bpy.context.scene.render.engine = original_engine
            bpy.context.scene.render.image_settings.file_format = original_format
            
            return True
            
        except Exception as e:
            print(f"Error preparing blend file: {e}")
            return False
    
    @staticmethod
    def validate_scene() -> Dict[str, Any]:
        """Validate the current scene for remote rendering"""
        try:
            import bpy
            
            issues = []
            warnings = []
            
            # Check for external files
            external_files = []
            for img in bpy.data.images:
                if img.filepath and not img.packed_file:
                    external_files.append(img.filepath)
            
            if external_files:
                warnings.append(f"Found {len(external_files)} external images. They will be packed automatically.")
            
            # Check render settings
            scene = bpy.context.scene
            if scene.render.resolution_x > 4096 or scene.render.resolution_y > 4096:
                warnings.append("High resolution detected. This may increase rendering time and cost.")
            
            if scene.render.engine == 'CYCLES' and scene.cycles.samples > 1000:
                warnings.append("High sample count detected. This may increase rendering time significantly.")
            
            # Check for missing materials
            missing_materials = []
            for obj in bpy.data.objects:
                if obj.type == 'MESH' and len(obj.data.materials) == 0:
                    missing_materials.append(obj.name)
            
            if missing_materials:
                warnings.append(f"Objects without materials: {', '.join(missing_materials[:5])}")
            
            return {
                'valid': len(issues) == 0,
                'issues': issues,
                'warnings': warnings
            }
            
        except Exception as e:
            return {
                'valid': False,
                'issues': [f"Validation error: {str(e)}"],
                'warnings': []
            }

class JobTracker:
    """Tracks and manages job history"""
    
    def __init__(self):
        self.jobs = []
    
    def add_job(self, job_data: Dict[str, Any]) -> str:
        """Add a new job to tracking"""
        job_id = job_data.get('job_id', '')
        self.jobs.append(job_data)
        return job_id
    
    def update_job_status(self, job_id: str, status: str) -> bool:
        """Update the status of a tracked job"""
        for job in self.jobs:
            if job.get('job_id') == job_id:
                job['status'] = status
                return True
        return False
    
    def get_job(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get job data by ID"""
        for job in self.jobs:
            if job.get('job_id') == job_id:
                return job
        return None
    
    def get_active_jobs(self) -> list:
        """Get all active (pending/in progress) jobs"""
        return [job for job in self.jobs if job.get('status') in ['PENDING', 'IN_PROGRESS']]
    
    def cleanup_old_jobs(self, max_jobs: int = 50):
        """Remove old jobs to keep history manageable"""
        if len(self.jobs) > max_jobs:
            # Keep most recent jobs
            self.jobs = self.jobs[-max_jobs:]

def calculate_file_hash(file_path: str) -> str:
    """Calculate SHA256 hash of a file"""
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    size = float(size_bytes)
    
    while size >= 1024.0 and i < len(size_names) - 1:
        size /= 1024.0
        i += 1
    
    return f"{size:.1f}{size_names[i]}"

def estimate_render_time(scene_data: Dict[str, Any]) -> int:
    """Estimate render time in minutes based on scene complexity"""
    # Simple heuristic for render time estimation
    base_time = 1  # 1 minute base
    
    resolution_factor = (scene_data.get('width', 1920) * scene_data.get('height', 1080)) / (1920 * 1080)
    sample_factor = scene_data.get('samples', 128) / 128
    
    estimated_time = base_time * resolution_factor * sample_factor
    
    # Add complexity factors
    if scene_data.get('has_subsurface', False):
        estimated_time *= 1.5
    
    if scene_data.get('has_volumetrics', False):
        estimated_time *= 2.0
    
    if scene_data.get('object_count', 0) > 100:
        estimated_time *= 1.2
    
    return max(1, int(estimated_time))