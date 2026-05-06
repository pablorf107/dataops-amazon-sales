variable "aws_region" {
  description = "AWS region where the infrastructure will be deployed"
  type        = string
  default     = "eu-west-1"
}

variable "bucket_name" {
  description = "Unique name for the S3 bucket used by the DataOps project"
  type        = string
  default     = "dataops-amazon-sales-bucket"
}