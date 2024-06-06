from aws_cdk import (
    # Duration,
    Stack,
    aws_ecr as ecr,
)
from constructs import Construct
import boto3


class CdrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Repository name to check and create
        ecr_name = 'testing'

        # Initialize Boto3 client for ECR
        ecr_client = boto3.client('ecr')

        # Function to check if repository exists
        def repository_exists(repo_name):
            try:
                response = ecr_client.describe_repositories(repositoryNames=[repo_name])
                return True
            except ecr_client.exceptions.RepositoryDoesNotExistException:
                return False

        # Check if the repository exists
        if not repository_exists(ecr_name):
            # Create ECR repository
            repository = ecr.Repository(
                self, 
                "Repo",
                repository_name=ecr_name,
                image_scan_on_push=True,
                image_tag_mutability=ecr.TagMutability.MUTABLE
            )

        
