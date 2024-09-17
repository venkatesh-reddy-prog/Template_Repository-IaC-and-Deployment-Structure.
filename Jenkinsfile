pipeline {
    agent any

    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'New repository URL')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                    }
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    bat '''
                        pip install --upgrade pip
                        pip install PyYAML GitPython
                    '''
                }
            }
        }
        stage('Run Script') {
            steps {
                script {
                    bat '''
                        python templatee.py
                    '''
                }
            }
        }
    }
}
