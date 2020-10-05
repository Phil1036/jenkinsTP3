pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
		echo "Etape de build"
			
			}
		}
		stage('Test') {
			steps {
				echo "Etape de test"
			}
		}
		stage('Deploy') {
			steps {
				echo "Etape de deploiement"
			}
		}
	}
}	