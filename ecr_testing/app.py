#!/usr/bin/env python3
import os
import aws_cdk as cdk
from ecr.ecr_stack import EcrStack

stack_name = self.node.try_get_context("stack_name")

app = cdk.App()
EcrStack(app, stack_name,)

app.synth()
