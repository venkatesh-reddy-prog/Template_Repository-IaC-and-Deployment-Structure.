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
                // Checkout the code from GitHub
                git url: "${GIT_REPO_URL}"
            }
        }

        stage('Update YAML') {
            steps {
                script {
                    def file = readFile(YAML_FILE_PATH)
                    def newFileContent = file.replaceAll(
                        /repoURL:\s*https:\/\/github.tools.sap\/BIC\/bic-product-dev\.git/,
                        "repoURL: ${NEW_REPO_URL}"
                    )
                    writeFile file: YAML_FILE_PATH, text: newFileContent
                }
            }
        }

        stage('Commit Changes') {
            steps {
                script {
                    sh 'git config user.name "jenkins"'
                    sh 'git config user.email "jenkins@example.com"'
                    sh 'git add ${YAML_FILE_PATH}'
                    sh 'git commit -m "Updated repoURL in additional-secrets.yaml"'
                    sh 'git push origin HEAD'
                }
            }
        }
    }
}
