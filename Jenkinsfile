pipeline {
    agent any
    environment {
        GIT_CREDENTIALS_ID = 'WAS'
        REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo'
        BRANCH_NAME = 'main'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    git credentialsId: "${GIT_CREDENTIALS_ID}", url: "${REPO_URL}", branch: "${BRANCH_NAME}"
                }
            }
        }
        stage('Update YAML') {
            steps {
                script {
                    def filePath = 'bic/applications/additional-secrets.yaml'
                    def newRepoURL = 'https://new-repo-url.com/new-repo.git'
                    
                    // Read the YAML file
                    def yaml = readYaml file: filePath
                    
                    // Update the repoURL in sources
                    yaml.spec.sources.each { source ->
                        if (source.repoURL == 'https://github.tools.sap/BIC/bic-product-dev.git') {
                            source.repoURL = newRepoURL
                        }
                    }
                    
                    // Write the YAML file back
                    writeYaml file: filePath, data: yaml
                }
            }
        }
        stage('Commit Changes') {
            steps {
                script {
                    sh 'git config user.email "jenkins@example.com"'
                    sh 'git config user.name "Jenkins"'
                    sh 'git add bic/applications/additional-secrets.yaml'
                    sh 'git commit -m "Update repoURL in additional-secrets.yaml"'
                    sh 'git push origin ${BRANCH_NAME}'
                }
            }
        }
    }
}

