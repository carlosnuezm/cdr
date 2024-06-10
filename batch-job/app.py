#!/usr/bin/env python3
import os
import aws_cdk as cdk
from batch.batch_stack import BatchStack

# stack_name = os.environ['STACK_NAME']
stack_name = "batch-job-stack"

app = cdk.App()
BatchStack(app, stack_name,)

app.synth()
