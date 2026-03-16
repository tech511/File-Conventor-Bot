admins = set()
banned_users = set()

start_image = None
prefix = "/"

def add_admin(uid):
    admins.add(uid)

def is_admin(uid):
    return uid in admins

def ban(uid):
    banned_users.add(uid)

def unban(uid):
    banned_users.discard(uid)

def is_banned(uid):
    return uid in banned_users

def set_start_image(file_id):
    global start_image
    start_image = file_id
