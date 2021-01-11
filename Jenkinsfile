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
                stage('Compile stage'){
                        steps {
                           withMaven(maven : 'maven_3.6.3') {
                               sh 'mvn clean compile'
                           }
                        }
                }
                stage('Unit Testing'){
                       steps {
                           withMaven(maven : 'maven_3_5_0') {
                               sh 'mvn test'
                           }
                        }
                }
                stage('Deployment Stage'){
                       steps {
                           withMaven(maven : 'maven_3_5_0') {
                               sh 'mvn deploy'
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