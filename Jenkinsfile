pipeline {
    stages {
        stage('build') {
            withEnv(["PATH=$PATH:~/.local/bin"]){
                sh "bash down.sh"
                sh "bash up.sh"
            }
        }
    }
}