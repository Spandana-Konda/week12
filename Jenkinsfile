pipeline{
    agent any
    stages{
        stage('Run selenium using pytest'){
            steps{
                echo 'Run selenium using pytest'
                bat "python -m pip install -r requirements.txt"
            }
        }
        stage('docker login'){
            steps{
                echo 'login to docker'
                bat "docker login"
            }
        }
        stage('Build Docker Image'){
                bat 'docker build -t my-flask-app .'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application...'
                bat
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying the application...'
                bat 'docker run -d -p 5000:5000 my-flask-app'
            }
        }
    }
}