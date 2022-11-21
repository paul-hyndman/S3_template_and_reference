#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from resource_stacks.s3_cdk_template_stack import S3CdkTemplateStack

app = cdk.App()
S3CdkTemplateStack(app, "S3CdkTemplateStack")

app.synth()
