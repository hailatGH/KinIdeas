gcloud config set account hailemichael.atrsaw@kinideas.com
gcloud config set project kin-project-352614

gcloud services enable \
  run.googleapis.com \
  sql-component.googleapis.com \
  sqladmin.googleapis.com \
  compute.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com \
  artifactregistry.googleapis.com

PROJECT_ID=$(gcloud config get-value core/project)
REGION=europe-west1

gcloud iam service-accounts create music-service-account

SERVICE_ACCOUNT=$(gcloud iam service-accounts list \
    --filter music-service-account --format "value(email)")

gcloud sql databases create music-database --instance kin-project-postgresql-v1

music_database_admin_password="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
gcloud sql users create music_database_admin --instance kin-project-postgresql-v1 --password $music_database_admin_password

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/cloudsql.client

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/storage.admin

GS_BUCKET_NAME=${PROJECT_ID}-storage
gsutil mb -l ${REGION} gs://${GS_BUCKET_NAME}

echo DATABASE_URL=\"postgres://music_database_admin:${music_database_admin_password}@//cloudsql/${PROJECT_ID}:${REGION}:kin-project-postgresql-v1/music-database\" > .env
echo GS_BUCKET_NAME=\"${GS_BUCKET_NAME}\" >> .env
echo SECRET_KEY=\"$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)\" >> .env
echo DEBUG=\"True\" >> .env

gcloud secrets create music_service_settings --data-file .env
gcloud secrets add-iam-policy-binding music_service_settings \
  --member serviceAccount:${SERVICE_ACCOUNT} --role roles/secretmanager.secretAccessor
rm .env

export PROJECTNUM=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export CLOUDBUILD=${PROJECTNUM}@cloudbuild.gserviceaccount.com

gcloud secrets add-iam-policy-binding music_service_settings \
  --member serviceAccount:${CLOUDBUILD} --role roles/secretmanager.secretAccessor

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:${CLOUDBUILD} --role roles/cloudsql.client

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member serviceAccount:${CLOUDBUILD} --role roles/storage.admin

music_admin_password="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"

echo -n "${music_admin_password}" | gcloud secrets create music_admin_password --data-file=-

gcloud secrets add-iam-policy-binding music_admin_password \
  --member serviceAccount:${CLOUDBUILD} --role roles/secretmanager.secretAccessor

gcloud builds submit --pack image=gcr.io/${PROJECT_ID}/music_service_image

gcloud builds submit --config migrate.yaml --substitutions _REGION=$REGION

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
     --member serviceAccount:${SERVICE_ACCOUNT} --role roles/secretmanager.secretAccessor

gcloud run deploy music-service \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/music_service_image \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:kin-project-postgresql-v1 \
  --set-secrets MUSIC_SERVICE_SETTINGS=music_service_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --allow-unauthenticated

MUSIC_SERVICE_URL=$(gcloud run services describe music-service \
  --platform managed \
  --region $REGION  \
  --format "value(status.url)")

gcloud secrets versions access latest --secret music_service_settings > temp_settings
echo MUSIC_SERVICE_URL=${MUSIC_SERVICE_URL} >> temp_settings
gcloud secrets versions add music_service_settings --data-file temp_settings
rm temp_settings

gcloud run services update music-service \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/music_service_image

gcloud secrets versions access latest --secret music_admin_password && echo ""

gcloud builds submit --pack image=gcr.io/${PROJECT_ID}/music_service_image

gcloud builds submit --config migrate.yaml --substitutions _REGION=$REGION

gcloud run services update music-service \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/music_service_image