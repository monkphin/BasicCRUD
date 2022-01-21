pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout[$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/monkphin/BasicCRUD.git]]]
            }
        }
        stage('Build') {
            steps {
                git 'https://github.com/monkphin/BasicCRUD.git'
                sh 'docker-compose -f /var/lib/jenkins/workspace/BasicCRUD/docker-compose.yml up --build -d'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'python -m pytest test_app.py'
            }
        }
    }
    stage('Stop') {
            steps{
                echo'Stop app has started'
                sh 'docker-compose -f /var/lib/jenkins/workspace/BasicCRUD/docker-compose.yml down'
                echo 'app has stopped'
            }
        }
    }
}