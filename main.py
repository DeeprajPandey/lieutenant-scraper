import pprint
import os

import yaml

from logger import get_logger
from scraper.content import scrape_content

logger = get_logger(__name__)

def load_config():
    with open("config.yaml", "r") as conf_file:
        return yaml.safe_load(conf_file)

def main():
    config = load_config()
    logger.info("Starting scraper")
    logger.debug("Testing debug")
    logger.debug(f"config: {pprint.pformat(config['scraper']['content'])}")
    
    scrape_content()

if __name__ == "__main__":
    main()
