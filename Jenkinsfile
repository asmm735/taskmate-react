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
                bat '''
                call npm -v
                call node -v
                call npm install --no-audit --no-fund --verbose
                '''
            }
        }

        stage('Build React App') {
            steps {
                bat 'call npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'call docker build -t taskmate-react .'
            }
        }

        stage('Install Selenium') {
            steps {
                bat 'call pip install selenium'
            }
        }

        stage('Run App Locally For UI Test') {
            steps {
                bat 'start /B cmd /c "npx serve -s build -l 3000"'
                sleep 10
            }
        }

        stage('Run Selenium Test') {
            steps {
                bat 'call python tests\\test_homepage.py'
            }
        }
    }

    post {
        always {
            script {
                bat(returnStatus: true, script: 'taskkill /F /IM node.exe')
            }
            archiveArtifacts artifacts: 'build/**/*', allowEmptyArchive: true
        }
    }
}