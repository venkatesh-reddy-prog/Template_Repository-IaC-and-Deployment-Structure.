pipeline {
    agent any

    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'The new repository URL to be used for updating YAML files')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    bat 'pip install gitpython pyyaml'
                }
            }
        }
        
        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning repository...'
                    bat 'python clone_repo.py'
                }
            }
        }
        
        stage('Update YAML Files') {
            steps {
                script {
                    echo 'Updating YAML files...'
                    bat "set NEW_REPO_URL=${params.NEW_REPO_URL} && python update_yaml.py"
                }
            }
        }

        stage('Push Changes') {
            steps {
                script {
                    echo 'Pushing changes to the repository...'
                    bat "python git_operations.py"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
