pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main' , url: 'https://github.com/Abdullahshahid984/Docker-and-jenkins.git'
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
                              -e EMAIL_SENDER="abdullahshahid984@gmail.com" \
                              -e EMAIL_PASSWORD="gagj zgls dfwv jvbd" \
                              -e EMAIL_RECEIVER="abdullahshahid984@gmail.com" \
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
