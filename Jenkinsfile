pipeline {
    agent any

    environment {
        IMAGE_NAME = 'taskmate-react'
        APP_PORT = '3000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Node Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Build React App') {
            steps {
                sh 'npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Install Browser + Selenium') {
            steps {
                sh '''
                    sudo apt-get update || apt-get update
                    sudo apt-get install -y chromium-driver chromium python3-pip || apt-get install -y chromium-driver chromium python3-pip
                    pip3 install --break-system-packages selenium || pip3 install selenium
                '''
            }
        }

        stage('Run App Locally For UI Test') {
            steps {
                sh '''
                    nohup npx serve -s build -l $APP_PORT > app.log 2>&1 &
                    sleep 10
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'python3 tests/test_homepage.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'app.log', onlyIfSuccessful: false
            sh 'pkill -f "serve -s build" || true'
        }
    }
}
