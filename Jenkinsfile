pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps{
                echo "killing old docker processes"
                sh "/usr/local/bin/docker-compose rm -fs"
                echo "building docker containers"
                sh "/usr/local/bin/docker-compose up --build -d"
            }
        }
    }
}
