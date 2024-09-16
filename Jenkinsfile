pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS_ID = 'WAS' // Jenkins credentials ID for GitHub
        GITHUB_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo' // GitHub repository URL
        GIT_BRANCH = 'main' // Branch where the files are located
        NEW_REPO_URL1 = 'https://new.repoURL1.com' // New repoURL1 value
        NEW_REPO_URL2 = 'https://new.repoURL2.com' // New repoURL2 value
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
                    // Define paths to the YAML files
                    def yamlFiles = [
                        'bic/applications/additional-secrets.yaml',
                        'bic/applications/btp-secrets.yaml',
                        'bic/applications/postgres-app.yaml'
                    ]

                    // Loop through each YAML file and replace the repoURL values
                    yamlFiles.each { filePath ->
                        def fileContent = readFile(filePath)
                        fileContent = fileContent.replaceAll('repoURL1', "${env.NEW_REPO_URL1}")
                        fileContent = fileContent.replaceAll('repoURL2', "${env.NEW_REPO_URL2}")
                        writeFile(file: filePath, text: fileContent)
                    }
                }
            }
        }
    }
}
