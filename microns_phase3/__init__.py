import os

from .version import __version__

import datajoint as dj

dj.config['enable_python_native_blobs'] = True
dj.errors._switch_filepath_types(True)
dj.errors._switch_adapted_types(True)

# try:
#     import coregister.solve as cs
# except ModuleNotFoundError:
#     raise ModuleNotFoundError('Coregistration package missing. Run "pip3 install git+https://github.com/AllenInstitute/em_coregistration.git@phase3"')


for key in ("custom", "stores"):
    if key not in dj.config:
        dj.config[key] = {}

# overwrite dj.config['custom'] values with environment variables if available

dj.config["custom"]["database.prefix"] = os.getenv(
    "DATABASE_PREFIX", dj.config["custom"].get("database.prefix", "")
)

DB_PREFIX: str = dj.config["custom"].get("database.prefix", "")
