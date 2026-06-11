
from huggingface_hub import HfApi
import os

api = HfApi(
    token=os.getenv("HF_TOKEN")
)

api.upload_folder(

    folder_path=
    "predictive_maintenance_project_12062026/deployment",

    repo_id=
    "NishaGok/engine-predictive-maintenance-app-12062026",

    repo_type="space"

)

print("Deployment uploaded successfully")
