"""Setup the myGTD application"""
import logging

import pylons.test

from authkit.users.sqlalchemy_driver import UsersFromDatabase
from mygtd.config.environment import load_environment
from mygtd import model


log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup mygtd here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

     # Load the models
    from mygtd.model import meta
    meta.metadata.bind = meta.engine

    log.info("Adding the AuthKit model...")
    users = UsersFromDatabase(model)
    

    # Create the tables if they don't already exist
    meta.metadata.create_all(checkfirst=True)