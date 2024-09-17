pipeline {
    agent any
    parameters {
        string(name: 'NEW_REPO_URL', defaultValue: '', description: 'Enter the new repoURL value')
    }
    stages {
        stage('Cloning') {
            steps {
                script {
                    checkout([$class: 'GitSCM',
                      userRemoteConfigs: [[url: 'https://github.com/venkatesh-reddy-prog/Template_Repo.git', credentialsId: 'WAS']],
                      branches: [[name: '*/main']],
                      doGenerateSubmoduleConfigurations: false,
                      submoduleCfg: [],
                      useShallowClone: true
                    ])
                }
            }
        }
        stage('Modifying yaml files') {
            steps {
                script {
                    bat '''
                        python templatee.py
                    '''
                }
            }
        }
    }
}
