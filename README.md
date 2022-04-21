gcloud builds submit --tag gcr.io/esghub/esghub --project=esghub

gcloud run deploy --image gcr.io/esghub/esghub --platform managed --project=esghub
--allow-unauthorized