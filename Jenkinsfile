pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins"
        EMAIL_SENDER = "abdullahshahid984@gmail.com"
        EMAIL_PASSWORD = "gagjzglsdfwvjvbd"
        EMAIL_RECEIVER = "abdullahshahid984@gmail.com"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo.git' // Replace with your actual repo
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
                    sh """
                        docker run --rm \
                          -e EMAIL_SENDER=${EMAIL_SENDER} \
                          -e EMAIL_PASSWORD=${EMAIL_PASSWORD} \
                          -e EMAIL_RECEIVER=${EMAIL_RECEIVER} \
                          ${IMAGE_NAME}
                    """
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

