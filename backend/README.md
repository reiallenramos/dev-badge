# dev-badge-backend

## Running locally
```bash
FLASK_APP=app/main.py flask run -p 56733
```

## Publish as docker image (optional)
```
docker build -t reiallenramos/dev-badge-backend:latest .
docker build -t reiallenramos/dev-badge-backend:vX.X.X .

docker push reiallenramos/dev-badge-backend:latest
docker push reiallenramos/dev-badge-backend:vX.X.X
```

## Personal dev notes
The following are personal notes and won't apply to forked repos.

### Re-tag image and push to Google Container Registry
```
docker tag reiallenramos/dev-badge-backend:latest asia.gcr.io/dev-color-picker/backend:latest
docker push asia.gcr.io/dev-color-picker/backend:latest
```
### Re-deploy your service in Google Cloud Run
Navigate to your service's Details page. Click 'Edit & Deploy New Version'. Scroll down, then click 'Deploy'.
