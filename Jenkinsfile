pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
        NEW_REPO_URL = 'https://new-repo-url.example.com/new-repo.git'
        YAML_FILE_PATH = 'bic/applications/additional-secrets.yaml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: "${GIT_REPO_URL}"
            }
        }

        stage('Update YAML') {
            steps {
                sh """
                    sed -i 's|repoURL: https://github.tools.sap/BIC/bic-product-dev.git|repoURL: ${NEW_REPO_URL}|' ${YAML_FILE_PATH}
                """
            }
        }

        stage('Commit Changes') {
            steps {
                sh """
                    git config user.name "B Venkatesh Reddy"
                    git config user.email "bvenkateshreddy87@gmail.com"
                    git add ${YAML_FILE_PATH}
                    git commit -m "Updated repoURL in additional-secrets.yaml"
                    git push origin HEAD
                """
            }
        }
    }
}
