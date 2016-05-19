====================================================
Matador-Deploy: Deployment Assister For Rancher
====================================================


### About this project
====================================================
The aim of this project was to create a simplfied build process for rancher when trying to use duplicate environments across a Production, Staging and Development environment. It allows the user to create one templated docker-compose and rancher-compose file and then add a configuration file that will provide your config where each of your environments differ. It heavily leverages the work done with the [rancher-compose](https://github.com/rancher/rancher-compose) module as well as the great work done over at [Rancher](http://rancher.com/). For more information on using their products, please see their documentation.


### Before we start
====================================================

This project uses the conventions and processes defined by [Docker](https://docs.docker.com/engine/userguide/intro/), [Docker Compose](https://docs.docker.com/compose/compose-file/), [Rancher](http://docs.rancher.com/rancher/latest/en/) and [Rancher Compose](http://docs.rancher.com/rancher/v1.0/zh/rancher-compose/). These are themselves quite are complicated tools that you will need to have a good understanding of to use this project. We will go into a little detail and provide some examples of these files, but for detailed usage instructions please see their respective documentation pages.
### Getting Started
====================================================

The Dependancies for this project include the following:

##### Python: [download link](https://www.python.org/downloads/)
Current this app has been tested in both Python 2.7 and 3.5. Test successful installation with the following command.

	$ python --version
	Python 2.7.11
or

	$ python3 --version
	Python 3.5.1
##### Python Package Index: [download link](https://pip.pypa.io/en/latest/installing/)
Pip should come with Python when you install the latest version, however a link is provided above if you are required to install is seperately. Test installing with the following command:

	$ pip --version
##### rancher-compose: [download link](https://github.com/rancher/rancher-compose)
Rancher Compose essentially turns your docker-compose files into rancher-compose files for uploading docker configurations to your Rancher Environment. It is easiest to install from a [binary of the latest release](https://github.com/rancher/rancher-compose/releases) and then if you are using a UNIX environment, simply copy it into the following directory on your system:

	/usr/local/bin

This will allow you to use it all across your terminal. Test installation with the following command:

	$ rancher-compose --version
	rancher-compose version v0.8.0

##### Docker: [download link](https://docs.docker.com/engine/installation/)
You will need to have the docker containers built and pushed up to [Docker Hub](https://hub.docker.com/) which you will also need an account for. See the example build section for more information on the required docker images and tags that you require to have setup on dockerhub for the application to work.

### Installing Matador-Deploy
====================================================

The matador-deploy script is provided on the PiPY network, so can easily be installed with the following command:

	$ pip install matador-deploy

Alternatively, it can be build from source by downloading the source code from github, navigation to the root of the git hub repository and running the following command:

	$ python setup.py install


### How it works
====================================================

The matador-deploy CLI is designed to solve two problems. The first is to allow you to create templates for your docker-compose.yml and rancher-compose.yml file and provide the sepearate configuration options between them in one config.yml file. The second, is to confirm that the rancher environment and api/secret keys are what you actually want to update.

#### File Structure
====================================================

The application is configured to look for a templates folder that will contain all the required templates and configuration files. Here is a sample node application structure:

	root/ ---|
			- database/
			- src/ ---|
					- client/
					- scripts/
					- scss/
					- server/

			- gulpfile.js
			- Makefile
			- package.json
			- README.md

To run the matador-deploy script while located in thr root directory you will need to create the three configuration files and add them into the templates directory:

	root/ ---|
			- database/
			- src/ ---|
					- client/
					- scripts/
					- scss/
					- server/

			- templates/ ---|
					- config.yml
					- docker-compose-template.yml
					- rancher-compose-template.yml

			- build/ <!-- This directory will be created within the script if it doesn't exist -->
			- gulpfile.js
			- Makefile
			- package.json
			- README.md

The build directory will be the location of your combined docker-compose.yml and rancher-compose.yml files that will be used when the application updates your rancher configuration. The contents of these files will be defined later in the project.

#### docker-compose-template.yml
====================================================

The docker-compose-template.yml file needs to follow the structure of a [standard docker compose file](https://docs.docker.com/compose/compose-file/) for which more documentation can be found at the link provided. However here is a basic example that uses a simple web image, load balancer, mongo database.

In short this file configures the connections between all your docker containers/images containers.

	# Example Docker Compose File

	lb:
  	  image: rancher/load-balancer-service
	  ports:
	    - "80:3000"
	  restart: always
	  links:
	    - web:web
	  labels:
	    io.rancher.scheduler.global: 'true'
	  tty: true
	  stdin_open: true
	web:
	  expose:
	    - 3000
	  links:
   	 - db:mongodb
	db:
	  image: mongo:3
	  container_name: mongodb
	  ports:
	    - "27017:27017"

This application does require that the main application container is called **web** as it uses this to dynamically generate the required docker images based on the environment that you are upgrading.

NOTE: Much like python, indentation is very important in .yaml files so be sure that everything is spaced correctly. [More information can be found in the officail YAML Docs](http://www.yaml.org/start.html)

#### rancher-compose-template.yml
====================================================

The rancher-compose-template.yml file needs to follow the structure of a [standard rancher compose file](http://docs.rancher.com/rancher/v1.0/zh/rancher-compose/commands/). Here is the basic instructions of what the rancher-compose file does from the Rancher Documenation:

*To enable features that are supported in Rancher, you can also have a rancher-compose.yml which extends and overwrites the docker-compose.yml. For example, scale of servives and health checks would be in the rancher-compose.yml file.*

An example file that connects with the above docker file is provided below.

	# Example Rancher Compose File

	lb:
  	  scale: 1
	  load_balancer_config:
    	name: lb config
	  health_check:
    	port: 42
	    interval: 2000
    	unhealthy_threshold: 3
	    healthy_threshold: 2
    	response_timeout: 2000

	web:
      scale: 2
	  health_check:
    	port: 3000
    	interval: 2000
	    unhealthy_threshold: 3
	    healthy_threshold: 2
    	response_timeout: 2000



#### config.yml file
====================================================

The config.yml file is where you can put all your specific environment configuration that will get copied and transferred into the docker compose file. Things like environment variables, or other specific varying configuration between your docker-compose.yml file for the different environments goes in here. An example is here and details will be explained afterwards.

	# Example Configuration File

	image_base: example/image
	project_name: example-project
	global:
	  web:
    	environment:
      	  - KEY=value
	dev:
  	  web:
    	environment:
      	  - NODE_ENV=dev
	    labels:
    	  io.rancher.scheduler.affinity:host_label: client=seed,env=development
	staging:
  	  web:
	    environment:
      	  - NODE_ENV=staging
	    labels:
   		  io.rancher.scheduler.affinity:host_label: client=seed,env=staging
          com.alessimutants.pods: version=0.1,branch=dev
	prod:
  	  lb:
    	labels:
      	io.rancher.scheduler.local: 'false'
	  web:
    	environment:
      	  - NODE_ENV=prod
    	labels:
    	  io.rancher.scheduler.affinity:host_label: client=seed,env=production
      	  io.rancher.scheduler.local: 'false'


NOTE: The names of the different environments must follow this convention.

**image_base:** This is the base dockerhub image name, it is **required**. The correct tags will be automatically added when searching for the specific environments particular tag. This is a convention that must be followed for the application to function correctly. For example, if our base dockerhub image name was seed/matador-deploy, then our required tags to correspond to our environments would be as follows:

*base:* seed/matador-deploy
*dev:* seed/matador-deploy:dev
*staging:* seed/matador-deploy:staging
*prod:* seed/matador-deploy:latest

These tags will be automatically appended depending on the environment flag you pass to the application when you run it in the command line.
Note: Your image tags in your docker-compose-template.yml should be overwritten by these conventions, so you do not require to add the image for your web container in your docker-compose.yml template.

**project_name:** This is the base name that will be given to your rancher environment when it is created in Rancher and is also **required**. It will simply add the environment name to the end of the base name as such if our project name was matador:

*base:* matador
*dev:* matador-dev
*staging:* matador-staging
*prod:* matador-prod

##### The Global and Environment Fields
====================================================

Depending on the environment that is passed to the command line application, the app will build in the configuration provided in the global and specfic enviroment field. Essentially, anything added in the global field will be added to the docker-compose.yml file regardless of the environment specified. The application will then add anything that is included in the field for the specific field that you are running the application with (eg: dev/staging/prod). Anything that is defined in the docker-compose.yml file will be added to where ever possible, lists and dictionaries will be added to however anything that is simply set to one variable will be overwritten by what is located in this config file.

NOTE: Again, the global config is added first, then the env specific config is added second. This means that the env specific config will overwrite any duplicate config from the global field.

#### The Build Folder
====================================================
This is where the output of the application will save the files that it is using when calling the rancher-compose command. It gives you a chance to see the output of the application incase there was an error when updating your rancher environment.



.
.
.
.
.


# Actually Using the Tool
====================================================

Okay, so that was a lot of background information, so how the hell do we actually run this thing?

### Foreword
====================================================

The application just needs to be run in a directory that has the /templates folder containing the 3 required files above. As the application only requires the yaml configuration files, as long as the templates folder is provided (and you are not inside it) then the deployment process should work.

### The Command
====================================================

The application is run with the following command:

	$ matador-deploy --url <rancher url> --key <rancher env key> --secret <rancher secret key> --env <dev|staging|prod>

**--url:** This refers to the rancher url that you are trying to upload your rancher configuration to.
**--key:** This is the API Key that needs to be created specifically for the rancher environment that you are trying to update.
**--secret:** This is the Secret Key of Password that is provided to you when you create a new API Key for your rancher environment.
**--env:** This is the environment that you wish to update. It takes one of the following options are <dev|staging|prod>

Example Usage to Update the Development Environment on a local rancher server:

	$ matador-deploy --url http://localhost:8080" --key 9F68C78 -secret pEkMsBYjcZNxhY4rzYu --env dev

#### Flags
====================================================

The following flags can also be passed to the application

Flags [-hfvd]
   	**-h**  Show the help documentation -- (will stop application from running unless force mode is also present)
    **-f**  Force Mode: force the application to run and supress all warnings
    **-v**  Verbose Mode: print additional messages are processes run
    **-d**  Development Mode: will bypass command line arguments and set default values for Rancher configuration

Example usaged with out previous command to run in Verbose and Force Mode:

	$ matador-deploy -vf --url http://localhost:8080" --key 9F68C78 -secret pEkMsBYjcZNxhY4rzYu --env dev

Finally, the version flag can also be passed to see the currently installed version, as well as the version of rancher-compose it is using.

	$ matador-deploy --version
	matador-deploy version v0.0.1
	rancher-compose version v0.8.0


### Additional Requirements and Tips
====================================================

One of the most annoying things is constantly having to copy your really long key files into the command, so you should add these keys as **variables in your bash profile**. This can be easily done by navigating to the root of your user directory and opening the .bash_profile and adding the keys to the end of it:

	$ cd ~/
	$ open .bash_profile

	# Add the following lines
	MYAPP_KEY_DEV=knsdjkfasflasdjfns
	MYAPP_SECRET_DEV=sdlf4jlnl42n2

NOTE: You will need these key value pairs for each of the different environments you have created.

#### How to create a Rancher API Key
====================================================

If you haven't used the command line or rancher-compose to update your application before, here is a qick guide on how to create a new Rancher Environment Key.

Open up the Rancher UI and Environment you wish to create a key for.
Click on the API tab at the top of the webpage.
Then click on the "Add Environment API Key" button.
Set a name and a description for it.
You will then get a popup that will show the KEY and the SECRET_KEY.
Save these somewhere (or add them straight to your .bash_profile as above)
Start Updating them environments!
