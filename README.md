# vue2proj

## Project setup
```
npm install
```
## We need to use virtualenvironment now since there are python packages involved.
```
source env/bin/activate
pip install -r requirements.txt
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

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### In the event that you installed another python package and want to add it to the requirements.txt file, just delete the old file and type
```
pip freeze > requirements.txt
```