from flask.cli import FlaskGroup
from server.app import create_app, db
from server.user.schema import User

# application factory in use
app = create_app()
cli = FlaskGroup(create_app=create_app)

# Registers CLI command for recreating db 
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()