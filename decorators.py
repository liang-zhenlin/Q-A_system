from functools import wraps
from flask import g, redirect, url_for 

def login_required(func):
    # 保留 func 的信息
    @wraps(func)
    def inner(*args, **kargs):
        if g.user:
            return func(*args, **kargs)
        else:
            return redirect(url_for("auth.login"))
    return inner