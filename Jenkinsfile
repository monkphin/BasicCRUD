pipeline {
    agent any

    stages {
        stage ('build'){
        steps{
            echo 'Build stage started.'
                sh 'git pull https://github.com/monkphin/BasicCRUD.git'
                sh 'docker-compose -f /var/lib/jenkins/workspace/QA_Project_main/docker-compose.yml up --build -d'

        }}

        stage ('test'){
        steps{
            echo 'Testing Start'
                sh 'pip install pytest'
                sh 'python -m pytest test_app.py'
        }}

        stage ('Post Check'){
        steps{
                echo'Stopping Microservices'
                sh 'docker-compose -f /var/lib/jenkins/workspace/QA_Project_main/docker-compose.yml down'
                echo 'Microservices have stopped'
        }}

    }
}
