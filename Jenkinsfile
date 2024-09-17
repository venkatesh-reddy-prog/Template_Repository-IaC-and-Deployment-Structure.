pipeline {
    agent any
    
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'The URL of the new repository')
    }
    
    stages {
        stage('Checkout and Run Script') {
            steps {
                checkout scm
                bat '''
                    echo Current directory:
                    cd
                    echo Python version:
                    python --version
                    echo Installing required packages...
                    pip install PyYAML GitPython
                    echo Directory contents:
                    dir
                    echo Setting NEW_REPO_URL environment variable...
                    set NEW_REPO_URL=%NEW_REPO_URL%
                    echo Running templatee.py...
                    python templatee.py
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        failure {
            echo 'The Pipeline failed. Check the console output for details.'
        }
    }
}
