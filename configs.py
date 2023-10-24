import yaml
from enum import Enum


DEFAULT_CONFIG_FILE = 'default.yaml'
CONFIG_FILE = 'river_sand_sam.yaml'

# Open config file
def load_config(file):
    with open(file, 'rb')as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
    return cfg

# Save config file
def save_config(cfg, file):
    s = yaml.dump(cfg)
    with open(file, 'w') as f:
        f.write(s)
    return True

# Use numbers control different modes
class STATUSMode(Enum):
    VIEW = 0 # 0 denotes the view mode to see annotations
    CREATE = 1 # 1 denotes the create mode to set up annotations
    EDIT = 2 # 2 denotes modification of annotations

# Use numbers control methods of traditional annotations or with SAM
class DRAWMode(Enum):
    POLYGON = 0 # 0 denotes the traditional annotating methods
    SEGMENTANYTHING = 1 # 1 denotes annotating with SAM

# Define the signals of the click by the mouse
class CLICKMode(Enum):
    POSITIVE = 0
    NEGATIVE = 1

# Use numbers divide different instances
class MAPMode(Enum):
    LABEL = 0
    SEMANTIC = 1
    INSTANCE = 2

# Use numbers divide types to save annotations
class CONTOURMode(Enum):
    SAVE_MAX_ONLY = 0 # Save the max area
    SAVE_EXTERNAL = 1 # Save the external contour only
    SAVE_ALL = 2 # Save all