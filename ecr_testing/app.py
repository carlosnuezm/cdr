#!/usr/bin/env python3
import os
import aws_cdk as cdk
from ecr.ecr_stack import EcrStack

stack_name = os.environ['STACK_NAME']

app = cdk.App()
EcrStack(app, stack_name,)

app.synth()
