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
                    // Ensure the parameter is not empty
                    if (params.NEW_REPO_URL.trim()) {
                        withEnv(["NEW_REPO_URL=${params.NEW_REPO_URL}"]) {
                            echo "Starting Python script execution"
                            try {
                                bat 'python templatee.py'
                            } catch (Exception e) {
                                error "Python script execution failed: ${e.getMessage()}"
                            }
                            echo "Finished Python script execution"
                        }
                    } else {
                        error "NEW_REPO_URL parameter is empty."
                    }
                }
            }
        }
    }
}
