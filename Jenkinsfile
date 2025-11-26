pipeline {
    agent any
    options { timestamps() }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    python -m pip install allure-pytest
                    python -m pytest --alluredir=allure-results
                    allure generate allure-results -o allure-report --clean
                """
            }
            post {
                always {
                     archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
        }
    }
}
