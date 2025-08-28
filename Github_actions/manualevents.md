1. You can trigger a workflow manually via GitHub UI, Github CLI or the Github REST API

2. To run the workflow manually the workflow must be configured to runon the "workflow_dispatch" event. 

Example: - 

on: 
    workflow_dispatch:
        inputs:
            name:
                description: 'Name of the person to greet'
                required: true
                type: string
            greeting:
                decription: 'Type of greeting
                required: true
                type: string
            data:
                description: 'Base64 encoded content of a file'
                required: false
                type: string

3. You can have 10 inputs for a workflow dispatch event. 

4. gh workflow run <workflow_file.yml> \
  --field name='Abhishek' \
  --field greeting='Hello' \
  --field data='U29tZSBiYXNlNjQgY29udGVudA=='

5. You can provide inputs to the workflow via the CLI as shown above. 
