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

        stage('Setup Python') {
            steps {
                sh '''
                python3 --version
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests with Pytest') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest tests/ --html=report.html --self-contained-html
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
            echo '❌ Des tests ont échoué'
        }
    }
}
