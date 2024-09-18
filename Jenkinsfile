pipeline {
    agent any
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'New repository URL to update in YAML files')
    }
    stages {
        stage('Check Python Path') {
            steps {
                script {
                    echo 'Checking Python version and path...'
                    bat 'where python'
                    bat 'python --version'
                }
            }
        }
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/venkatesh-reddy-prog/Template_Repo']])
            }
        }
        stage('Run Python Script') {
            steps {
                script {
                    echo 'Starting Python script execution...'
                    bat 'python templatee.py'
                    echo 'Python script execution completed.'
                }
            }
        }
        stage('Check Git Status and Commit') {
            steps {
                script {
                    echo 'Checking for changes...'
                    def status = bat(script: 'git status --porcelain', returnStdout: true).trim()
                    if (status) {
                        echo "Changes detected, committing..."
                        bat 'git add bic/applications/*.yaml'
                        bat 'git commit -m "Update repoURL in YAML files"'
                        echo "Pushing changes to remote..."
                        bat 'git push origin main'
                    } else {
                        echo "No changes to commit."
                    }
                }
            }
        }
    }
}
