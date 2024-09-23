pipeline {
    agent any

    parameters {
        string(name: 'UPDATES', defaultValue: '', description: 'Environment variables for YAML modification')
    }

    environment {
        PYTHON_PATH = 'C:\\Users\\I751676\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'  
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo "Cloning repository..."
                    bat "${PYTHON_PATH} clone_repo.py"
                }
            }
        }

        stage('Update YAML Files') {
            steps {
                script {
                    echo "Updating YAML files with environment variables: ${params.UPDATES}"
                    bat """
                        set updates=${params.UPDATES} && ${PYTHON_PATH} update_yaml.py
                    """
                }
            }
        }

        stage('Push Changes to Repo') {
            steps {
                script {
                    echo "Pushing changes to new repository..."
                    bat "${PYTHON_PATH} git_push.py"
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
