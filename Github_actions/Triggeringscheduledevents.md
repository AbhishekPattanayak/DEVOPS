1. Schedule can use a cron expression to trigger a workflow at a specific time or day. 


2. on:  #Specifies on which time the workflow should run
        schedule:
            - cron: '30 5 * * 1,3'
   jobs:
       test_schedule:
        runs-on: ubunytu-latest # Specifies the image of the docker on which the job runs. 
        steps:  #Basically these are the steps which runs sequentially 
            - name: Not on Monday or Wednesday
              if: github.event.schedule != '30 5 * * 1,3'  #Condition if statisfied lets the step run. 
              run: echo "skip this step on Monday and Wednesday"