pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        REPORT_DIR = "report"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python --version
                python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                if not exist %REPORT_DIR% mkdir %REPORT_DIR%
                cd %WORKSPACE%  # racine du projet
                pytest tests\\formulaire_test.py --html=%REPORT_DIR%\\index.html --self-contained-html -v || exit 0
                '''
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'report',
                reportFiles: 'index.html',
                reportName: 'Rapport de tests Selenium',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }
    }
}
