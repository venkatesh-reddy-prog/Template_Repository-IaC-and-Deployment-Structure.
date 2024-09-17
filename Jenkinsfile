pipeline {
    agent any

    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'The URL of the new repository')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Script') {
            steps {
                withEnv(["NEW_REPO_URL=${params.NEW_REPO_URL}"]) {
                    bat '''
                        python templatee.py
                    '''
                }
            }
        }
    }
}
