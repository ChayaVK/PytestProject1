pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    if exist requirements.txt (
                        python -m pip install -r requirements.txt
                    )
                """
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pytest --alluredir=allure-results
                    allure generate allure-results -o allure-report --clean
                """
            }
        }

        
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
            junit 'allure-results/*'  // Optional: if you want Jenkins test results view
        }
    }
}
