pipeline {
    agent any

    stages {
        stage ('build'){
        steps{
            echo 'Build stage started.'
                sh 'git pull https://github.com/monkphin/BasicCRUD.git'
                sh 'docker kill $(docker ps -aq)'
                sh 'docker rm $(docker ps -aq)'
                sh 'docker-compose -f /var/lib/jenkins/workspace/QA_Project_main/docker-compose.yml up --build -d'

        }}

        stage ('test'){
        steps{
            echo 'Testing Start'
                sh 'pip install pytest'
                sh + python3 test_app.py
                sh 'python3 -m pytest test.py'
        }}

        stage ('Post Check'){
        steps{
                echo'Stopping Microservices'
                sh 'docker-compose -f /var/lib/jenkins/workspace/QA_Project_main/docker-compose.yml down'
                echo 'Microservices have stopped'
        }}

    }
}
