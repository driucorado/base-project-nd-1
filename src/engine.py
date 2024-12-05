from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = os.environ['DB_URL']

logger.info(DATABASE_URL)
engine = create_engine(os.environ['DB_URL'])
# Define Table Classes
Base = declarative_base()