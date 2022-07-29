#!/bin/bash

gcloud config set account hailemichael.atrsaw@kinideas.com
gcloud config set project kin-project-352614

gcloud iam service-accounts delete podcast-service-account@kin-project-352614.iam.gserviceaccount.com
gcloud sql databases delete podcast-database --instance kin-project-postgresql-v2
gcloud sql users delete podcast_database_admin --instance kin-project-postgresql-v2
gcloud secrets delete podcast_service_settings
gcloud secrets delete podcast_admin_password
gcloud run services delete podcast-service
