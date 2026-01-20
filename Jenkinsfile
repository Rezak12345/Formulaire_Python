pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                python --version
                python -m venv %VENV_DIR%
                %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Generate Report') {
            steps {
                bat '''
                %VENV_DIR%\\Scripts\\activate
                pytest tests --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }

        success {
            echo '✅ Tests exécutés avec succès'
        }

        failure {
            echo '❌ Échec des tests – voir le rapport'
        }
    }
}
