pipeline {
    agent any
    stages {
        stage ('Git log') {
            steps {
                sh 'git log -p -1'
            }
        }
        stage ('Success'){
            steps {
                echo 'success!'
            }
        }
    }
}