from vdmap import create_app, db
from vdmap.db.models import users, routes

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Users": users.Users, "Routes": routes.Routes}

