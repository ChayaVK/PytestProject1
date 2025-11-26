pipeline {
    agent any
    options { timestamps() }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat """
                    python3 -m venv .venv
                    source .venv/bin/activate
                    py -m pip install --upgrade pip
                    py -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    source .venv/bin/activate
                    pytest --junitxml=report.xml --html=report.html --self-contained-html
                """
            }
        }
    }
}
