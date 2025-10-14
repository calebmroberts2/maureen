# NOTE: Do not modify this file. This file is managed by the deployment and integration system.

import logging
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

from agency import create_agency
from agency_swarm.integrations.fastapi import run_fastapi


if __name__ == "__main__":
    run_fastapi(
        agencies={
            # you must export your create agency function here
            "my-agency": create_agency,
        },
        port=8080,
        enable_logging=True
    )