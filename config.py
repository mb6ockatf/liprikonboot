# Config file

import os

# Bot's configs
ds_app_token = os.environ['ds_app_token']  # App's token
myserver = int(os.environ['myserver'])  # Server's id

# List of administration roles id's
ds_server_admins = int(os.environ['ds_server_admins'])  # Moderator's role
ds_server_host = os.environ['ds_server_host']  # Server host's  role

ds_prefix = os.environ['ds_prefix']  # Bot's prefix
rules = "1.Do not spam\n\
2.Do not rebel\n\
3.Do not offend admins & other members\n\
4.Be polite\n\
5.Do not change the server's name with no permission of the \
Head Admin\n\
6.Do not ban other members with no permission of the Head \
Admin\n\
7.Revolutions are forbidden\n\
 \
© @liprikon2020#5527"
