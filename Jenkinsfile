pipeline {
    agent any
    stages {
        stage('Deploy') {
            sh "bash down.sh"
            sh "bash up.sh"
        }
    }
}
