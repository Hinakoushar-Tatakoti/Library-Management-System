pipeline{
      agent any{
          stages{
                stage('checkout'){
                        steps {
                           checkout scm
                        }
                }
                stage('Build environment'){
                        steps {
                           script {
                                   sh """
                                   pip install -r requirements.txt
                                   """
                           }
                        }
                }
                stage('Linting'){
                       steps {
                           script {
                                   sh """
                                    pylint **/*.py
                                   """
                           }
                        }
                }
                stage('Unit Testing'){
                       steps {
                           script {
                                   sh """
                                    python -m unittest discover -s tests/unit
                                   """
                           }
                        }
                }
                stage('Integration Testing'){
                       steps {
                           script {
                                   sh """
                                    python -m unittest discover -s tests/integration
                                   """
                           }
                        }
                }
          }
          post {
              always {
                 echo 'This will always run'
              }
              success {
                  echo 'This will run only if successful'
              }
              failure {
                      script {
                                msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
                      }
              }
              unstable {
                  echo 'This will run only if the run was marked as unstable'
              }
              changed {
                  echo 'This will run only if the state of the Pipeline has changed'
                  echo 'For example, if the Pipeline was previously failing but is now successful'
              }
          }
      }
}