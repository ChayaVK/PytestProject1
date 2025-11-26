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
                    python -m pip install allure-pytest
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    python -m pytest --alluredir=allure-results

                """
            }
        stage('Generate Allure Report') {
            steps {
                bat """
                    allure generate allure-results -o allure-report --clean
                """
            }
        }
            post {
                always {
                     archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
        }
    }
}
