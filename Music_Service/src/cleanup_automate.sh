#!/bin/bash
gcloud iam service-accounts delete music-service-account
gcloud sql databases delete music-database --instance kin-project-postgresql-v2
gcloud sql users delete music_database_admin --instance kin-project-postgresql-v2
gcloud secrets delete music_service_settings
gcloud secrets delete music_admin_password
gcloud run services delete music-service
