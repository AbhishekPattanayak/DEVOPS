# Gitlab is a CI-CD tool which promotes continuous integration and continous deployment.

# To create a gitlab configuration file name the file as -> ".gitlab-ci.yml"

1. Inside the configuartion file, you will need to create the jobs

2. Jobs are most fundamental and are used to perform set to tasks. 

3. Example :- 

    build_job:  #You can name the jobs howver you want. 
    script:  #We are telling here to run a script.
        - echo "Hello this is Abhishek, learning GitLAB"

4. Understanding GitLAB logs :- The logs provide you with a keyword called as runners - Runners are small, may be docker instances on which the pipelines run. 


5. So basically if you create tasks , the tasks would run parallely and there is a chance of the deploy stage being completed first which would fail. So stages are necessary to define which set of taskd should run first. 

6. Stages example:- 

stages:  #You declared two stages. 
    - build_stage
    - deploy_stage

build:
    stage: build_stage  #Here you are defining which stage is which. 
    script:
        - apt update -y
deploy:
    stage: deploy_stage   #Here is the second stage
    script:
        - echo "whatever"

7. Artifact - suppose the first build stage is downloading dependancies and the second stage should use the dependacies - this is just an example to understand artifact where the files/folders you create in any of the stages can be retained. 


8. Example of how you can use artifact:-

stages:
    -build_stage
    -deploy_stage

build:
    stage: build_stage
    script:
        - touch mylog.txt
    artifact:
        paths:
            - "Name of the file" #This is the file that you want to pass onto the next stage to execute

deploy:
    stage: deploy_stage
    script:
        - echo "Whatever"

9. Suppose you are deploying an application it will run on a continous loop, you can send the output to /dev/null 2>&1 & -> you atre sending standard error and standard output to null and & means the job or script will run on the background. 

10. You can also specify the images for your docker image in the Gitlab. 

stages:
    -build_stage
    -deploy_stage

build:
    stage: build_stage
    image: node  #This will change the image to node instead of the default image.  
    script:
        - touch mylog.txt
    artifact:
        paths:
            - "Name of the file" #This is the file that you want to pass onto the next stage to execute

deploy:
    stage: deploy_stage
    image: node #This will change the image to node instead of the default image.
    script:
        - echo "Whatever"

11. GitLab runners :- Observation, Runners are basically small instances which are used to run the CI/CD jobs. 

        - Gitlab SAAS Runners (These are shared runners and are managed by Gitlab)

        - Self managed Runners (Specific to your Project)