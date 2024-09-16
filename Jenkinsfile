pipeline {
    agent any

    parameters {
        string(name: 'REPO_URL', description: 'Repository URL to set in YAML files')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        durabilityHint('MAX_SURVIVABILITY')
        timeout(time: 1, unit: 'HOURS')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/venkatesh-reddy-prog/Template_Repo.git', credentialsId: 'WAS'
            }
        }

        stage('Modify YAML Files') {
            steps {
                script {
                    def yamlFile = 'additional-secrets-app.yaml'
                    def yamlContent = readYaml file: yamlFile
                    yamlContent.spec.sources.each { source ->
                        source.repoURL = params.REPO_URL
                    }
                    writeYaml file: yamlFile, data: yamlContent
                    echo "Modified file: ${yamlFile} with new repoURL: ${params.REPO_URL}"
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                sh 'git config --global user.email "your-email@example.com"'
                sh 'git config --global user.name "Your Name"'
                sh 'git add .'
                sh "git commit -m 'Update repoURL to ${params.REPO_URL}'"
                sh 'git push origin main'
            }
        }
    }

    post {
        success {
            echo 'Pipeline successful'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            cleanWs()
        }
    }
}
