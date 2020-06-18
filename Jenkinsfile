pipeline{
	agent any
	tools {
		jdk 'JDK1.8'
	}
	options {
		timestamps()
		properties([[$class: 'JiraProjectProperty'], buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '5'))])
	}
	stages {
		stage('Display the path of jenkins'){
			steps{
				echo "this is building an job"
				echo "PATH = ${PATH}"
			}
		}
		stage('check the source code'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Nirmalraaj/Jenkins.git']]])
			}
		}
		stage('run the python code'){
			sh 'python test.py'
		}
	}
}