import aws_cdk as cdk
from aws_cdk import cloudformation_include as cfn_inc
from aws_cdk import (
    core,
    aws_s3 as _s3
)
import json

class S3CdkTemplateStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        template = cfn_inc.CfnInclude(
            self, 
            "myS3BucketId",
            template_file= "cdk_templates/s3_template.json"
        )
        
        # Create bucket based on simple template file
        template_bucket = template.get_resource("TemplatedBucket")

        # Add a feature not present on template
        template_bucket.apply_removal_policy(core.RemovalPolicy.DESTROY)

        arn = core.Fn.get_att("TemplatedBucket", "Arn")

        # Get reference to created resource as a bucket using arn, but name can be used if that's known
        existing_bucket = _s3.Bucket.from_bucket_arn(
            self, 
            "Bucket", 
            arn.to_string()
        )

        core.CfnOutput(
            self,
            "bucketArn",
            value=f"{arn.to_string()}",
            description="templated bucket arn"
        )

        core.CfnOutput(
            self,
            "bucketName",
            value=f"{existing_bucket.bucket_name}",
            description="templated bucket name"
        )