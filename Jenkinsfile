pipeline {
    agent any

    parameters {
        string(name: 'UPDATES', defaultValue: '', description: 'Environment variables for YAML modification')
    }

    environment {
        PATH = "C:\Users\I751676\AppData\Local\Programs\Python\Python312\python.exe;$PATH"
        GIT_CLONE_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
        GIT_NEW_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
        CLONE_DIR = "${WORKSPACE}\\Clone_Repo\\Template_Repo"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo "Cloning repository..."
                    bat """
                        if not exist ${WORKSPACE}\\Clone_Repo mkdir ${WORKSPACE}\\Clone_Repo
                        python clone_repo.py
                    """
                }
            }
        }

        stage('Update YAML Files') {
            steps {
                script {
                    echo "Updating YAML files with environment variables: ${params.UPDATES}"
                    bat """
                        set updates=${params.UPDATES} && python update_yaml.py
                    """
                }
            }
        }

        stage('Push Changes to Repo') {
            steps {
                script {
                    echo "Pushing changes to new repository..."
                    bat """
                        python git_push.py
                    """
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
