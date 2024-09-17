pipeline{
    agent any
    parameters{
        string(name: 'NEW_REPO_URL', defaultValue:'', description:'Enter the new repoURL value')
    }
    stages{
        stage('Cloning'){
            steps{
                script{
                    checkout scm
                }
            }
        }
        stage('Dependencies that need to be installed'){
            steps{
                script{
                    bat '''
                        pip install pyyaml gitpython
                    '''
                }
            }
        }
        stage('Modifying yaml files'){
            steps{
                script{
                    bat 'python templatee.py'
                }
            }
        }
    }
}

                    
