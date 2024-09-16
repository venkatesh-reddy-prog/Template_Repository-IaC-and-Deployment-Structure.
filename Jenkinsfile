pipeline {
    agent any
    stages {
        stage('Clone GitHub Repository') {
            steps {
                git url: 'https://github.com/venkatesh-reddy-prog/Template_Repo', branch: 'main'
            }
        }
        
        stage('Update YAML Files') {
            steps {
                script {
                    def yamlFilePath = 'bic/applications/additional-secrets.yaml'
                    def yamlData = readYaml file: yamlFilePath
                    
                    // Check if the file exists and delete it before writing new data
                    def file = new File(yamlFilePath)
                    if (file.exists()) {
                        echo "File ${yamlFilePath} exists, deleting it..."
                        file.delete()
                    }

                    // Writing new YAML content
                    echo "Writing new YAML content..."
                    writeYaml file: yamlFilePath, data: yamlData
                    
                    echo "YAML file updated successfully!"
                }
            }
        }
    }
}
