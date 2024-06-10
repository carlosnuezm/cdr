from aws_cdk import (
    aws_ec2 as ec2,
    aws_ec2 as iam,
    Stack,
)
from constructs import Construct

class BatchStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service_name = "api-testing"

        vpc = ec2.Vpc.from_vpc_attributes(self, "VPC",
            vpc_id="vpc-048863e8d9f79408b",
            availability_zones=["us-west-2a", "us-west-2b", "us-west-2a", "us-west-2d"],
            private_subnet_ids=["subnet-069b65c7d6445250b", "subnet-0956e34abd6ad038f", "subnet-0c0aa0f953236a5d6", "subnet-04bfb39092394b11e"]
        )

        # Define the SecurityGroup for AWS Batch
        sg_batch = ec2.SecurityGroup(self, "SecurityGroup", 
            vpc=vpc, 
            security_group_name = f"{service_name}-security-group",
            allow_all_outbound=True
        )

        # Define the IAM Role for AWS Batch
        batch_role = iam.Role(self, "BatchServiceRole",
            assumed_by=iam.ServicePrincipal("batch.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSBatchServiceRole")
            ],
            role_name = f"{service_name}-service-role"
        )