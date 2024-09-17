pipeline {
    agent any

    environment {
        // Set the new repository URL directly as an environment variable
        NEW_REPO_URL = 'https://your-new-repo-url.git' // Replace with your actual new repo URL
    }

    stages {
        stage('Checkout Template Repo') {
            steps {
                script {
                    // Clone the template repository
                    git url: 'https://github.com/venkatesh-reddy-prog/Template_Repo.git', branch: 'main'
                }
            }
        }

        stage('Run Update Script') {
            steps {
                script {
                    // Ensure Python and necessary packages are installed
                    bat 'pip install -r requirements.txt || echo "No requirements.txt file or installation failed"'

                    // Run the Python script
                    bat 'python templatee.py'
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                script {
                    // Check if there are changes
                    def changes = bat(script: 'git status --porcelain', returnStdout: true).trim()
                    
                    if (changes) {
                        // Commit and push changes if any
                        bat '''
                        git add .
                        git commit -m "Update repoURL in YAML files"
                        git push origin main
                        '''
                    } else {
                        echo "No changes to commit."
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
