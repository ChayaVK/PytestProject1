pipeline {
    agent any
    options { timestamps() }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    source .venv/bin/activate
                    pytest --junitxml=report.xml --html=report.html --self-contained-html
                """
            }
        }
    }
}
