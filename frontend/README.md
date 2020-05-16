# dev-badge-frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

## Publish as docker image (optional)
```
docker build -t reiallenramos/dev-badge-frontend:latest .
docker build -t reiallenramos/dev-badge-frontend:vX.X.X .

docker push reiallenramos/dev-badge-frontend:latest
docker push reiallenramos/dev-badge-frontend:vX.X.X
```


## Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Personal dev notes
The following are personal notes and won't apply to forked repos.

Before you begin, check `.env.production` if it uses the correct runtime environment variable to connect to the backend. If not, check the backend service's id (in Cloud Run), update `.env.production` then rebuild the image.

### Re-tag image and push to Google Container Registry
```
docker tag reiallenramos/dev-badge-frontend:latest asia.gcr.io/dev-color-picker/frontend:latest
docker push asia.gcr.io/dev-color-picker/frontend:latest
```
### Re-deploy your service in Google Cloud Run
Navigate to your service's Details page. Click 'Edit & Deploy New Version'. Scroll down, then click 'Deploy'.
