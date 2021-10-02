pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        bat 'python jenkinstest.py'
      }
    }

    stage('Test') {
      steps {
        bat 'python test_jenkins.py'
      }
    }

  }
}