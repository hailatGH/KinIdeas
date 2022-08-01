#!/bin/bash

gcloud config set account hailemichael.atrsaw@kinideas.com
gcloud config set project kin-project-352614

PROJECT_ID=$(gcloud config get-value core/project)
REGION=europe-west1

gcloud builds submit --region=${REGION} --pack image=gcr.io/${PROJECT_ID}/podcast_service_image

gcloud builds submit --region=${REGION} --config migrate.yaml --substitutions _REGION=$REGION

gcloud run services update podcast-service \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/podcast_service_image