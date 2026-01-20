pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        PYTHON = "${VENV_DIR}\\Scripts\\python.exe"
        PIP = "${VENV_DIR}\\Scripts\\pip.exe"
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/Rezak12345/Formulaire_Python.git', branch: 'main'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                python -m venv venv
                call ${PIP} install --upgrade pip
                call ${PIP} install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                REM --- Lancer les tests en headless ---
                ${PYTHON} -m pytest tests\\formulaire_test.py --html=report\\index.html --self-contained-html -v
                """
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportName: 'Rapport Tests',
                    reportDir: 'report',
                    reportFiles: 'index.html',
                    keepAll: true,               // ⚠️ Obligatoire
                    alwaysLinkToLastBuild: true,
                    allowMissing: false          // ⚠️ Obligatoire
                ])
            }
        }
    }

    post {
        always {
            echo "Build terminé. Vérifiez le rapport HTML."
        }
    }
}
