# parsons-prefect-gcp-deployment

This repo is an example of how to use a Prefect automatic deployment and provisioning of workflow on GCP. 

Here are all the relevant Prefect Docs. 

https://docs.prefect.io/latest/guides/deployment/push-work-pools/


Some prereqs are that you need to have a GCP account with a billing account and you need Docker installed and running. 

Getting Started:


1. **Clone the repository:**

   ```bash
   git clone https://github.com/matthewkrausse/parsons-prefect-gcp-deployment

2. **Create a Virtual Environment:**

   ```bash
   python3.10 -m venv venv

3. **Activate the venv:**

   ```bash
   source venv/bin/activate

4. **Install the reqs:**

   ```bash
   pip install -r requirements.txt

5. **Install the gcloud cli client:**

   Install the gcloud CLI (https://cloud.google.com/sdk/docs/install) and authenticate with your GCP project (https://cloud.google.com/docs/authentication/gcloud).

   Also pull any updates
   ```bash
   gcloud components update

6. **Download Docker:**
   
    https://docs.docker.com/get-docker/

7. **Create the work pool:**
   Using the --provision-infra flag will allow you to select a GCP project to use for your work pool and automatically configure it to be ready to execute flows via Cloud Run. In your GCP project, this command will activate the Cloud Run API, create a service account, and create a key for the service account, if they don't already exist. In your Prefect workspace, this command will create a GCPCredentials block for storing the service account key.

   ```bash
   prefect work-pool create --type cloud-run:push --provision-infra my-cloud-run-pool

8. **Run the built in prefect flow deployment or create your own and run it**

  ```bash
  python test_deployment.py
