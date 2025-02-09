pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: '66142c87-d271-41f4-82d1-cbbee8e844d0', url: 'https://github.com/AngelsTech/Docker-and-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'email-credentials', usernameVariable: 'EMAIL_SENDER', passwordVariable: 'EMAIL_PASSWORD')]) {
                        sh """
                            docker run --rm \
                              -e EMAIL_SENDER="${EMAIL_SENDER}" \
                              -e EMAIL_PASSWORD="${EMAIL_PASSWORD}" \
                              -e EMAIL_RECEIVER="${EMAIL_SENDER}" \
                              ${IMAGE_NAME}
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Email sent successfully!"
        }
        failure {
            echo "❌ Email sending failed!"
        }
    }
}
