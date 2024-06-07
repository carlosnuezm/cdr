#!/usr/bin/env python3
import os
import aws_cdk as cdk
from ecr.ecr_stack import EcrStack


app = cdk.App()
EcrStack(app, "EcrStack",)

app.synth()
