pipeline {
    agent any

    parameters {
        string(name: 'REPO_URL', description: 'Repository URL to set in all YAML files')
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to modify')
    }

    stages {
        stage('Checkout') {
            steps {
                bat "git config --global core.longpaths true"
                checkout([$class: 'GitSCM', 
                    branches: [[name: "*/${params.BRANCH}"]], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/venkatesh-reddy-prog/Template_Repo', 
                        credentialsId: 'WAS'
                    ]]
                ])
            }
        }

        stage('Modify YAML Files') {
            steps {
                script {
                    def yamlFiles = [
                        'bic/applications/additional-secrets.yaml',
                        'bic/applications/btp-secrets.yaml',
                        'bic/applications/postgres-app.yaml'
                    ]
                    
                    yamlFiles.each { file ->
                        if (fileExists(file)) {
                            def content = readFile(file)
                            def modifiedContent = content.replaceAll(
                                /repoURL:\s*['"](https:\/\/[^'"]+)['"]/, 
                                "repoURL: \"${params.REPO_URL}\""
                            )
                            writeFile file: file, text: modifiedContent
                            echo "Modified file: ${file} with new repoURL: ${params.REPO_URL}"
                        } else {
                            echo "File ${file} does not exist. Skipping."
                        }
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'WAS', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    bat """
                        git config user.email "jenkins@example.com"
                        git config user.name "Jenkins"
                        git add bic/applications/*.yaml
                        git diff --quiet && git diff --staged --quiet || (git commit -m "Update repoURL in YAML files" && git push https://%GIT_USERNAME%:%GIT_PASSWORD%@github.com/venkatesh-reddy-prog/Template_Repo.git ${params.BRANCH})
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
