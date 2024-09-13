pipeline {
    agent any

    environment {
        // Define environment variables
        REPO_URL = 'https://new-repo-url.com/repository.git'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Update YAML Files') {
            steps {
                script {
                    // Update YAML files using PowerShell
                    bat '''
                    PowerShell -Command "& {
                        Get-ChildItem -Recurse -Filter *.yaml | ForEach-Object {
                            (Get-Content $_.FullName) -replace '\\{\\{ .Values.repoURL1 \\}\\}', '%REPO_URL%' | Set-Content $_.FullName
                        }
                    }"
                    '''
                }
            }
        }

        stage('Commit Changes') {
            steps {
                script {
                    // Configure Git
                    bat "git config user.name 'jenkins'"
                    bat "git config user.email 'jenkins@example.com'"

                    // Add changes
                    bat "git add ."

                    // Commit changes
                    bat "git commit -m 'Update repoURL1 to %REPO_URL%'"

                    // Push changes
                    bat "git push origin HEAD"
                }
            }
        }
    }
}
