# Config file

import os

# Bot's configs
ds_app_token = os.environ['ds_app_token']  # App's token

# List of administration roles id's
ds_server_admins = int(os.environ['ds_server_admins'])  # Moderator's role
ds_server_host = os.environ['ds_server_host']  # Server host's  role

ds_prefix = os.environ['ds_prefix']  # Bot's prefix
