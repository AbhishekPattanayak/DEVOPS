# Gitlab is a CI-CD tool which promotes continuous integration and continous deployment.

# To create a gitlab configuration file name the file as -> ".gitlab-ci.yml"

1. Inside the configuartion file, you will need to create the jobs

2. Jobs are most fundamental and are used to perform set to tasks. 

3. Example :- 

    build_job:  #You can name the jobs howver you want. 
    script:  #We are telling here to run a script.
        - echo "Hello this is Abhishek, learning GitLAB"

4. Understanding GitLAB logs :- The logs provide you with a keyword called as runners - Runners are small, may be docker instances on which the pipelines run. 


5. So basically if you create a 