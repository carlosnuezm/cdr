from aws_cdk import (
    Stack,
    aws_iam as iam
)
from constructs import Construct

class EcrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieve the role name from context variables
        service_name = self.node.try_get_context("service_name")
        
        # Define the IAM Role for AWS Batch
        batch_role = iam.Role(self, "BatchServiceRole",
            assumed_by=iam.ServicePrincipal("batch.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSBatchServiceRole")
            ],
            role_name=f"{service_name}-service-role"
        )
