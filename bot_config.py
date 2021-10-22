# Config file

import os

# Server config
ds_client_id = os.environ['ds_client_id']
ds_server_token = os.environ['ds_server_token']

# List of administration roles id's
ds_server_admins = os.environ['ds_server_admins']  # Moderator's role
ds_server_host = os.environ['ds_server_host']  # Server host's  role

ds_bot_name = os.environ['ds_boot_name']
ds_bot_prefix = os.environ['ds_bot_prefix']