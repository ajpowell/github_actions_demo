# github-actions-demo

### initialise local git repository...
`git init`
### add the files...
`git add .`
### and commit them...
`git commit -m 'First commit'`

### rename master branch to main
`git branch -M main`
### set remote to existing, empty github repository
`git remote add origin [github repo path]`
### push up the files
`git push origin main`


## Github actions

Install extension 'GitHub Actions'

### Ensure we are on the main branch
`git checkout main`

### Create folder in root of project
`mkdir .github`

### Create subfolder workflows
`mkdir .github\workflows`

### within workflows folder, create yml file for your actions
`vi .github\workflows\flask-test.yml`

