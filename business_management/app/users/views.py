from . import ubp


@ubp.route("/admin")
def users_index():
    return "这是users中的首页"