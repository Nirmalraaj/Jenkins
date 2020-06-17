pipeline{
	agent any
		stages {
			stage('one'){
				steps {
					echo 'Hi, this is nirmal'
				}
			}
			stage('two') {
				steps {
					input('Do u want to proceed')
				}
			}
			stage('three') {
				when {
					not {
						branch "master"
					}
				}
				steps {
					echo "hello"
				}
			}
}
}
			        
