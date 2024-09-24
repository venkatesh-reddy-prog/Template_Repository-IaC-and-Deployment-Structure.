pipeline {
    agent any

    parameters {
        string(name: 'UPDATES', defaultValue: '', description: 'Environment variables for YAML modification')
        string(name: 'GIT_PAT', defaultValue: '', description: 'Personal Access Token for Git authentication')
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
                    echo "Pushing changes to repository..."
                    def repoUrl = "https://${params.GIT_PAT}:x-oauth-basic@github.com/venkatesh-reddy-prog/repo.git"
                    
                    bat """
                        git -C C:\\Users\\I751676\\Desktop\\Clone_Repo\\Demo1-Folder remote set-url origin ${repoUrl}
                        git -C C:\\Users\\I751676\\Desktop\\Clone_Repo\\Demo1-Folder add --all
                        git -C C:\\Users\\I751676\\Desktop\\Clone_Repo\\Demo1-Folder commit -m "Update YAML files"
                        git -C C:\\Users\\I751676\\Desktop\\Clone_Repo\\Demo1-Folder push
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
