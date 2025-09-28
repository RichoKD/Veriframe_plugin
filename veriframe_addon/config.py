"""
Configuration and constants for VeriFrame addon
"""

# Version information
ADDON_VERSION = (1, 0, 0)
REQUIRED_BLENDER_VERSION = (4, 0, 0)

# Network endpoints
DEFAULT_SEPOLIA_RPC = "https://api.cartridge.gg/x/starknet/sepolia"
DEFAULT_MAINNET_RPC = "https://api.cartridge.gg/x/starknet/mainnet"

# Contract addresses
SEPOLIA_CONTRACT_ADDRESS = "0x03103f3d37047b8bd0680c22a9b8d9502d5d1e34ab12259659dea2f6354ad7e8"
MAINNET_CONTRACT_ADDRESS = ""  # To be deployed

# IPFS configuration
DEFAULT_IPFS_API_URL = "http://127.0.0.1:5001"
DEFAULT_IPFS_GATEWAY_URL = "http://127.0.0.1:8080"

# Job limits and defaults
DEFAULT_REWARD_AMOUNT = 10.0
MIN_REWARD_AMOUNT = 0.1
MAX_REWARD_AMOUNT = 10000.0

DEFAULT_DEADLINE_HOURS = 24
MIN_DEADLINE_HOURS = 1
MAX_DEADLINE_HOURS = 168  # 1 week

MAX_FILE_SIZE_MB = 500  # Maximum blend file size
MAX_JOB_HISTORY = 100

# Supported render engines
SUPPORTED_ENGINES = [
    ('CYCLES', 'Cycles', 'Use Cycles rendering engine'),
    ('EEVEE', 'Eevee', 'Use Eevee rendering engine'), 
    ('WORKBENCH', 'Workbench', 'Use Workbench rendering engine'),
]

# Supported output formats
SUPPORTED_FORMATS = [
    ('PNG', 'PNG', 'Portable Network Graphics'),
    ('JPEG', 'JPEG', 'JPEG format'),
    ('EXR', 'EXR', 'OpenEXR format'),
    ('TIFF', 'TIFF', 'TIFF format'),
]

# Job status types
JOB_STATUS_TYPES = [
    ('PENDING', 'Pending', 'Job is waiting for a worker'),
    ('IN_PROGRESS', 'In Progress', 'Job is being processed'),
    ('COMPLETED', 'Completed', 'Job has been completed'),
    ('FAILED', 'Failed', 'Job failed to complete'),
    ('CANCELLED', 'Cancelled', 'Job was cancelled'),
]

# UI constants
PANEL_CATEGORY = "VeriFrame"
ICON_CONNECTED = 'LINKED'
ICON_DISCONNECTED = 'UNLINKED'
ICON_JOB_PENDING = 'TIME'
ICON_JOB_PROGRESS = 'RENDER_ANIMATION'
ICON_JOB_COMPLETED = 'CHECKMARK'
ICON_JOB_FAILED = 'CANCEL'

# Error messages
ERROR_WALLET_NOT_CONNECTED = "Please connect your wallet first"
ERROR_INVALID_REWARD = "Reward amount must be greater than 0"
ERROR_IPFS_UPLOAD_FAILED = "Failed to upload to IPFS"
ERROR_CONTRACT_SUBMIT_FAILED = "Failed to submit job to contract"
ERROR_JOB_NOT_FOUND = "Job not found"
ERROR_JOB_NOT_COMPLETED = "Job is not completed yet"
ERROR_DOWNLOAD_FAILED = "Failed to download result"

# Success messages
SUCCESS_JOB_SUBMITTED = "Job submitted successfully!"
SUCCESS_WALLET_CONNECTED = "Wallet connected successfully"
SUCCESS_RESULT_DOWNLOADED = "Result downloaded successfully"
SUCCESS_JOBS_REFRESHED = "Jobs refreshed successfully"

# File paths
DOWNLOADS_FOLDER = "veriframe_downloads"
TEMP_FOLDER = "veriframe_temp"

# Validation limits
MAX_RESOLUTION_WARNING = 4096
MAX_SAMPLES_WARNING = 1000
MAX_OBJECTS_WARNING = 1000

# Auto-refresh settings
DEFAULT_REFRESH_INTERVAL = 30  # seconds
MIN_REFRESH_INTERVAL = 10
MAX_REFRESH_INTERVAL = 300