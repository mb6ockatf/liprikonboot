# Roles
import os

# List of administration roles ids
admins_role_id = os.environ['discord_admins']
moder_role_id = [os.environ['discord_admins'], os.environ['discord_owner']]
