import boto3

cfn = boto3.resource('cloudformation')

for stack in cfn.stacks.all():

    if str(stack.creation_time)[0:7] == "2021-08":
        print(stack.name + " " + stack.stack_status + " " + str(stack.creation_time))
        #Delete Stack
        #stack.delete()


