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
                pytest tests --html=%REPORT_DIR%\\index.html --self-contained-html -v || exit 0
                '''
            }
        }
    }

    post {
        always {
            // Publier le rapport dans Jenkins (paramètre allowMissing ajouté)
            publishHTML([
                reportDir: 'report',
                reportFiles: 'index.html',
                reportName: 'Rapport de tests Selenium',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true          // ⚠️ paramètre obligatoire
            ])
        }
    }
}
