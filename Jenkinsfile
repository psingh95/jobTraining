pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'sh \'python testjenkins.py\''
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
    }

  }
}
