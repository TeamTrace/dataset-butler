# get.py
import os
import logging
import requests
import redivis

logger = logging.getLogger(__name__)

REDIVIS_API_TOKEN = os.environ["REDIVIS_API_TOKEN"]
WORDPRESS_API_KEY = os.environ["WORDPRESS_API_KEY"]

if not REDIVIS_API_TOKEN:
    raise RuntimeError("Missing REDIVIS_API_TOKEN environment variable.")

def get():
    
    logger.info('Getting notebooks from Redivis...')
    username = "glevines"  # Replace with your Redivis username
    workflow_name = "murder-suicides-family-annihilations-gl:j5pt"  # Replace with your workflow name
    notebook_name = "murder-suicides-family-annihilations:15s0"  # Replace with your notebook name
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    logger.info(f'Running {notebook_name} notebook finished.')
    
    # OPTIONAL - Republish the WordPress page
    # try:
    #     site_url = (
    #             f"https://datahub.thetrace.org/wp-json/dataset/v1/dataset/",
    #             f"{wp_post}/reload?key={WORDPRESS_API_KEY}"
    #     )
    #     response = requests.post(site_url, data=None, headers={'User-Agent': ''})
    #     response.raise_for_status()
    #     logger.info(response.text)
    #     logger.info("Update complete.")

    # except requests.exceptions.HTTPError as err:
    #     logger.info(f"HTTP error occurred: {err}")
    #     logger.info(f"Server response: {response.text}")

    # except Exception as err:
    #     logger.info(f"An error occurred: {err}")
