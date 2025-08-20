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
    stage: deploy_stage
    script:
        - echo "whatever"
