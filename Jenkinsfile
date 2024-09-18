pipeline {
    agent any
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'New repository URL to update in YAML files')
    }
    environment {
        // Ensure that the NEW_REPO_URL environment variable is available in all stages
        NEW_REPO_URL = "${params.NEW_REPO_URL}"
    }
    stages {
        stage('Set Environment') {
            steps {
                script {
                    if (!env.NEW_REPO_URL) {
                        error("The environment variable 'NEW_REPO_URL' must be set.")
                    }
                    echo "NEW_REPO_URL is set to: ${env.NEW_REPO_URL}"
                }
            }
        }
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
                    bat 'python modify_yaml.py'
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
    post {
        always {
            script {
                echo 'Pipeline complete.'
            }
        }
        success {
            script {
                echo 'Changes have been successfully pushed.'
            }
        }
        failure {
            script {
                echo 'Pipeline failed.'
            }
        }
    }
}
