pipeline {
  agent any
  stages {
    stage('test') {
      post {
        always {
          junit 'test-reports/*.xml'
        }

      }
      steps {
        sh 'sh \'python testjenkins.py\''
      }
    }

  }
}