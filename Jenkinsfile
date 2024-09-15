pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS_ID = 'your-github-credentials-id' // Jenkins credentials ID for GitHub
        GITHUB_REPO_URL = 'https://github.com/venkatesh-reddy-prog/Template_Repo' // GitHub repository URL
        GIT_BRANCH = 'main' // Branch where the files are located
        NEW_REPO_URL1 = 'https://new.repoURL1.com' // New repoURL1 value
        NEW_REPO_URL2 = 'https://new.repoURL2.com' // New repoURL2 value
    }

    stages {
        stage('Clone GitHub Repository') {
            steps {
                git branch: "${env.GIT_BRANCH}",
                    credentialsId: "${env.GITHUB_CREDENTIALS_ID}",
                    url: "${env.GITHUB_REPO_URL}"
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

                    // Loop through each YAML file and replace the repoURL values based on the template
                    yamlFiles.each { filePath ->
                        def fileContent = readFile(filePath)

                        // Replace placeholders for repoURL1 and repoURL2 in the template format
                        fileContent = fileContent.replaceAll(/\{\? \{\.Values\.repoURL1: ''\} : ''\}/, "${env.NEW_REPO_URL1}")
                        fileContent = fileContent.replaceAll(/\{\? \{\.Values\.repoURL2: ''\} : ''\}/, "${env.NEW_REPO_URL2}")

                        // Write the updated content back to the file
                        writeFile file: filePath, text: fileContent
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                script {
                    sh 'git config user.name "jenkins"'
                    sh 'git config user.email "jenkins@example.com"'
                    
                    // Add changes, commit, and push to GitHub
                    sh 'git add .'
                    sh 'git commit -m "Update repoURL values in YAML files based on template structure"'
                    sh "git push origin ${env.GIT_BRANCH}"
                }
            }
        }
    }
}
