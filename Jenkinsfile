pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                git url: 'https://github.com/yang0425/machine_learning.git'
            }
        }
        stage ('Git log') {
            steps {
                sh 'git log -p -1'
            }
        }
    }
}