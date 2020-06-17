pipeline{
	agent any
		stages {
			stage(job1){
				steps {
					echo 'Hi, this is nirmal'
				}
			}
			stage(safejob) {
				steps {
					input('Do u want to proceed')
				}
			}
			stage(privaterepository) {
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
			        
