pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        REPORT_DIR = "${WORKSPACE}\\report"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\pip.exe install --upgrade pip
                call %VENV_DIR%\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Crée le dossier report s'il n'existe pas
                bat "if not exist %REPORT_DIR% mkdir %REPORT_DIR%"

                // Lancer pytest avec Selenium Edge headless
                bat """
                call %VENV_DIR%\\Scripts\\python.exe -m pytest tests\\formulaire_test.py --html=%REPORT_DIR%\\index.html --self-contained-html -v
                """
            }
        }
    }

    post {
        always {
            // Archive le rapport HTML pour Jenkins
            archiveArtifacts artifacts: 'report\\index.html', fingerprint: true
            echo "Rapport HTML disponible : ${REPORT_DIR}\\index.html"
        }

        failure {
            echo "Les tests ont échoué ! Vérifie le rapport HTML."
        }
    }
}
