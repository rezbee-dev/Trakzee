from flask.cli import FlaskGroup

from server.app import create_app, db
from server.user.schema import UserSchema

# application factory in use
app = create_app()
cli = FlaskGroup(create_app=create_app)


# Registers CLI command for recreating db
@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(UserSchema(username="test_name_1", email="test_name_1@email.com", password="test_name_1_password"))
    db.session.add(UserSchema(username="test_name_2", email="test_name_2@email.org", password="test_name_2_password"))
    db.session.commit()


if __name__ == "__main__":
    cli()
