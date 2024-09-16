pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS_ID = 'WAS' // Jenkins credentials ID for GitHub
        GITHUB_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo' // GitHub repository URL
        GIT_BRANCH = 'main' // Branch where the files are located
        NEW_REPO_URL = 'https://new.repoURL000.com' // New repoURL value
    }

    stages {
        stage('Clone GitHub Repository') {
            steps {
                // Cloning the repo with specific branch and credentials
                git branch: 'main', 
                    credentialsId: 'WAS', 
                    url: 'https://github.com/venkatesh-reddy-prog/Template_Repo'
            }
        }

        stage('Update YAML Files') {
            steps {
                script {
                    // Use a YAML parser to properly handle the file
                    def yamlFiles = [
                        'bic/applications/additional-secrets.yaml',
                        'bic/applications/btp-secrets.yaml',
                        'bic/applications/postgres-app.yaml'
                    ]

                    yamlFiles.each { filePath ->
                        def yamlContent = readYaml(file: filePath)
                        
                        // Update all repoURL fields in the YAML content
                        yamlContent.sources.each { source ->
                            if (source.repoURL) {
                                source.repoURL = "${env.NEW_REPO_URL}"
                            }
                        }
                        
                        // Write back the updated YAML content
                        writeYaml file: filePath, data: yamlContent
                    }
                }
            }
        }
    }
}
