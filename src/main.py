import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from engine import engine, Base

if __name__ == '__main__':
   logger.info("Run App")