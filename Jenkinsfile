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
                    call venv\\Scripts\\activate
                    python -m pytest .
                """
            }
        }
    }
}
