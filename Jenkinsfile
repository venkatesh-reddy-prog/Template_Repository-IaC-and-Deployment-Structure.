pipeline {
    agent any

    environment {
        NEW_REPO_URL = 'https://your-new-repo-url.git'
    }

    stages {
        stage('Checkout Template Repo') {
            steps {
                script {
                    git url: 'https://github.com/venkatesh-reddy-prog/Template_Repo.git', branch: 'main'
                }
            }
        }

        stage('Run Update Script') {
            steps {
                script {
                    bat 'python templatee.py'
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                script {
                    def changes = bat(script: 'git status --porcelain', returnStdout: true).trim()
                    
                    if (changes) {
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
}
