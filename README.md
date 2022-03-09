# for-developers-gcp-cloud-function-python
Python Cloud Function Demo for GCP

This function is using Flask and Function Framework for testing.

Prerequisite:
- install Function framework
```
pip install functions-framework
```

To start cloud function locally:
```
functions-framework --target hello_world --debug
```
To execute the function open http://localhost:8080/ in your browser and see Hello world!
If you want to provide a parameter then use http://localhost:8080/?message=HelloYou

For all the details see https://cloud.google.com/functions/docs/running/function-frameworks

##Deploy Cloud Function to GCP via gcloud
```
gcloud auth login
gcloud config set project PROJECT_ID
gcloud functions deploy hello_world --region europe-west3 --allow-unauthenticated --memory 128MB --runtime python39 --timeout 90 --min-instances 0 --max-instances 1 --trigger-http --service-account hello-world-function-sa@for-developers-343319.iam.gserviceaccount.com 
```
