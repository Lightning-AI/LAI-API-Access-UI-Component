import os
import json
from typing import Any, Dict
from lightning.app.frontend import StaticWebFrontend


class APIAccessFrontend(StaticWebFrontend):
    """The APIAccessFrontend enables you to give users a guide for interacting with your app via an API.
        
    Example:

        In your LightningFlow, override the method `configure_layout`:

        .. code-block:: python

            def configure_layout(self):
                return APIAccessFrontend(apis=[{
                    "url": "endpoint_url",
                    "method": "POST|PUT|GET",
                    "request": "Example request JSON",
                    "response": "Example response JSON",
                }])
    """

    def __init__(self, apis: Dict[str, Any]) -> None:
        ui_dir = os.path.join(os.path.dirname(__file__), "ui", "build")

        super().__init__(ui_dir)

        # Write API metadata to a JSON file
        # Note: This will deliberately be performed each time the `APIAccessFrontend` so that the metadata can change dynamically without issues
        metadata_file = os.path.join(ui_dir, "api_metadata.json")
        with open(metadata_file, 'w') as f:
            json.dump({"apis": apis}, f)