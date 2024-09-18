pipeline {
    agent any
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'New repository URL to update in YAML files')
    }
    environment {
        NEW_REPO_URL = "${params.NEW_REPO_URL}"
    }
    stages {
        stage('Clone Repo') {
            steps {
                script {
                    echo 'Cloning repository...'
                    bat 'python clone_repo.py'
                }
            }
        }
        stage('Modify YAML Files') {
            steps {
                script {
                    echo 'Modifying YAML files...'
                    bat "python modify_yaml.py --new-repo-url=${NEW_REPO_URL}"
                }
            }
        }
        stage('Commit and Push Changes') {
            steps {
                script {
                    echo 'Committing and pushing changes...'
                    bat 'python git_commit_push.py'
                }
            }
        }
    }
}
