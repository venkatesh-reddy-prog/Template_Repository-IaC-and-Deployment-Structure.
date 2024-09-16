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
        stage('List Files') {
            steps {
                script {
                    // List files in the directory for debugging
                    bat 'dir bic\\applications\\'
                }
            }
        }
        stage('Update YAML') {
            steps {
                script {
                    def filePath = 'bic/applications/additional-secrets.yaml'
                    def newRepoURL = 'https://new-repo-url.com/new-repo.git'
                    
                    // Check if file exists
                    if (fileExists(filePath)) {
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
                    } else {
                        error "File not found: ${filePath}"
                    }
                }
            }
        }
        stage('Commit Changes') {
            steps {
                script {
                    bat 'git config user.email "jenkins@example.com"'
                    bat 'git config user.name "Jenkins"'
                    bat 'git add bic\\applications\\additional-secrets.yaml'
                    bat 'git commit -m "Update repoURL in additional-secrets.yaml"'
                    bat 'git push origin ${BRANCH_NAME}'
                }
            }
        }
    }
}
