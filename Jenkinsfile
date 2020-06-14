pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps{
                sh "bash down.sh"
                sh "bash up.sh"
            }
        }
    }
}
