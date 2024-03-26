import os
import requests
from util import utils




def upscale_image(image_dir, output_dir):
    engine_id = "esrgan-v1-x2plus"
    api_host = os.getenv("API_HOST", "https://api.stability.ai")
    api_key = "sk-YXDhn2YY01VtUgE3w9ozmMwkzPRn19imBOj86XQsBXIOu2NO"

    if api_key is None:
        raise Exception("Missing Stability API key.")

    for image in utils.list_files_abs_path(image_dir):
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/image-to-image/upscale",
            headers={
                "Accept": "image/png",
                "Authorization": f"Bearer {api_key}"
            },
            files={
                "image": open(image, "rb")
            },
        )

        if response.status_code != 200:
            print("Non-200 response: " + str(response.text))
            continue
        image_name = image.split('/')[-1]
        os.makedirs(output_dir, exist_ok=True)
        with open(f"{output_dir}/{image_name}", "wb") as f:
            f.write(response.content)