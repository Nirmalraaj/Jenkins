pipeline{
	agent any
	tools {
		jdk '1.8.0_252'
	}
	parameters {
        	choice(name: 'branch', choices: ['master', 'slave1', 'slave2'], description: 'Run on specific platform')
         }
	options {
		timestamps()
		
		
	}
	stages {
		stage('Display the path of jenkins'){
			steps {
				echo "this is building an job"
				echo "PATH = ${PATH}"
			}
		}
		stage('run the slave branch'){
			steps{
				
				echo "pulling th changes from ${params.branch}"
				git url :"https://github.com/Nirmalraaj/Jenkins", branch :"${params.branch}"
				sh 'python demo.py'
			}
		}
		stage('run the python code'){
			steps {
				sh 'python test.py'
			}
		}
		stage('email notifictaion'){
			steps {
				mail bcc: '', body: 'Hi error has occured', cc: '', from: '', replyTo: '', subject: 'Jenkins Pipeline', to: 'nirmal11.12.1998@gmail.com'
	
			}
		}
	}
}
