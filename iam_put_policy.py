import boto3
import json

# Initialize IAM client
iam = boto3.client(
    'iam',
    region_name='us-east-1',
    aws_access_key_id="AKIAAIDAYRANYAHGQOHD",
    aws_secret_access_key="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",
)

# Define policy document
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["ssm:SendCommand"],
            "Resource": [
                "arn:aws:ec2:us-east-1:748127089694:instance/i-0415bfb7dcfe279c5",
                "arn:aws:ec2:us-east-1:748127089694:document/RestartServices"
            ]
        }
    ]
}

# Define parameters for the put_user_policy call
user_name = "haug"  # Replace with your IAM user's name
policy_name = "SendCommandPolicy"  # Define a name for your policy

try:
    # Attach the policy to the user
    response = iam.put_user_policy(
        UserName=user_name,
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)  # Convert the policy document to JSON string
    )
    print("Policy successfully attached to the user.")
except Exception as e:
    print(f"An error occurred: {e}")
