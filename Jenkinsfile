pipeline {
    agent any

    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'The new repository URL to replace in YAML files')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/venkatesh-reddy-prog/Template_Repo.git']]
                ])
            }
        }
        
        stage('Run Script') {
            steps {
                script {
                    if (params.NEW_REPO_URL) {
                        withEnv(["NEW_REPO_URL=${params.NEW_REPO_URL}"]) {
                            echo "Starting Python script execution"
                            bat 'python templatee.py'
                            echo "Finished Python script execution"
                        }
                    } else {
                        error "NEW_REPO_URL parameter is required."
                    }
                }
            }
        }
    }
}
