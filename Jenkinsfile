pipeline {
    agent any
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/venkatesh-reddy-prog/Template_Repo']])
            }
        }
        stage('Run Python Script') {
            steps {
                script {
                    bat 'python templatee.py'
                }
            }
        }
        stage('Commit Changes') {
            steps {
                script {
                    def status = bat(script: 'git status --porcelain', returnStdout: true).trim()
                    if (status) {
                        bat 'git add bic/applications/*.yaml'
                        bat 'git commit -m "Update repoURL in YAML files"'
                        bat 'git push origin main'
                    } else {
                        echo "No changes to commit."
                    }
                }
            }
        }
    }
}
