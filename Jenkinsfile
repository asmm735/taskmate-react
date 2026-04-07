pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/asmm735/taskmate-react.git'
            }
        }

        stage('Install Node Dependencies') {
            steps {
                bat 'npm install'
            }
        }

        stage('Build React App') {
            steps {
                bat 'npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t taskmate-react .'
            }
        }

        stage('Install Selenium') {
            steps {
                bat 'pip install selenium'
            }
        }

        stage('Run App Locally For UI Test') {
            steps {
                bat 'start /B npx serve -s build -l 3000'
                bat 'timeout /t 10'
            }
        }

        stage('Run Selenium Test') {
            steps {
                bat 'python tests\\test_homepage.py'
            }
        }
    }

    post {
        always {
            bat 'taskkill /F /IM node.exe || exit /b 0'
            archiveArtifacts artifacts: 'build/**/*', allowEmptyArchive: true
        }
    }
}